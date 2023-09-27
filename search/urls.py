from django.urls import path
from . import views


urlpatterns = [
    path('products/',views.ProductSearchView.as_view(),name='search'),
]
