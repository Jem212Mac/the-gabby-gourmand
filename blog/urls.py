from . import views
from django.urls import path

urlpatterns = [
    path('', views.ReviewList.as_view(), name='home'),
    path('', views.FoodList.as_view(), name='food'),
    path('', views.CocktailList.as_view(), name='cocktail'),
]