from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Review, Recipe, Comment
from .forms import CommentForm


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
    comments = recipe.comments.all().order_by("-created_on")
    comment_count = recipe.comments.filter(approved=True).count()
    
    if request.method == "POST":
        print('request.POST', request.POST)
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.recipe = recipe
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
    )

    comment_form = CommentForm()

    return render(
        request,
        "blog/food_detail.html",
        {"recipe": recipe,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,},
    )

def cocktail_detail(request, slug):
    queryset = Recipe.objects.filter(status=1, type=1)
    recipe = get_object_or_404(queryset, slug=slug)
    comments = recipe.comments.all().order_by("-created_on")
    comment_count = recipe.comments.filter(approved=True).count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.recipe = recipe
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
    )

    comment_form = CommentForm()

    return render(
        request,
        "blog/cocktail_detail.html",
        {"recipe": recipe,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,},
    )