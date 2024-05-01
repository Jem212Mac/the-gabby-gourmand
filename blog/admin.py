from django.contrib import admin
from .models import Review, Recipe, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Review)
class ReviewAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'author', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'author', 'created_on',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'type', 'author', 'status', 'created_on')
    search_fields = ['title', 'ingredients', 'instructions']
    list_filter = ('status', 'author', 'type', 'created_on',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('ingredients', 'instructions')

admin.site.register(Comment)