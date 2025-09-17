from django.urls import path
from .views import UserAccountsAPIView

urlpatterns = [
    path('accounts/', UserAccountsAPIView.as_view(), name='user-accounts'),
]