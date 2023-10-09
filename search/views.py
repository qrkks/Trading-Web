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
        'partial_template_path':'products/partial/main-list.html',
    }
    
    def get_queryset(self):
        q = self.request.GET.get('q', '').strip()
        if q == '':
            self.extra_context['main_title'] = 'search'
            results = Product.objects.none()
            return results
        else:
            query = Q()
            for term in q.split():
                query &= (
                    Q(name__icontains=term) | Q(slug__icontains=term) | Q(description__icontains=term)
                    )
            results = Product.objects.active().filter(query)

            self.extra_context['main_title'] = f'{results.count()} results found for "{q}"'
            return results


    def render_to_response(self, context, **response_kwargs):
        if self.request.headers.get('HX-Request') == 'true':
            return render(self.request, 'products/partial/main-list.html', context)

        return super().render_to_response(context, **response_kwargs)
    
def clear_results(request):
    return HttpResponse ()

def search_all(request):
    q = request.GET.get('q')
    q_list = q.split()
    query_product = Q()
    query_blog = Q()
    for term in q_list:
        query_product &= Q(name__icontains=term)|Q(slug__icontains=term)|Q(description__icontains=term)
        query_blog &= Q(title__icontains=term)|Q(slug__icontains=term)|Q(description__icontains=term)
    results_product = Product.objects.filter(query_product)
    results_blog = Blog.objects.filter(query_blog)
    return render(request,'search/partial/search-results.html',{
        'results_product':results_product,
        'results_blog':results_blog,
    })