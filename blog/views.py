from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.db.models import QuerySet

from .models import Blog, Category
# Create your views here.

class BlogList(ListView):
    template_name = 'blog/blog-list.html'

    def get_queryset(self):
        category_path:str = self.kwargs['path']
        category_slug = category_path.split('/').pop()
        category:Category = get_object_or_404(Category,slug=category_slug)
        blogs = Blog.objects.filter(category__in = category.get_descendants(include_self=True))
        return blogs
    
    

class BlogDetail(DetailView):
    template_name = 'blog/blog-detail.html'
    model = Blog

def blog_index(request):
    root_nodes = Category.objects.filter(level=1)

    root_nodes_data = {}
    for root_node in root_nodes:
        blogs:QuerySet[Blog] = Blog.objects.filter(category__in=root_node.get_descendants(include_self=True))[:3]
        root_nodes_data[root_node] = blogs

    context = {
        'root_nodes_data':root_nodes_data,
    }
    # print(f"context:{context}")
    return render(request,'blog/blog-index.html',context)
