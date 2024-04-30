from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))
RATING = ((5, "Excellent - 5 Stars"), (4, "Good - 4 Stars"), (3, "Ok - 3 Stars"), (2, "Could Be Better - 2 Stars"), (1, "Poor - 1 Star"), (0, "Really Bad - 0 Stars"))
PRICE = ((0, "Low"), (1, "Medium"), (2, "High"))
TYPE = ((0, "Food"), (1, "Cocktail"))

class Review(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_reviews"
    )
    restaurant = models.CharField(max_length=200)
    content = models.TextField()
    location = models.CharField(max_length=200)
    visited_on = models.DateTimeField()
    rating = models.IntegerField(choices=RATING, default=5)
    price = models.IntegerField(choices=PRICE, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    updated_on = models.DateTimeField(auto_now=True)


class Recipe(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_recipes"
    )
    ingredients = models.TextField()
    instructions = models.TextField()
    type = models.IntegerField(choices=TYPE, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    updated_on = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)