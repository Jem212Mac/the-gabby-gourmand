from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))
RATING = (
    (5, "Excellent - 5 Stars"), (4, "Good - 4 Stars"), (3, "Ok - 3 Stars"),
    (2, "Could Be Better - 2 Stars"),
    (1, "Poor - 1 Star"), (0, "Really Bad - 0 Stars"))
PRICE = ((0, "Low"), (1, "Medium"), (2, "High"))
TYPE = ((0, "Food"), (1, "Cocktail"))


class Review(models.Model):
    """
    Stores a single restaurant review related to :model:`auth.User`.
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_reviews"
    )
    featured_image_1 = CloudinaryField('image', default='placeholder')
    featured_image_2 = CloudinaryField('image', default='placeholder')
    featured_image_3 = CloudinaryField('image', default='placeholder')
    restaurant = models.CharField(max_length=200)
    content = models.TextField()
    location = models.CharField(max_length=200)
    visited_on = models.DateTimeField()
    rating = models.IntegerField(choices=RATING, default=5)
    price = models.IntegerField(choices=PRICE, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | written by {self.author}"


class Recipe(models.Model):
    """
    Stores a single recipe related to :model:`auth.User`.
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_recipes"
    )
    featured_image_1 = CloudinaryField('image', default='placeholder')
    featured_image_2 = CloudinaryField('image', default='placeholder')
    featured_image_3 = CloudinaryField('image', default='placeholder')
    ingredients = models.TextField()
    instructions = models.TextField()
    type = models.IntegerField(choices=TYPE, default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} | written by {self.author}"


class Comment(models.Model):
    """
    Stores a single comment related to :model:`auth.User`
    and :model:`blog.recipe`.
    """
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"{self.body} by {self.author}"
