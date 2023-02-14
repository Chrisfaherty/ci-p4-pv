from django.shortcuts import render

# Create your views here.

def get_passmanager(request):
    return render(request, 'passmanager.html')