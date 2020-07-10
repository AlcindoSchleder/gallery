# _*_ coding: utf-8 _*_
from django.test import TestCase
from django.contrib.auth.models import User


class TestShowIndexPageView(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.credentials = {
            'username': 'magron',
            'password': 'test_pwd@magron'
        }
        User.objects.create_user(**cls.credentials)

    def setUp(self) -> None:
        logout = self.client.logout()

    def test_home_get_index(self):
        # Test main page
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200, 'Get index.page!')

    def test_home_get_login_index(self):
        # Test login page
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200, 'Get index.page!')

    def test_register_auth_login(self):
        # Test login page auth
        response = self.client.post('/login/', self.credentials, follow=True)
        self.assertEqual(str(response.context['user']), self.credentials['username'])
        self.assertTrue(response.context['user'].is_authenticated)

    def test_show_category_form(self):
        response = self.client.get('category_detail/0')
        self.assertEqual(response.status_code, 200, 'Show Category Form!')
