from django.urls import path
from . import views

urlpatterns = [
    # path('',views.blog_index,name='blog-index'),
    path('',views.BlogIndex.as_view(),name='blog-index'),
    path('category/<path:category_path>/',views.BlogList.as_view(),name='blog-list'),
    path('detail/<path:category_path>/<slug:slug>/',views.BlogDetail.as_view(),name='blog-detail'),
]
