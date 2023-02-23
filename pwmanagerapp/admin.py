from django.contrib import admin
from .models import PwAccount
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.

@admin.register(PwAccount)
class PWAdmin(SummernoteModelAdmin):
    
    list_display = ('name', 'website', 'email','username')
    exclude = ('password',)

# class PWadmin(admin.ModelAdmin):
#     list_display = ('name', 'website', 'email','username')
#     excludes = ('password',)