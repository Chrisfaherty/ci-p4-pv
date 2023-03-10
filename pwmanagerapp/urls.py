from django.urls import path
from . import views

# These are the urls connect ignt he views to the links
urlpatterns = [
    path("<int:id>", views.index, name="index"),
    path("", views.home, name="home"),
    path("create/", views.create, name="create"),
    path("view/", views.view, name="view"),
    path("edit/", views.edit, name="edit")
]