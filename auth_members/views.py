from django.shortcuts import render, redirect
from auth_members.forms import MemberUserForm
from django.contrib import messages



def create_member(request):
    if request.method == 'POST':
        form = MemberUserForm(request.POST)
        if form.is_valid():
            form.save()  # This saves the new `MemberUser` instance
            # messages.success(request, 'Member created successfully!')
            return redirect('mylogin')  # Replace `member_list` with your desired redirect URL
        # else:
        #     messages.error(request, 'Please correct the errors below.')
    else:
        form = MemberUserForm()

    return render(request, 'create_member.html', {'form': form})


