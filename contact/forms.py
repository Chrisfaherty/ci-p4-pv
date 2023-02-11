from django.forms import ModelForm
from .models import Contact


class ContactForm(ModalForm):
    class Meta:
        model = Contact()
        fields = '__all__'