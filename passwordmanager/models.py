from django.db import models
from django.contrib.auth.models import User


class Password(models.Model):
    useraccount = models.ForeignKey(User, related_name='useraccount', null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length =50, blank=False)
    website = models.CharField(max_length =100)
    email = models.EmailField(max_length =100)
    username = models.CharField(max_length =50)
    password = models.CharField(max_length =50, blank=False)
    message = models.TextField(max_length =250)

    def __str__(self):
        return self.name
        