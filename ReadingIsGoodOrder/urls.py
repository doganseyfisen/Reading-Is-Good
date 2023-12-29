from django.urls import path
from ReadingIsGoodOrder import views

urlpatterns = [
    path('checkout/', views.checkout),
    path('orders/', views.OrdersList.as_view()),  
]