from django.contrib import admin
from .models import Review, Recipe, Comment

admin.site.register(Review)
admin.site.register(Recipe)
admin.site.register(Comment)