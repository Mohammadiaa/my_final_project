from django.contrib import admin
from .models import Contact, User
# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'subject', 'created_date', 'updated_date')
    search_fields = ('name', 'email', 'subject', 'message')
    list_filter = ('created_date', 'updated_date')
    ordering = ('-created_date',)


@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'active', 'superuser', 'staff', 'created_date')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('active', 'superuser', 'staff', 'created_date')
    ordering = ('-created_date',)