from rest_framework import serializers
from .models import Bank

class BankSerializer(serializers.ModelSerializer):
    branch_count = serializers.SerializerMethodField()

    class Meta:
        model = Bank
        fields = ['id', 'name', 'swift_code', 'is_islamic', 'established_date', 'branch_count']

    def get_branch_count(self, obj):
        return obj.branches.count()