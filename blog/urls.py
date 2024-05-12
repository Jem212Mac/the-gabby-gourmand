from django.urls import path
from . import views

urlpatterns = [
    path('', views.ReviewList.as_view(), name='home'),
    path('food_recipes', views.FoodList.as_view(), name='food'),
    path('cocktail_recipes', views.CocktailList.as_view(), name='cocktail'),
    path('<slug:slug>/', views.review_detail, name='review_detail'),
    path('food_recipes/<slug:slug>/', views.food_detail, name='food_detail'),
    path(
        'cocktail_recipes/<slug:slug>/',
        views.cocktail_detail, name='cocktail_detail'),
    path(
        'food_recipes/<slug:slug>/edit_comment/<int:comment_id>',
        views.food_comment_edit, name='food_comment_edit'),
    path(
        'cocktail_recipes/<slug:slug>/edit_comment/<int:comment_id>',
        views.cocktail_comment_edit, name='cocktail_comment_edit'),
    path(
        'food_recipes/<slug:slug>/delete_comment/<int:comment_id>',
        views.food_comment_delete, name='food_comment_delete'),
    path(
        'cocktail_recipes/<slug:slug>/delete_comment/<int:comment_id>',
        views.cocktail_comment_delete, name='cocktail_comment_delete'),
]
