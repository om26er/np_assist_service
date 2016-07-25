from django.contrib import admin
from django.contrib.auth.models import Group

from main.models import User


class UserAdmin(admin.ModelAdmin):
    fields = (
        'is_active',
        'email',
        'password',
        'first_name',
        'last_name',
        'mobile_phone',
        'home_phone',
    )
    readonly_fields = (
        'email',
        'password',
    )

    class Meta:
        model = User


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
