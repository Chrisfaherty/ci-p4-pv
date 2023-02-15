from django.db import models


class Password(models.Model):
    name = models.CharField(max_length =50, null=False, blank=False)
    website = models.URLField(max_length =100, null=False, blank=False)
    email = models.EmailField(max_length =100)
    username = models.CharField(max_length =50, null=False, blank=False)
    password = models.CharField(max_length =50, null=False, blank=False)
    message = models.TextField(max_length =250)

    def __str__(self):
        return self.name
        