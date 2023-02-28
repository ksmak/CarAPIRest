# Django
from django.contrib import admin

# Local
from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    """Custom user admin model."""
    model = CustomUser
    list_display = (
        'username',
        'first_name',
        'last_name',
        'email',
        'is_active'
    )
    list_display_links = list_display
    search_fields = list_display
    add_fieldsets = (
        (None, {
            'classes':(
                'wide'
            ),
            'fields': (
                'username',
                'password1',
                'password2',
                'first_name',
                'last_name',
                'email',
            )
        }),
        ('Permissions', {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser'
            )
        })
    )
    fieldsets = (
        (None, {
            'fields': (
                'username',
                'password',
                'first_name',
                'last_name',
                'email',
            )
        }),
        ('Permissions', {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser'
            )
        })
    )


admin.site.register(CustomUser, CustomUserAdmin)
