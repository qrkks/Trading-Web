from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Blog
# Create your views here.

class BlogList(ListView):
    template_name = 'blog/blog-list.html'
    model = Blog

class BlogDetail(DetailView):
    template_name = 'blog/blog-detail.html'
    model = Blog
