from django.urls import path
from . import views

urlpatterns = [
    path('',views.BlogList.as_view(),name='blog-list'),
    path('<slug:slug>/',views.BlogDetail.as_view(),name='blog-detail'),
]
