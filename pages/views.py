from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model
from django.views.generic.list import ListView

from .models import Recipe

# Create your views here.
def index(request):
    return render(request,'pages/index.html')

def search(request):
    search_text = request.GET.get('q')
    print(search_text)
    if search_text:
        results = Recipe.objects.filter(title__icontains = search_text)
        context = {
            'results':results
        }
        print(context)
        return render(request,'pages/partial/search-results.html',context)
    return render(request,'pages/partial/search-results.html',{'results':None})
    


class RecipeList(ListView):
    template_name = 'pages/index.html'
    model = Recipe
    context_object_name = 'recipes'

    def get_queryset(self) -> QuerySet[Any]:
        return Recipe.objects.all()

def add_recipe(request):
    title = request.POST.get('title')
    Recipe.objects.create(title=title)

    # 返回所有recipes
    recipes = Recipe.objects.all()
    return render(request,'pages/partial/recipe-list.html',{'recipes':recipes})

# def search_page(request):
#     return render(request,'pages/search-page.html')

