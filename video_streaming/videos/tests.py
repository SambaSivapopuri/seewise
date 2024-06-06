from django.test import TestCase
from django.contrib.auth.models import User
from .models import Video
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token

class VideoTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test', password='testpass')
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_video_create(self):
        response = self.client.post('/api/videos/', {'name': 'Test Video', 'url': 'http://example.com/video.mp4'})
        self.assertEqual(response.status_code, 201)

    def test_video_list(self):
        Video.objects.create(user=self.user, name='Test Video', url='http://example.com/video.mp4')
        response = self.client.get('/api/videos/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
