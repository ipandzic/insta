from django.test import TestCase
from django.urls import reverse

from django.contrib.auth import get_user_model

# Create your tests here.

from .models import Post

User = get_user_model()


class PostModelTestCase(TestCase):
    def setUp(self):
        some_random_user = User.objects.create(username='ivan')

        Post.objects.create(
            user=User.objects.first(),
            content='Some random content'
        )

    def test_tweet_item(self):
        obj = Post.objects.create(
            user=User.objects.first(),
            content='Some random content'
        )
        self.assertTrue(obj.content == "Some random content")

    