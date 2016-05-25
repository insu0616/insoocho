from django.shortcuts import render
from .models import Post
from django.views import generic
from django.views.generic import View
# Create your views here.

class IndexView(generic.ListView):
    template_name = "blog/index.html"
    context_object_name = "posts"

    def get_queryset(self):
        return Post.objects.all()

class DetailView(generic.DetailView):
    model = Post
    template_name = "blog/detail.html"