from django.shortcuts import render, redirect, get_object_or_404
from .models import Password
from .forms import AccountForm
from passwordmanager import encryption
from cryptography.fernet import Fernet


def get_passmanager(request):
    passwords = Password.objects.all()
    context = {
        'passwords': passwords
    }
    return render(request, 'passmanager.html', context)


def add_password(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            response.useraccount.Password.set.create(name=n)
            form.save()
            return redirect('get_passmanager')
    form = AccountForm()
    context = {
        'form': form
    }
    return render(request, 'add_password.html', context)


def edit_password(request, password_id):
    passwords = get_object_or_404(Password, id=password_id)
    if request.method == 'POST':
        form = AccountForm(request.POST, instance=passwords)
        if form.is_valid():
            form.save()
            return redirect('get_passmanager')
    form = AccountForm(instance=passwords)
    context = {
        'form': form
    }
    return render(request, 'edit_password.html', context)


def delete_password(request, password_id):
    passwords = get_object_or_404(Password, id=password_id)
    passwords.delete()
    return redirect('get_passmanager')


def view(response):
    return render(response,'view.html',{})

