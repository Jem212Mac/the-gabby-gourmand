from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Review, Recipe, Comment


# Create your views here.
class ReviewList(generic.ListView):
    queryset = Review.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6

class FoodList(generic.ListView):
    queryset = Recipe.objects.filter(status=1, type=0)
    template_name = "blog/food.html"
    paginate_by = 6

class CocktailList(generic.ListView):
    queryset = Recipe.objects.filter(status=1, type=1)
    template_name = "blog/cocktail.html"
    paginate_by = 6

def review_detail(request, slug):
    queryset = Review.objects.filter(status=1)
    review = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "blog/review_detail.html",
        {"review": review},
    )

def food_detail(request, slug):
    queryset = Recipe.objects.filter(status=1, type=0)
    recipe = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "blog/food_detail.html",
        {"recipe": recipe},
    )

def cocktail_detail(request, slug):
    queryset = Recipe.objects.filter(status=1, type=1)
    recipe = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "blog/cocktail_detail.html",
        {"recipe": recipe},
    )