from django.urls import path
from home.views import GetHomeView


app_name = 'home'

urlpatterns = [
    path('', GetHomeView.as_view(), name='home'),
]

    