from bs4 import BeautifulSoup, NavigableString
from django.utils.html import escape, mark_safe
import re
from typing import Any
from django import http
from django.shortcuts import render
from blog.models import Blog
from products.models import Product
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from django.views.generic import ListView

# Create your views here.


# def search(request):
#     q = request.GET.get('q','').strip()
#     products = Product.objects.active().filter(
#         Q(name__icontains=q)|
#         Q(slug__icontains=q)|
#         Q(description__icontains=q)
#     )
#     if not products.exists():
#         products = "There are no products"

#     context = {
#         'products':products,
#         'partial_template_path':'products/partial/main-list.html'
#     }
#     if request.headers.get('HX-Request') == 'true':
#         return render(request,'products/partial/main-list.html',context)
#     return render(request,'products/product.html',context)

class ProductSearchView(ListView):
    model = Product
    template_name = 'products/product.html'  # 用于渲染产品列表的模板
    context_object_name = 'products'  # 可选，用于在模板中引用对象列表的变量名，默认是 'object_list'
    paginate_by = 12  # 每页显示 12 个产品
    extra_context = {
        'partial_template_path': 'products/partial/main-list.html',
    }

    def get_queryset(self):
        q = self.request.GET.get('q', '').strip()
        if not q or q.isspace():
            return Product.objects.none()

        q_list = [term for term in q.split() if term]

        query_product = Q()
        for term in q_list:
            query_product &= (Q(name__icontains=term) | Q(
                slug__icontains=term) | Q(description__icontains=term))

        results = Product.objects.filter(query_product)
        self.extra_context['main_title'] = f'{results.count()} results found for "{q}"'

        highlighted_results_product = []
        for product in results:
            highlighted_name = product.name
            highlighted_description = product.description
            for term in q_list:
                highlighted_name = highlight(highlighted_name, term)
                highlighted_description = highlight(
                    highlighted_description, term)
            # 将高亮属性动态添加到产品对象
            product.highlighted_name = highlighted_name
            product.highlighted_description = highlighted_description
            highlighted_results_product.append(product)

        return results

    def render_to_response(self, context, **response_kwargs):
        if self.request.headers.get('HX-Request') == 'true':
            return render(self.request, 'products/partial/main-list.html', context)

        return super().render_to_response(context, **response_kwargs)


def clear_results(request):
    return HttpResponse()


def highlight(text, term, class_name='text-red-500'):
    """辅助函数，用于突出显示文本中的关键词"""
    escaped_term = escape(term)

    # 使用Beautiful Soup解析文本
    soup = BeautifulSoup(text, 'html.parser')

    def replacer(match):
        """这个内部函数将被 re.sub() 使用，以动态的方式替换匹配项"""
        return f'<span class="{class_name}">{match.group(0)}</span>'

    # 使用正则表达式创建匹配模式
    pattern = re.compile(re.escape(escaped_term), re.IGNORECASE)

    # 遍历soup中的所有文本节点，并替换找到的匹配项
    for text_node in soup.find_all(text=True):
        if isinstance(text_node, NavigableString) and not text_node.parent.name == 'span':
            replaced_text = pattern.sub(replacer, text_node)
            text_node.replace_with(BeautifulSoup(replaced_text, 'html.parser'))

    # 将修改后的soup转换回字符串
    return mark_safe(str(soup))


def search_all(request):
    q = request.GET.get('q', '').strip()
    # print(f"Value of q: '{q}'")  # 打印q的值，用于调试

    if not q or q.isspace():  # 主要是检查q是否为None，因为在这种情况下，q.split()将引发AttributeError。
        # results = Product.objects.none()y
        # return render(request,'search/partial/search-results.html',{})
        # print("执行了if not q")
        return HttpResponse()

    # print('执行了if 后面的分支')
    q_list = [term for term in q.split() if term]  # 过滤q_list中的空字符串
    # 或者
    # q_list = filter(None, q.split())  # 这也可以过滤掉空字符串
    query_product = Q()
    query_blog = Q()
    for term in q_list:
        if term:
            query_product &= (Q(name__icontains=term) | Q(
                slug__icontains=term) | Q(description__icontains=term))
            query_blog &= (Q(title__icontains=term) | Q(
                slug__icontains=term) | Q(description__icontains=term))

    results_product = Product.objects.filter(query_product)
    results_blog = Blog.objects.filter(query_blog)

    # 初始化高亮结果列表
    highlighted_results_product = []
    highlighted_results_blog = []

    # 高亮处理
    for product in results_product:
        highlighted_name = product.name
        highlighted_description = product.description
        for term in q_list:
            highlighted_name = highlight(highlighted_name, term)
            highlighted_description = highlight(highlighted_description, term)
        highlighted_results_product.append({
            'category': product.category,
            'name': highlighted_name,
            'description': highlighted_description
        })

    for blog in results_blog:
        highlighted_title = blog.title
        highlighted_description = blog.description
        for term in q_list:
            highlighted_title = highlight(highlighted_title, term)
            highlighted_description = highlight(highlighted_description, term)
        highlighted_results_blog.append({
            'category': blog.category,
            'title': highlighted_title,
            'description': highlighted_description
        })

    return render(request, 'search/partial/search-results.html', {
        'results_product': highlighted_results_product,
        'results_blog': highlighted_results_blog,
    })
