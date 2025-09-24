

# Register your models here.
from django.contrib import admin
from .models import Bank, BankBranch

@admin.register(Bank)
class BankAdmin(admin.ModelAdmin):
    list_display = ('name', 'swift_code', 'is_islamic', 'established_date')
    list_filter = ('is_islamic',)
    search_fields = ('name', 'swift_code')

@admin.register(BankBranch)
class BankBranchAdmin(admin.ModelAdmin):
    list_display = ('name', 'bank', 'branch_code', 'address')
    search_fields = ('name', 'branch_code', 'address')