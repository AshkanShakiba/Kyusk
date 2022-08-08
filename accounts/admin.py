from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import KyuskUserCreationForm, KyuskUserChangeForm
from .models import KyuskUser


class KyuskUserAdmin(UserAdmin):
    add_form = KyuskUserCreationForm
    form = KyuskUserChangeForm
    model = KyuskUser
    list_display = [
        "username",
        "email",
        "age",
        "is_staff",
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("age",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("age",)}),)


admin.site.register(KyuskUser, KyuskUserAdmin)
