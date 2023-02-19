from django.test import TestCase
from .models import Password


class TestViews(TestCase):


    def test_get_passmanager(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'passmanager.html')

    def test_get_add_password_page(self):
        response = self.client.get('/add')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_password.html')

    def test_get_edit_password_page(self):
        passwords = Password.objects.create(name='Test password')
        response = self.client.get(f'/edit/{password.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_password.html')
    
    def test_can_add_password(self):
        response = self.client.post('/add', {'name': 'Test Added Password'})
        self.assertRedirect(response, '/')


    def test_can_delete_password(self):
        passwords = Password.objects.create(name='Test password')
        response = self.client.get(f'/delete/{password.id}')
        self.assertRedirect(response, '/')
        exsisting_passwords = Password.objects.filter(id=password.id)
        self.assertEqual(len(existing_passwords),0)


    def test_can_edit_password(self):
        passwords = Password.objects.create(name='Test password')
        response = self.client.post(f'/edit/{password.id}', {'name': 'Updated Name'})
        self.assertRedirect(response, '/')
        updated_passwords = Password.objects.get(id=password.id)
        self.assertEqual(updated_password.name, 'Updated Name')




        
