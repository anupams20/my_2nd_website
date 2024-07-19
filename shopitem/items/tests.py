# tests.py

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Itemlist
from .forms import Userform, ShoppingItemForm

class ViewsTestCase(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')
        self.item = Itemlist.objects.create(name='Item 1', price=10.0, discount=45)  # Example item
        
    def test_post_list_view(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'items/item_list.html')
        # Add more assertions as needed
    
    def test_hello_view(self):
        response = self.client.get(reverse('post_list'))  # Assuming 'post_list' is the correct view name for 'hello'
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'items/item_list.html')
        # Add more assertions as needed
    
    def test_signup_view_get(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'items/signup.html')
        # Add more assertions as needed
    
    def test_signup_view_post(self):
        data = {
            'email': 'test@example.com',
            'password': 'testpassword',
            'form-TOTAL_FORMS': 1,
            'form-INITIAL_FORMS': 0,
            'form-MIN_NUM_FORMS': 0,
            'form-MAX_NUM_FORMS': 1000,
            'form-0-name': 'John Doe',
            'form-0-phone_number': '1234567890',
            'form-0-place': 'Someplace',
        }
        response = self.client.post(reverse('signup'), data)
        self.assertEqual(response.status_code, 302)  # Expecting redirect upon successful signup
        self.assertRedirects(response, reverse('signup_done'))
        # Add more assertions as needed
    
    def test_login_view_get(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'items/login.html')
        # Add more assertions as needed
    
    def test_login_view_post_valid_credentials(self):
        data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'testpassword',
        }
        response = self.client.post(reverse('login'), data)
        self.assertEqual(response.status_code, 302)  # Expecting redirect upon successful login
        self.assertRedirects(response, reverse('success_url'))
        # Add more assertions as needed
    
    def test_shopping_items_view_get(self):
        response = self.client.get(reverse('shopping_items'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'items/shopping_items.html')
        # Add more assertions as needed
    
    def test_shopping_items_view_post(self):
        data = {
            'form-TOTAL_FORMS': 1,
            'form-INITIAL_FORMS': 0,
            'form-MIN_NUM_FORMS': 0,
            'form-MAX_NUM_FORMS': 1000,
            'form-0-name': 'Item 2',
            'form-0-price': 20.0,
            'form-0-discount': 23,
        }
        response = self.client.post(reverse('shopping_items'), data)
        self.assertEqual(response.status_code, 302)  # Expecting redirect upon successful form submission
        self.assertRedirects(response, reverse('shopping_items_done'))
        # Add more assertions as needed
    
    def test_logout_view(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)  # Expecting redirect upon logout
        self.assertRedirects(response, reverse('logout_done'))
        # Add more assertions as needed
    
    def test_password_change_view(self):
        self.client.force_login(self.user)
        data = {
            'old_password': 'testpassword',
            'new_password1': 'newtestpassword',
            'new_password2': 'newtestpassword',
        }
        response = self.client.post(reverse('password_change'), data)
        self.assertEqual(response.status_code, 302)  # Expecting redirect upon password change
        self.assertRedirects(response, reverse('password_change_done'))
        # Add more assertions as needed

