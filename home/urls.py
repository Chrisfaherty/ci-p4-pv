from django.urls import path
from home.views import GetHomeView

# This is the the url to connect the home view to the home page
app_name = 'home'

urlpatterns = [
    path('', GetHomeView.as_view(), name='home'),
]

    