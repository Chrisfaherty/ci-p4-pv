from django.contrib import admin
from .models import PwAccount
from django_summernote.admin import SummernoteModelAdmin


# This is for the admin to be able to view the accounts stored but hide the passwords

@admin.register(PwAccount)
class PWAdmin(SummernoteModelAdmin):
    
    list_display = ('name', 'website', 'email','username')
    exclude = ('password',)
