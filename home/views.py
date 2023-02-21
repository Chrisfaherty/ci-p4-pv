from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import generic




# Create your views here.
class GetHomeView(TemplateView):
    template_name = 'home.html'

