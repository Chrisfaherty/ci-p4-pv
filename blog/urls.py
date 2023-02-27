from . import views
from django.urls import path

app_name = 'blog'

# These are the URLS used to create links for the blog templates and views.
urlpatterns = [
    path('', views.PostList.as_view(), name='blog'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]