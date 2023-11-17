from django.urls import path
from . import views


urlpatterns = [
    # path('category/<path:category_path>/',views.category_products,name='category-products'),
    path('category/<path:category_path>/',views.CategoryProductListView.as_view(),name='category-products'),
    path('detail/<path:category_path>/<slug:slug>/',views.ProductDetail.as_view(),name='product-detail'),
    path('',views.products_index,name='product-index'),
    # path('detail/', views.detail_redirect, name='detail-redirect'),
    # path('category/', views.category_listing, name='category-redirect'),
]
