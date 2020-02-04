from django import forms
from users.models import User
from django.core import validators


class NewUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
