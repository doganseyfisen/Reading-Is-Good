
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from ReadingIsGoodBook.models import Book, Category
from .models import Order

class OrderAPITestCase(APITestCase):
    def setUp(self):
        # Creating a test user
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client.force_authenticate(user=self.user)
        
        # Creating a test category
        self.category = Category.objects.create(name='Fiction', slug='fiction')

        # Creating a test book (assuming Book model from ReadingIsGoodBook app)
        self.book = Book.objects.create(
            name='Test Book', 
            price=9.99, 
            slug='test-book',
            category=self.category)

        # Creating a test order
        self.order = Order.objects.create(
            user=self.user, 
            first_name='John', 
            last_name='Doe', 
            email='johndoe@example.com', 
            phone = '123456789',
            address='123 Main St', 
            zipcode='12345', 
            place='Test City')

    def test_order_checkout(self):
        """ Ensure the checkout process works correctly """
        url = reverse('checkout')  # URL name from urls.py
        data = {'first_name': 'John', 
                'last_name': 'Doe', 
                'email': 'johndoe@example.com',
                'phone': '123456789', 
                'address': '123 Main St', 
                'zipcode': '12345',
                'place': 'Test City'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_orders_list(self):
        """ Ensure we can retrieve the list of orders """
        url = reverse('orders-list')  # URL name from urls.py
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) >= 1)  # Ensure at least one order is returned
