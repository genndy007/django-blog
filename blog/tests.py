from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
import sys

from .models import Post
# Create your tests here.

extitle = 'title'
exbody = 'body'
exusername = 'test'

post_url = '/post'
bad_index = sys.maxsize


class BlogTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            username=exusername,
            email='test@test.com',
            password='secret'
        )

        self.post = Post.objects.create(
            title=extitle,
            body=exbody,
            author=self.user
        )

    def test_string_repr(self):
        post = Post(title=extitle)
        self.assertEqual(str(post), post.title)

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', extitle)
        self.assertEqual(f'{self.post.author}', exusername)
        self.assertEqual(f'{self.post.body}', exbody)

    def test_post_list_view(self):
        res = self.client.get(reverse('home'))
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, exbody)
        self.assertTemplateUsed(res, 'home.html')

    def test_post_detail_view(self):
        res = self.client.get(f'/post/1')
        nores = self.client.get(f'{post_url}/{bad_index}')

        self.assertEqual(res.status_code, 301)
        self.assertEqual(nores.status_code, 404)
        self.assertContains(res, extitle)
        self.assertTemplateUsed(res, 'post_detail.html')













