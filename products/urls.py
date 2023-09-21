from django.urls import path
from . import views


urlpatterns = [
    # path('category/<path:category_path>/',views.category_products,name='category-products'),
    path('category/<path:category_path>/',views.CategoryProductListView.as_view(),name='category-products'),
    path('detail/<slug:slug>/',views.ProductDetail.as_view(),name='product-detail'),
    path('',views.products_index,name='product-index'),
]

htmx_urlpatterns = [
    # path('get_list_main/',views)
]

urlpatterns += htmx_urlpatterns