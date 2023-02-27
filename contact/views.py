from django.views.generic import FormView, TemplateView
from django.shortcuts import render
from .forms import ContactForm
from django.urls import reverse_lazy

# This is the contact form view

class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact:success')

    def form_valid(self, form):
        form.send()
        return super().form_valid(form)

# This is for the customer sucess image
class ContactSuccessView(TemplateView):
    template_name = 'success.html'
