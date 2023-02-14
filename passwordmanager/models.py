from django.db import models


class Password(models.Model):
    name = models.CharField(max_length =50, null=False, blank=False)
    website = models.URLField()
    email = models.EmailField()
    username = models.CharField(max_length =50, null=False, blank=False)
    password = models.CharField(max_length =50, null=False, blank=False)
    message = models.TextField(max_length =250)