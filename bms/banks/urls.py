from django.urls import path
from .views import BankListAPIView

urlpatterns = [
    path('banks/', BankListAPIView.as_view(), name='banks-list'),
]