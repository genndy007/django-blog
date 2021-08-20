from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
import sys

from .models import Post
# Create your tests here.

extitle = 'title'
exbody = 'body'
extitle2 = 'new title'
exbody2 = 'new body'
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
        res = self.client.get(f'{post_url}/1', follow=True)
        nores = self.client.get(f'{post_url}/{bad_index}', follow=True)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(nores.status_code, 404)
        self.assertContains(res, extitle)
        self.assertTemplateUsed(res, 'post_detail.html')

    def test_get_absolute_url(self):
        self.assertEqual(self.post.get_absolute_url(), f'{post_url}/1/')

    def test_post_create_view(self):
        res = self.client.post(reverse('post_new'), {
            'title': extitle2,
            'body': exbody2,
            'author': self.user.pk,
        }, follow=True)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(Post.objects.last().title, extitle2)
        self.assertEqual(Post.objects.last().body, exbody2)

    def test_post_update_view(self):
        res = self.client.post(reverse('post_edit', args='1'), {
            'title': 'Updated title',
            'body': 'Updated text',
        }, follow=True)
        self.assertEqual(res.status_code, 200)

    def test_post_delete_view(self):
        res = self.client.post(reverse('post_delete', args='1'), follow=True)
        self.assertEqual(res.status_code, 200)









