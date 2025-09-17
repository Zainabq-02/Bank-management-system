# accounts/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import BankAccount
from .serializers import BankAccountSerializer

class UserAccountsAPIView(APIView):
    permission_classes = [IsAuthenticated]  # 🔒 Require login

    def get(self, request):
        # Only fetch accounts for the logged-in user
        accounts = BankAccount.objects.filter(user=request.user)
        serializer = BankAccountSerializer(accounts, many=True)
        return Response(serializer.data)
