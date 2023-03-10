from django.urls import path
from . import views

# This is the urls for the contact createing links for the views
app_name = 'contact'

urlpatterns = [
    path('', views.ContactView.as_view(), name="contact"),
    path('success/', views.ContactSuccessView.as_view(), name="success"),
]