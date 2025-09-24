from django.urls import path
from .views import BankListCreateAPIView, BankDetailAPIView

urlpatterns = [
    path('banks/', BankListCreateAPIView.as_view(), name='bank-list-create'),
    path('banks/<int:pk>/', BankDetailAPIView.as_view(), name='bank-detail'),
]