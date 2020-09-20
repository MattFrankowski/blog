from django.test import TestCase
from django.contrib.auth import authenticate, get_user_model
from django.conf import settings
import os
from datetime import datetime

from .models import Blogger

class SigninTestCase(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='test', password='12test12', email='test@example.com')
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_correct(self):
        user = authenticate(username='test', password='12test12')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_wrong_username(self):
        user = authenticate(username='wrong', password='12test12')
        self.assertFalse(user is not None and user.is_authenticated)

    def test_wrong_pssword(self):
        user = authenticate(username='test', password='wrong')
        self.assertFalse(user is not None and user.is_authenticated)


class BloggerTestCase(TestCase):

    def setUp(self):
        self.blogger = Blogger.objects.create(user=get_user_model().objects.create_user(username='test', password='12test12', email='test@example.com'),
                                              name="John Doe",
                                              bio="Test Bio",
                                              email="test@example.com",
                                              photo=os.path.join(settings.BASE_DIR, "static/profile_pics/unnamed.png"),
                                              date_created=datetime.now()
                                              )

    def test_user(self):
        user = authenticate(username=self.blogger.user.username, password=self.blogger.user.password)
        self.assertFalse(user is not None and user.is_authenticated)

    def test_name(self):
        self.assertTrue(self.blogger.name == "John Doe")

    def test_bio(self):
        self.assertTrue(self.blogger.bio == "Test Bio")

    def test_email(self):
        self.assertTrue(self.blogger.email == "test@example.com")

    def test_photo(self):
        photo = self.blogger.photo
        self.assertTrue(photo is not None)

    def test_date(self):
        date_created = self.blogger.date_created
        self.assertTrue(isinstance(date_created, datetime))

    
