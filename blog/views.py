from typing import Any
from django import http
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.db.models import QuerySet

from .models import Blog, Category
# Create your views here.

class BlogList(ListView):
    template_name = 'blog/blog.html'
    paginate_by = 12
    extra_context = {'partial_template_path':'blog/partial/main-list.html'}

    def get_queryset(self):
        category_path:str = self.kwargs['path']
        category_slug = category_path.split('/').pop()
        category:Category = get_object_or_404(Category,slug=category_slug)
        blogs = Blog.objects.filter(category__in = category.get_descendants(include_self=True))
        return blogs
    
    def render_to_response(self, context: dict[str, Any], **response_kwargs: Any) -> http.HttpResponse:
        if self.request.headers.get('HX-Request') == 'true':
            # This is an HTMX request
            # Your logic for handling HTMX request goes here
            return render(self.request,'blog/partial/main-list.html',context)
        return super().render_to_response(context, **response_kwargs)

class BlogDetail(DetailView):
    template_name = 'blog/blog.html'
    model = Blog
    extra_context = {'partial_template_path':'blog/partial/main-detail.html'}

    def render_to_response(self, context: dict[str, Any], **response_kwargs: Any) -> http.HttpResponse:
        if self.request.headers.get('HX-Request') == 'true':
            # This is an HTMX request
            # Your logic for handling HTMX request goes here
            return render(self.request,'blog/partial/main-detail.html',context)
        return super().render_to_response(context, **response_kwargs)

# def blog_index(request):
#     root_nodes = Category.objects.filter(level=0)

#     root_nodes_data = {}
#     for root_node in root_nodes:
#         blogs:QuerySet[Blog] = Blog.objects.filter(category__in=root_node.get_descendants(include_self=True))[:3]
#         root_nodes_data[root_node] = blogs

#     context = {
#         'root_nodes_data':root_nodes_data,
#     }
#     # print(f"context:{context}")
#     return render(request,'blog/blog-index.html',context)

class BlogIndex(ListView):
    model = Blog
    paginate_by = 12
    template_name = "blog/blog-index.html"

