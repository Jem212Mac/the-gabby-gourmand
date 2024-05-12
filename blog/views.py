from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Review, Recipe, Comment
from .forms import CommentForm


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
            "comment_form": comment_form, },
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
            "comment_form": comment_form, },
    )


def food_comment_edit(request, slug, comment_id):
    """
    view to edit comments on food recipes
    """
    if request.method == "POST":

        queryset = Recipe.objects.filter(status=1, type=0)
        recipe = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.recipe = recipe
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(
                request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('food_detail', args=[slug]))


def cocktail_comment_edit(request, slug, comment_id):
    """
    view to edit comments on cocktail recipes
    """
    if request.method == "POST":

        queryset = Recipe.objects.filter(status=1, type=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.recipe = recipe
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(
                request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('cocktail_detail', args=[slug]))


def food_comment_delete(request, slug, comment_id):
    """
    view to delete comments on food recipes
    """
    queryset = Recipe.objects.filter(status=1, type=0)
    recipe = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(
            request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('food_detail', args=[slug]))


def cocktail_comment_delete(request, slug, comment_id):
    """
    view to delete comments on cocktail recipes
    """
    queryset = Recipe.objects.filter(status=1, type=1)
    recipe = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(
            request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('cocktail_detail', args=[slug]))
