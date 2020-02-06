from django import forms
from django.contrib.auth.models import User

from users.models import UserProfileInfo
from django.core import validators


class NewUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password')


class NewUserInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfileInfo
        fields = ('profile_site', 'profile_pic', 'ucountry','ucity','ustreetAddress','umembership')
