from typing import Any,Dict
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.db.models import QuerySet
from render_block import render_block_to_string

from abstractapp.custom_context_processors import global_context

from .models import Blog, Category
# Create your views here.



class BlogList(ListView):
    template_name = 'blog/blog.html'
    paginate_by = 12
    extra_context = {'partial_template_path': 'blog/partial/main-list.html'}

    def dispatch(self, request, *args, **kwargs):
        category_path = self.kwargs['category_path']
        category_slug = category_path.split('/').pop()
        self.category = get_object_or_404(Category, slug=category_slug)
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        blogs = Blog.objects.filter(
            category__in=self.category.get_descendants(include_self=True))
        return blogs

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)

        # 处理面包屑
        breadcrumbs = []
        for ancestor in self.category.get_ancestors(include_self=True):
            breadcrumbs.append({
                'name': ancestor.name,
                'url': ancestor.get_absolute_url()  # 调用方法以获取URL
            })
        context['breadcrumbs'] = breadcrumbs

        # 添加标题 - 类别名
        context['main_title'] = self.category.name

        return context

    def render_to_response(self, context: Dict[str, Any], **response_kwargs: Any) -> HttpResponse:
        if self.request.headers.get('HX-Request') == 'true':
            if self.request.headers.get('source') == 'navBar':
                html = render_block_to_string('blog/blog.html','content',{**context,**global_context(self.request)})
                return HttpResponse(html)
            return render(self.request, 'blog/partial/main-list.html', context)
        return super().render_to_response(context, **response_kwargs)


class BlogDetail(DetailView):
    template_name = 'blog/blog.html'
    model = Blog
    extra_context = {'partial_template_path': 'blog/partial/main-detail.html'}

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
                # 获取上一个和下一个对象
        previous_object = Blog.objects.filter(category=self.object.category).filter(id__lt=self.object.id).order_by('-id').first()
        next_object = Blog.objects.filter(category=self.object.category).filter(id__gt=self.object.id).order_by('id').first()

        # 将上一个和下一个对象添加到上下文中
        context['previous_object'] = previous_object
        context['next_object'] = next_object

        # 创建面包屑列表
        category = self.object.category
        breadcrumbs = []

        for ancestor in category.get_ancestors(include_self=True):
            breadcrumbs.append({'name': ancestor.name, 'url': ancestor.get_absolute_url()})
        
        # 为当前产品添加一个面包屑
        breadcrumbs.append({'name': self.object.title, 'url': self.object.get_absolute_url()})
        context['breadcrumbs'] = breadcrumbs  # 添加到上下文中

        # 添加标题-产品名
        context['main_title'] = self.object.title

        return context

    def render_to_response(self, context: dict[str, Any], **response_kwargs: Any) -> HttpResponse:
        # print(self.request.headers)
        if self.request.headers.get('HX-Request') == 'true':
            # This is an HTMX request
            # Your logic for handling HTMX request goes here
            if self.request.headers.get('source') == 'navBar':
                html = render_block_to_string('blog/blog.html','content',{**context,**global_context(self.request)})
                # print('获取了header')
                return HttpResponse(html)
            # print('没有获取header')
            return render(self.request, 'blog/partial/main-detail.html', context)
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

    def render_to_response(self, context: dict[str, Any], **response_kwargs: Any) -> HttpResponse:
        if self.request.headers.get('HX-Request') == 'true':
            html = render_block_to_string('blog/blog-index.html', 'content', {**context,**global_context(self.request)})
            return HttpResponse(html)  
        return super().render_to_response(context, **response_kwargs)