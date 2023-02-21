"""passwordvault URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from contact.views import ContactView, ContactSuccessView
from home.views import GetHomeView
from pwmanagerapp.views import create, view, index, edit, delete


urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', include('contact.urls'), name='contact_urls'),
    path('', GetHomeView.as_view(), name='home'),
    path("<int:id>", index, name="index"),
    path("create/", create, name="create"),
    path("view/", view, name="view"),
    path("edit/<ls_id>", edit, name="edit"),
    path("delete/<ls_id>", delete, name="delete"),
    path('summernote/', include('django_summernote.urls')),
    path("", include("blog.urls"), name="blog-urls"),
    path('accounts/', include('allauth.urls')),
]
