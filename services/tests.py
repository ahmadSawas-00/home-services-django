from django.test import TestCase
from django.urls import reverse

class ViewsTest(TestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_services_ui_status_code(self):
        response = self.client.get(reverse('services-ui'))
        self.assertEqual(response.status_code, 200)