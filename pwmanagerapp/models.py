from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class ToDoList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todolist", null=True) # <--- added
    name = models.CharField(max_length=200)
    website = models.CharField(max_length =100)
    email = models.EmailField(max_length =100)
    username = models.CharField(max_length =50)
    password = models.CharField(max_length =50, blank=False)

    def __str__(self):
	    return self.name


class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)

    def __str__(self):
	    return self.text
    

