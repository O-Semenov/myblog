from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from blog.models import Post
from django.views.generic import ListView, DetailView

class index(ListView):
    model = Post
    template_name = 'blog/index.html'

class post_detail(DetailView):
    model = Post
    template_name = 'blog/post-detail.html'
