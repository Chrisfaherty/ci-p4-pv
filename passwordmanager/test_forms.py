from django.test import TestCase
from .forms import AccountForm


class TestItemForm(TestCase):

    def test_password_name_is_required(self):
        from = AccountForm({'name':''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    
    def test_done_field_is_not_required(self):
        form = AccountForm({'name': 'Test Password'})
        self.assertTrue(form.is_valid())


    def test_fields_are_explicit_in_form_metaclass(self):
        form = AccountForm()
        self.assertEqual(form.Meta.fields, ['name', 'done'])
