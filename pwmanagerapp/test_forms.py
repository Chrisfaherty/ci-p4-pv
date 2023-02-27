from django.test import TestCase
from .forms import CreateNewPwAccount


class TestCreateNewPwAccount(TestCase):

    def test_password_name_is_required(self):
        form = CreateNewPwAccount({'name':''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_password_website_is_required(self):
        form = CreateNewPwAccount({'website':''})
        self.assertFalse(form.is_valid())
        self.assertIn('website', form.errors.keys())
        self.assertEqual(form.errors['website'][0], 'This field is required.')

    def test_password_email_is_required(self):
        form = CreateNewPwAccount({'email':''})
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(form.errors['email'][0], 'This field is required.')
    
    def test_password_username_is_required(self):
        form = CreateNewPwAccount({'username':''})
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors.keys())
        self.assertEqual(form.errors['username'][0], 'This field is required.')
    
    def test_password_password_is_required(self):
        form = CreateNewPwAccount({'password':''})
        self.assertFalse(form.is_valid())
        self.assertIn('password', form.errors.keys())
        self.assertEqual(form.errors['password'][0], 'This field is required.')

    def test_fields_are_explicit_in_form_metaclass(self):
        form = CreateNewPwAccount()
        self.assertEqual(form.Meta.fields, ['name', 'website', 'email', 'username', 'password'])
