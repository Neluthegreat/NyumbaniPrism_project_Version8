from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserProfile

class UserProfileTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
    
    def test_user_profile_creation(self):
        profile = UserProfile.objects.create(
            user=self.user,
            role='staff',
            department='IT'
        )
        self.assertEqual(str(profile), 'testuser - staff')
