from django.urls import path, include
from ReadingIsGoodBook import views

urlpatterns = [
    # name="latest-book-list" used in tests.py
    path('latest-books/', views.LatestBooksList.as_view(), name="latest-books-list"),
    path('books/search/', views.search),
    # name="book-detail" used in tests.py
    path('books/<slug:category_slug>/<slug:book_slug>/', views.BookDetail.as_view(), name="book-detail"),
    path('books/<slug:category_slug>/', views.CategoryDetail.as_view()),
]
