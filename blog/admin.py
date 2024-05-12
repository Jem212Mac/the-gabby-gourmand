from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Review, Recipe, Comment


@admin.register(Review)
class ReviewAdmin(SummernoteModelAdmin):
    """
    Lists fields for display in admin, fields for search,
    field filters, fields to prepopulate and rich-text editor.
    """
    list_display = ('title', 'slug', 'author', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'author', 'created_on',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    """
    Lists fields for display in admin, fields for search,
    field filters, fields to prepopulate and rich-text editor.
    """
    list_display = ('title', 'slug', 'type', 'author', 'status', 'created_on')
    search_fields = ['title', 'ingredients', 'instructions']
    list_filter = ('status', 'author', 'type', 'created_on',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('ingredients', 'instructions')


admin.site.register(Comment)
