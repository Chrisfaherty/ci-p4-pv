from django.shortcuts import render, redirect
from .models import Password

# Create your views here.

def get_passmanager(request):
    passwords = Password.objects.all()
    context = {
        'passwords': passwords
    }
    return render(request, 'passmanager.html', context)


def add_password(request):
    if request.method == 'POST':
        name = request.POST.get('password_name')
        password = request.POST.get('password_password')
        Password.objects.create(name=name, password=password)

        return redirect('get_passmanager')
    return render(request, 'add_password.html')