

# Register your models here.
from django.contrib import admin
from .models import BankAccount

@admin.register(BankAccount)
class BankAccountAdmin(admin.ModelAdmin):
    list_display = ('account_number', 'user', 'bank_branch', 'account_type', 'balance', 'is_active')
    list_filter = ('account_type', 'is_active')
    search_fields = ('account_number', 'user__username')