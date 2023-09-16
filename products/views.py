from django.shortcuts import render
from .models import Category
# Create your views here.
def products_list(request):



    return render(request,'products/product-list.html')
