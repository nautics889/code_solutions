import json
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIRequestFactory, APIClient

from users.models import User
from rest_framework_simplejwt import views as jwt_views


#fixtures must be moved outside of this file further
USER = {
	"username": "foobar",
	"email": "foobar@example.com",
	"password": "newpassword",
	"first_name": "fn",
	"last_name": "ln"
}


class BasicTestCase(TestCase):
    factory = APIRequestFactory()

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(**USER)


class CurrentUserRetrieveUpdateTestCase(BasicTestCase):
    def setUp(self):
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_retrieve_info_about_logged_user(self):
        response = self.client.get('/users/details/', format='json')
        self.assertEqual(response.data.get('username'), 'foobar')
        self.client.logout()

    def test_update_field_of_logged_user(self):
        self.client.patch('/users/details/', {'username': 'FOOBAR'}, format='json')
        self.assertTrue(User.objects.get(id=self.user.id).username.isupper())
        self.client.logout()
