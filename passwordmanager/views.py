from django.shortcuts import render, redirect
from .models import Password
from .forms import AccountForm

# Create your views here.

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
            form.save()
            return redirect('get_passmanager')
    form = AccountForm()
    context = {
        'form': form
    }
    return render(request, 'add_password.html', context)