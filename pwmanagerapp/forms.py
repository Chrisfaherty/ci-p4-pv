from django import forms
from django.db import models
from .models import PwAccount


class CreateNewPwAccount(forms.ModelForm):
    class Meta:
        model = PwAccount
        fields = ['name','website','email','username','password']


