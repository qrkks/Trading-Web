from django.urls import path
from .views import inquiry_create

urlpatterns = [
    path('inquiry_create/', inquiry_create, name='inquiry_create'),
]
