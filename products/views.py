from django.db.models import Q
from django.shortcuts import get_object_or_404, render
from .models import Category, Product
# Create your views here.


def products_list(request):
    return render(request, 'products/product-list.html')

# views.py

# def category_products(request, *category_slugs):
#     slugs = list(category_slugs)
#     category_slug = slugs.pop()
#     category = get_object_or_404(Category, slug=category_slug)

#     while slugs:
#         subcategory_slug = slugs.pop(0)
#         category = category.children.get(slug=subcategory_slug)

#     products = category.product_set.all()

#     return render(request, 'products-list.html', {'category': category, 'products': products})


def category_products(request, category_path):
    slugs = category_path.split('/')
    category_slug = slugs.pop()
    category = get_object_or_404(Category, slug=category_slug)

    # 使用 Q 对象来构建查询，包括类别及其所有子类别的产品
    products = Product.objects.filter(
        Q(category=category) | Q(
            category__in=category.get_descendants(include_self=True))
    )

    return render(request, 'products/product-list.html', { 'products': products})
