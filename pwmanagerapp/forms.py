from django import forms
from django.db import models
from .models import ToDoList


class CreateNewList(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
    website = forms.CharField(label="Website", max_length =100)
    email = forms.EmailField(label="Email", max_length =100)
    username = forms.CharField(label="Username", max_length =50)
    password = forms.CharField(label="Password", max_length =50)


