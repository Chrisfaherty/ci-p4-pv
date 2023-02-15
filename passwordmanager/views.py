from django.shortcuts import render
from .models import Password

# Create your views here.

def get_passmanager(request):
    passwords = Password.objects.all()
    context = {
        'password': passwords
    }
    return render(request, 'passmanager.html', context)


def add_password(request):
    return render(request, 'add_password.html')