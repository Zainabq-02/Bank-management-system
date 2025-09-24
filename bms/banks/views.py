from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Bank
from .serializers import BankSerializer

class BankListCreateAPIView(ListCreateAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer

class BankDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer