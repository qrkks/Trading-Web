from django.urls import path
from . import views


urlpatterns = [
    path('',views.index),
]

htmx_urlpatterns = [
    # path('to-search/',views.search,name='search'),
    # path('recipes/',views.RecipeList.as_view(),name='recipe-list'),
    # path('add-recipe',views.add_recipe,name='add-recipe'),
]

urlpatterns += htmx_urlpatterns
