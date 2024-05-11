from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .forms import CommentForm
from .models import Recipe

class TestFoodDetailViews(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )
        self.recipe = Recipe(title="Blog title", author=self.user, 
            slug="blog-title", ingredients="Blog ingredients", instructions="Blog instructions", type = "0", status=1)
        self.recipe.save()

    def test_render_food_detail_page_with_comment_form(self):
        response = self.client.get(reverse(
            'food_detail', args=['blog-title']))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Blog title", response.content)
        self.assertIn(b"Blog ingredients", response.content)
        self.assertIn(b"Blog instructions", response.content)
        self.assertIsInstance(
            response.context['comment_form'], CommentForm)

    def test_successful_comment_submission(self):
        """Test for posting a comment on a post"""
        self.client.login(
            username="myUsername", password="myPassword")
        post_data = {
            'body': 'This is a test comment.'
        }
        response = self.client.post(reverse(
            'food_detail', args=['blog-title']), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Comment submitted and awaiting approval',
            response.content
        )

class TestCocktailDetailViews(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="myUsername",
            password="myPassword",
            email="test@test.com"
        )
        self.recipe = Recipe(title="Blog title", author=self.user, 
            slug="blog-title", ingredients="Blog ingredients", instructions="Blog instructions", type = "1", status=1)
        self.recipe.save()

    def test_render_cocktail_detail_page_with_comment_form(self):
        response = self.client.get(reverse(
            'cocktail_detail', args=['blog-title']))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Blog title", response.content)
        self.assertIn(b"Blog ingredients", response.content)
        self.assertIn(b"Blog instructions", response.content)
        self.assertIsInstance(
            response.context['comment_form'], CommentForm)

    def test_successful_comment_submission(self):
        """Test for posting a comment on a post"""
        self.client.login(
            username="myUsername", password="myPassword")
        post_data = {
            'body': 'This is a test comment.'
        }
        response = self.client.post(reverse(
            'cocktail_detail', args=['blog-title']), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Comment submitted and awaiting approval',
            response.content
        )