from django.db import models
from django.contrib.auth.models import User
from django_cryptography.fields import encrypt


# This is the fields for the password account inputs & the passwod input is encrypted
class PwAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="pwaccount", null=True)
    name = models.CharField(max_length=200)
    website = models.CharField(max_length =100)
    email = models.EmailField(max_length =100)
    username = models.CharField(max_length =50)
    password = encrypt(models.CharField(max_length=50, blank=False))

    def __str__(self):
	    return self.name

    

