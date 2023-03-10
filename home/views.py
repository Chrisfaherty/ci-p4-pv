from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import generic
from blog.models import Post

# This is to get the home view and also get the latest 3 blog posts to display

class GetHomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(GetHomeView, self).get_context_data(**kwargs)
        context['post_list'] = Post.objects.all().order_by("-created_on")[:3]
        return context


