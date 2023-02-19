from django import forms
from django.db import models
from .models import ToDoList


class CreateNewList(forms.ModelForm):
    class Meta:
        model = ToDoList
        fields = ['name','website','email','username','password']


