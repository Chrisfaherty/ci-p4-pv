from django.test import TestCase
from .models import Password


class TestModels(TestCase):

    def test_done_defaults_to_false(self):
        passwords = Password.objects.create(name='Test Passwords')
        self.assertFalse(password.done)

    
    def test_password_string_method_returns_name(self):
        passwords = Password.objects.create(name='Test Password Manager')
        self.assertEqual(str(item), 'Test Password manager')