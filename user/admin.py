from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserCust


class CustomUserAdmin(UserAdmin):
    pass


admin.site.register(UserCust)

