from django.urls import path
from . import views


urlpatterns = [
    path('products/',views.ProductSearchView.as_view(),name='search'),
    path('search/search_results_reset',views.clear_results,name='clear-search-results'),
]
