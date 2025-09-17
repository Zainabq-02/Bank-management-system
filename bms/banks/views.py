
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Bank
from .serializers import BankSerializer

class BankListAPIView(APIView):
    def get(self, request):
        banks = Bank.objects.all()
        serializer = BankSerializer(banks, many=True)
        return Response(serializer.data)