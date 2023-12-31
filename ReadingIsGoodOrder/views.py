import stripe
from django.shortcuts import render
# To get Stripe's secret key
from django.conf import settings
from django.contrib.auth.models import User
from django.http import Http404
from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Order, OrderItem, Book
from .serializers import OrderSerializer, MyOrderSerializer

@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def checkout(request):
    serializer = OrderSerializer(data=request.data)

    if serializer.is_valid():
        stripe.api_key = settings.STRIPE_SECRET_KEY
        paid_amount = sum(item.get('quantity') * item.get('book').price for item in serializer.validated_data['items'])

        # Checking stock
        for item in serializer.validated_data['items']:
            book = Book.objects.get(id=item['book'].id)
            if book.stock < item['quantity']:
                return Response({'error': 'Not enough books in stock'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            charge = stripe.Charge.create(
                amount=int(paid_amount * 100),
                currency='USD',
                description='Charge from Reading Is Good',
                source=serializer.validated_data['stripe_token']
            )

            # Updating stock info
            for item in serializer.validated_data['items']:
                book = Book.objects.get(id=item['book'].id)
                book.stock -= item['quantity']
                book.save()

            serializer.save(user=request.user, paid_amount=paid_amount)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        except Exception as e:
            stripe.Refund.create(charge=charge.id)
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrdersList(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        # If user is Admin 
        if request.user.is_staff:
            orders = Order.objects.all()
        
        else:
            # Custom user's own orders
            orders = Order.objects.filter(user=request.user)
        
        serializer = MyOrderSerializer(orders, many=True)
        
        return Response(serializer.data)
