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
        'root_nodes_data':root_nodes_data,
    })



def category_products(request, category_path):
    slugs = category_path.split('/')
    category_slug = slugs.pop()
    category = get_object_or_404(Category, slug=category_slug)

    # 使用 Q 对象来构建查询，包括类别及其所有子类别的产品
    products = Product.objects.active().filter(
        Q(category=category) | Q(
            category__in=category.get_descendants(include_self=True))
    )

    return render(request, 'products/product-list.html', { 'products': products})
