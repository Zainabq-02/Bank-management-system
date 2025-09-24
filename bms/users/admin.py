

# Register your models here.
from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'phone', 'date_of_birth', 'is_staff')
    search_fields = ('username', 'phone')