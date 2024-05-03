from . import views
from django.urls import path

urlpatterns = [
    path('', views.ReviewList.as_view(), name='home'),
    path('food_recipes', views.FoodList.as_view(), name='food'),
    path('cocktail_recipes', views.CocktailList.as_view(), name='cocktail'),
]