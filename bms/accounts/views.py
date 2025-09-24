from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import BankAccount
from .serializers import BankAccountSerializer
from rest_framework.permissions import IsAuthenticated

class AccountListCreateAPIView(ListCreateAPIView):
    serializer_class = BankAccountSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Show only current user's accounts
        return BankAccount.objects.filter(user=self.request.user)

class AccountDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = BankAccountSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Show only current user's accounts
        return BankAccount.objects.filter(user=self.request.user)