from django import forms
from django.contrib.auth.models import User

from users.models import UserProfileInfo, PaymentMethods, WebSites
from django.core import validators


class NewUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')


class NewUserInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfileInfo
        fields = ('profile_site', 'profile_pic', 'ucountry', 'ucity', 'ustreetAddress', 'umembership')


class NewPaymentMethodForm(forms.ModelForm):
    class Meta:
        model = PaymentMethods
        fields = ('paymethod',)


class NewWebsiteForm(forms.ModelForm):
    class Meta:
        model = WebSites
        fields = ('wname',)
