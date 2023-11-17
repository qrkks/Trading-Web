from django.urls import path
from . import views


urlpatterns = [
    path('products/',views.ProductSearchView.as_view(),name='search-product'),
    path('clear_search_results',views.clear_results,name='clear-search-results'),
    path('search_all',views.search_all,name='search-all')
]
