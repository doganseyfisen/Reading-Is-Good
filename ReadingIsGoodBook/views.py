from .serializers import BookSerializer, CategorySerializer
from .models import Book, Category
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import Http404

class LatestBooksList(APIView):
    def get(self, request, format=None):
        books = Book.objects.all()[0:4]
        serializer = BookSerializer(books, many=True)

        return Response(serializer.data)
    
class BookDetail(APIView):
    def get_object(self, category_slug, book_slug):
        try:
            """
            Attention!!!
            The double underscore '__' in 'category__slug' is used to access fields of a related model in Django. Here, it performs a query on the 'slug' field of the 'Category' model, which is related to the 'Book' model through a ForeignKey. This approach simplifies querying related model fields, acting like a JOIN operation in SQL, enhancing readability and efficiency.
            """
            return Book.objects.filter(category__slug=category_slug).get(slug=book_slug)
        except Book.DoesNotExist:
            raise Http404
        
    def get(self, request, category_slug, book_slug, format=None):
        book = self.get_object(category_slug, book_slug)
        serializer = BookSerializer(book)

        return Response(serializer.data)
    
class CategoryDetail(APIView):
    def get_object(self, category_slug):
        try:
            return Category.objects.get(slug=category_slug)
        except Book.DoesNotExist:
            raise Http404
        
    def get(self, request, category_slug, format=None):
        category = self.get_object(category_slug)
        serializer = CategorySerializer(category)

        return Response(serializer.data)

# Searching    
@api_view(['POST'])
def search(request):
    query = request.data.get('query', '')

    if query:
        books = Book.objects.filter(name__icontains=query)
        serializer = BookSerializer(books, many=True)

        return Response(serializer.data)
    
    else:
        return Response({"books": []})