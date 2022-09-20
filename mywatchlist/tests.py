from django.test import TestCase, Client
from django.urls import resolve
# Create your tests here.

class AppTest(TestCase):
    def test_contoh_app_url_exists(self):
        response = Client().get('/contohapp/')
        self.assertEqual(response.status_code,200)
    
