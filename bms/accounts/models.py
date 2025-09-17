

# Create your models here.
from django.db import models
from banks.models import BankBranch
from users.models import User

class BankAccount(models.Model):
    ACCOUNT_TYPE_CHOICES = [
        ('SAVINGS', 'Savings'),
        ('CURRENT', 'Current'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='accounts')
    bank_branch = models.ForeignKey(BankBranch, on_delete=models.CASCADE, related_name='accounts')
    account_number = models.CharField(max_length=20)
    account_type = models.CharField(max_length=10, choices=ACCOUNT_TYPE_CHOICES)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.account_number} ({self.user.username})"