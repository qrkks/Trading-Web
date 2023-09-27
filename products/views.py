from typing import Any
from django.views.generic import ListView, DetailView
from django.db.models import Q
from django.shortcuts import get_object_or_404, render
from .models import Category, Product
# Create your views here.


def products_index(request):
    # 获取根节点列表
    root_nodes = Category.objects.filter(parent=None)

    root_nodes_data = {}

    for root_node in root_nodes:
        products = Product.objects.active().filter(
            Q(category__in=root_node.get_descendants(include_self=True))
        )
        root_nodes_data[root_node] = products

    context_data = {
        'root_nodes_data': root_nodes_data,
        'partial_template_path':'products/partial/main-index.html',
    }

    products = Product.objects.active().all()

    return render(request, 'products/product.html', context_data )



class CategoryProductListView(ListView):
    template_name = 'products/product.html'  # 指定模板文件路径
    context_object_name = 'products'  # 指定模板上下文变量的名称
    paginate_by = 2
    extra_context = {
        'partial_template_path':"products/partial/main-list.html",
        'main_title':'products list',
    }

    def get_queryset(self):
        # 获取 category_path 参数并拆分为 slugs 列表
        category_path = self.kwargs['category_path']

        if category_path == 'all-products':
            products = Product.objects.active().all()
        else:
            slugs = category_path.split('/')
            category_slug = slugs.pop()
            # 获取 Category 对象    
            category = get_object_or_404(Category, slug=category_slug)

            # 使用 Q 对象来构建查询，包括类别及其所有子类别的产品
            products = Product.objects.active().filter(
                Q(category__in=category.get_descendants(include_self=True))
            )

        return products
    
    def render_to_response(self, context, **response_kwargs):
        if self.request.headers.get('HX-Request') == 'true':
            # 处理HTMX请求，只返回列表部分的HTML内容
            return render(self.request, 'products/partial/main-list.html', context)
        else:
            # 处理常规请求，返回整个页面的HTML
            return super().render_to_response(context, **response_kwargs)



class ProductDetail(DetailView):
    template_name = 'products/product-detail.html'
    model = Product
    context_object_name = 'product'
    # slug_field = 'slug'
    extra_context = {
        'partial_template_path':"products/partial/main-detail.html"
    }

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        # 获取产品对象
        product = context['object']

        # 获取所有属性名
        attribute_names = [field.name for field in Product._meta.get_fields()]

        # 筛选满足条件的属性名，不以"page"，'is'开头
        filtered_attribute_names = [attr for attr in attribute_names if not (attr.startswith("page") or attr.startswith('is') or attr  in ['images','custom_order'] )]


        # 创建一个字典，包含属性名和对应的值，将下划线替换为空格
        product_data = {attr.replace("_", " "): getattr(product, attr) for attr in filtered_attribute_names}

        # 将 product_data 添加到上下文
        context['product_data'] = product_data
        return context
    
    def render_to_response(self, context, **response_kwargs):
        if self.request.headers.get('HX-Request') == 'true':
            # 处理HTMX请求，只返回列表部分的HTML内容
            return render(self.request, 'products/partial/main-detail.html', context)
        else:
            # 处理常规请求，返回整个页面的HTML
            return super().render_to_response(context, **response_kwargs)

    