from django.urls import path
from ReadingIsGoodOrder import views

urlpatterns = [
    path('checkout/', views.checkout, name="checkout"),
    path('orders/', views.OrdersList.as_view(), name="orders-list"),  
]