import json
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model

from apps.users.models import User

# Create your tests here.

class TestSetup(APITestCase):

    def setUp(self):
        self.register_url = '/auth/users/'
        self.partial_update_url = '/api/v1/user/'
        return super().setUp()
    
    def tearDown(self):
        return super().tearDown()
    

class TestViews(TestSetup):

    def test_register(self):
        response = self.client.post(
            self.register_url,
            data=json.dumps({
                'email': 'testuser@example.com',
                'password': 'secretpassword',
                're_password': 'secretpassword'
            }),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 201)

        user_modal = get_user_model()
        user = user_modal.objects.get(email='testuser@example.com')
        self.assertEqual(user.email, 'testuser@example.com') # type: ignore


    def test_update_user(self):
        user = self.create_and_login_user()
        response = self.client.put(
            f'{self.partial_update_url}{user.id}/',
            data=json.dumps({
               "full_name": "User 123",
                "email": "user@example.com",
                "gender": "Male",
                "phone_number": "9856237896",
                "is_staff": False
            }),
            content_type='application/json'
        )
        self._verify_the_data(response, user)


    def test_update_partial_user(self):
        user = self.create_and_login_user()
        response = self.client.patch(
            f'{self.partial_update_url}{user.id}/',
            data=json.dumps({
                'phone_number': '9856237896',
            }),
            content_type='application/json'
        )
        self._verify_the_data(response, user)

    # TODO Rename this here and in `test_update_user` and `test_update_partial_user`
    def _verify_the_data(self, response, user):
        self.assertEqual(response.status_code, 200)
        updated_user = User.objects.get(id=user.id)
        self.assertEqual(updated_user.phone_number, '9856237896')


    def create_and_login_user(self):
        user_modal = get_user_model()
        result = user_modal.objects.create_user(
            email='testuser@example.com', password='secretpassword'
        )
        self.client.login(email='testuser@example.com', password='secretpassword')
        return result