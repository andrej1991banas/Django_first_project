from django import forms
from auth_members.models import MemberUser


class MemberUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)  # Ensure password is handled securely

    class Meta:
        model = MemberUser
        fields = ['username', 'email', 'first_name', 'last_name', 'password']  # Include required fields

    def save(self, commit=True):
        # Override save to handle password encryption
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])  # Hash the password
        if commit:
            user.save()
        return user