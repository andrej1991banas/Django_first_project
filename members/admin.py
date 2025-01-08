from django.contrib import admin
from .models import Member


# Register your models here.

class MemberAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "firstname", "lastname", "email", "entries", "joined_date")


admin.site.register(Member, MemberAdmin)
