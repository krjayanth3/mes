from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class PublicSiteTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.admin = get_user_model().objects.create_superuser(
            username='test-admin',
            email='admin@example.com',
            password='safe-test-password',
        )

    def get(self, path):
        return self.client.get(path, secure=True, HTTP_HOST='localhost')

    def test_public_pages_are_available(self):
        for path in ('/', '/about/', '/departments/', '/faculty/', '/notices/', '/gallery/', '/contact/', '/login/'):
            with self.subTest(path=path):
                self.assertEqual(self.get(path).status_code, 200)

    def test_staff_dashboard_requires_login(self):
        response = self.get('/staff-dashboard/')
        self.assertEqual(response.status_code, 302)
        self.assertIn(reverse('login'), response.url)

    def test_staff_dashboard_is_available_to_staff(self):
        self.client.force_login(self.admin)
        response = self.get('/staff-dashboard/')
        self.assertEqual(response.status_code, 200)
