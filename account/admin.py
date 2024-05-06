from django.contrib import admin
from .models import CustomUser


class UserModelAdmin(admin.ModelAdmin):
    list_display = ['email', 'is_staff', 'is_vendor', 'is_customer']


admin.site.register(CustomUser, UserModelAdmin)