from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from factufast.users.forms import UserAdminChangeForm, UserAdminCreationForm
from factufast.users.models import Client

User = get_user_model()


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):

    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    list_display = ["username", "name", "is_superuser"]
    search_fields = ["name"]


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ["name", "address", "city", "phone_number", "email"]
    list_filter = ["city"]
    search_fields = ["name", "city", "phone_number", "email"]
    list_per_page = 25

    