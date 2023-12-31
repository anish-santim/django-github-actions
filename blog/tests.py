from django.test import TestCase
from .models import Post


class ModelTest(TestCase):

    def setUp(self):
        self.blog = Post.objects.create(title='django', slug='django')

    def test_post_model(self):
        d = self.blog
        self.assertTrue(isinstance(d, Post))
        self.assertEqual(str(d), 'django')
