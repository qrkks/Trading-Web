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

    return render(request, 'products/product-index.html', {
        'root_nodes_data': root_nodes_data,
    })


# def category_products(request, category_path):
#     slugs = category_path.split('/')
#     category_slug = slugs.pop()
#     category = get_object_or_404(Category, slug=category_slug)

#     # 使用 Q 对象来构建查询，包括类别及其所有子类别的产品
#     products = Product.objects.active().filter(
#         Q(category=category) | Q(
#             category__in=category.get_descendants(include_self=True))
#     )

#     return render(request, 'products/product-list.html', { 'products': products})

# CBV


class CategoryProductListView(ListView):
    template_name = 'products/product-list.html'  # 指定模板文件路径
    context_object_name = 'products'  # 指定模板上下文变量的名称
    paginate_by = 12

    def get_queryset(self):
        # 获取 category_path 参数并拆分为 slugs 列表
        category_path = self.kwargs['category_path']
        slugs = category_path.split('/')
        category_slug = slugs.pop()

        # 获取 Category 对象
        category = get_object_or_404(Category, slug=category_slug)

        # 使用 Q 对象来构建查询，包括类别及其所有子类别的产品
        products = Product.objects.active().filter(
             Q(category__in=category.get_descendants(include_self=True))
        )

        return products



class ProductDetail(DetailView):
    template_name = 'products/product-detail.html'
    model = Product
    context_object_name = 'product'
    slug_field = 'slug'

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        # 获取产品对象
        product = context['product']

        # 获取所有属性名
        attribute_names = [field.name for field in Product._meta.get_fields()]

        # 排除属性
        # attribute_names = {key: value for key, value in attribute_names if key.startswith("page")}


        # 创建一个字典，包含属性名和对应的值，将下划线替换为空格
        product_data = {attr.replace("_", " "): getattr(product, attr) for attr in attribute_names}

        # 将 product_data 添加到上下文
        context['product_data'] = product_data
        return context