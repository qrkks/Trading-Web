from django.urls import path
from . import views

urlpatterns = [
    # path('',views.blog_index,name='blog-index'),
    path('',views.BlogIndex.as_view(),name='blog-index'),
    path('category/<path:path>/',views.BlogList.as_view(),name='blog-list'),
    path('<slug:slug>/',views.BlogDetail.as_view(),name='blog-detail'),
]
