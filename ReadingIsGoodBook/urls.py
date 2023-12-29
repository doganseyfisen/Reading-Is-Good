from django.urls import path, include
from ReadingIsGoodBook import views

urlpatterns = [
    path('latest-books/', views.LatestBooksList.as_view()),
    path('books/search/', views.search),
    path('books/<slug:category_slug>/<slug:book_slug>/', views.BookDetail.as_view()),
    path('books/<slug:category_slug>/', views.CategoryDetail.as_view()),
]
