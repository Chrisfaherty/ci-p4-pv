from django.test import TestCase
from .models import PwAccount
from . import views

# Testing the pwmanagerapp views
class TestViews(TestCase):

    def test_get_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/home.html')

    def test_get_add_password_page(self):
        response = self.client.get('/create')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pwmanagerapp/createpw.html')

    def test_get_edit_password_page(self):
        passwords = PwAccount.objects.create(name='Test password')
        response = self.client.get(f'/edit/{acc.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_password.html')
    
    def test_can_add_password(self):
        response = self.client.post('/create', {'name': 'Test Added Password'})
        self.assertRedirect(response, 'pwmanagerapp/list.html')

    def test_can_delete_password(self):
        passwords = PwAccount.objects.create(name='Test password')
        response = self.client.get(f'/delete/{acc.id}')
        self.assertRedirect(response, 'pwmanagerapp/list.html')
        exsisting_passwords = PwAccount.objects.filter(id=acc.id)
        self.assertEqual(len(existing_passwords),0)
