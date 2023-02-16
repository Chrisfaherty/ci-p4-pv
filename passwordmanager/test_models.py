from django.test import TestCase
from .models import Password


class TestModels(TestCase):

    def test_done_defaults_to_false(self):
        passwords = Password.objects.create(name='Test Passwords')
        self.assertFalse(password.done)