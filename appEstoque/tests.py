import json

from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import AccessToken
from .models import Post

class PostAPITestCase(TestCase):
    def setUp(self):
       self.user = User.objects.create_user(username = 'testuser', password = 'testpassword')
       self.access_token = AccessToken.for_user(self.user)
       self.authorization_header = f'Bearer {self.access_token}'

    def test_create_post (self):
        response = self.client.post('/api/posts/', {'title': 'Novo Post', 'content': 'Conteúdo do novo post'}, HTTP_AUTHORIZATION = self.authorization_header)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Post.objects.count(), 1)

        post = Post.objects.first()
        self.assertEqual(post.title, 'Novo Post')
        self.assertEqual(post.content, 'Conteúdo do novo post')

    def test_create_post_unauthenticated (self):
        response = self.client.post('/api/posts/', {'title': 'Novo Post', 'content': 'Conteúdo do novo post'}, HTTP_AUTHORIZATION = '')
        self.assertEqual(response.status_code, 401)
        
    def test_retrieve_post (self):
        post = Post.objects.create(title = 'Teste', content = 'Conteúdo do teste')
        response = self.client.get(f'/api/posts/{post.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id'], post.id)
        self.assertEqual(response.data['title'], post.title)
        self.assertEqual(response.data['content'], post.content)

    def test_update_post(self):
        post = Post.objects.create(title = 'Teste', content = 'Conteúdo do teste')
        updated_data = {'title': 'Post Atualizado', 'content': 'Conteúdo atualizado'}
        response = self.client.put(f'/api/posts/{post.id}/', json.dumps(updated_data), content_type = 'application/json', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        post.refresh_from_db()
        self.assertEqual(post.title, updated_data['title'])
        self.assertEqual(post.content, updated_data['content'])
    
    def test_delete_post(self):
        post = Post.objects.create(title = 'Teste', content = 'Conteúdo do teste')
        response = self.client.delete(f'/api/posts/{post.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Post.objects.count(), 0)