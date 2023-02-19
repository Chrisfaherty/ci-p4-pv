from django import forms
from .models import ToDoList


class AccountForm(forms.ModelForm):
    class Meta:
        model = ToDoList
        fields = ['name','website','email','username','password']


