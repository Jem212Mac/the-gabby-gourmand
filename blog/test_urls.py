"""Tests for the blog app's urls."""
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from blog.views import (
    ReviewList,
    FoodList,
    CocktailList
    )


class TestUrls(SimpleTestCase):
    """Test the urls for the blog app."""

    def test_home_url_resolves(self):
        url = reverse('home')
        self.assertEqual(resolve(url).func.view_class, ReviewList)

    def test_home_url_resolves(self):
        url = reverse('food')
        self.assertEqual(resolve(url).func.view_class, FoodList)

    def test_home_url_resolves(self):
        url = reverse('cocktail')
        self.assertEqual(resolve(url).func.view_class, CocktailList)
