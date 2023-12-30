
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book, Category

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Creating a test category
        self.category = Category.objects.create(name='Fiction', slug='fiction')
        # Creating a test book
        self.book = Book.objects.create(
            name='Test Book',
            category=self.category,
            slug='test-book',
            price=9.99,
            stock=3,
        )

    def test_latest_books_list(self):
        """ Ensure we can retrieve the latest books """
        url = reverse('latest-books-list')  # URL name from urls.py
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) >= 1)  # Ensure at least one book is returned

    def test_book_detail(self):
        """ Ensure we can retrieve a single book detail """
        url = reverse('book-detail', kwargs={'category_slug': self.category.slug, 'book_slug': self.book.slug})  # URL name and kwargs from urls.py
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test Book')
