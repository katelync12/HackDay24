from django.contrib import admin
from .models import User, Messages

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'name', 'state', 'adoption', 'reimbursement', 'csection')
    search_fields = ('username', 'name', 'state')

@admin.register(Messages)
class MessagesAdmin(admin.ModelAdmin):
    list_display = ('username', 'role', 'sender', 'message')
    search_fields = ('username', 'role', 'sender')
