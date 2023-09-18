from django.urls import path
from . import views


urlpatterns = [
    path('category/<path:category_path>/',views.category_products,name='category-products'),
    path('',views.products_list,name='product-list'),
]
