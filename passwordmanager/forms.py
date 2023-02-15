from django import forms
from .models import Password


class AccountForm(forms.ModelForm):
    class Meta:
        model = Password
        fields = ['name','website','email','username','password','message']


