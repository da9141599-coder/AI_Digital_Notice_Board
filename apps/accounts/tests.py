from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile

class ProfileSignalTest(TestCase):
    def test_profile_created_on_user_create(self):
        user = User.objects.create_user(username='testuser', password='pwd12345')
        self.assertTrue(hasattr(user, 'profile'))
        self.assertIsInstance(user.profile, Profile)
