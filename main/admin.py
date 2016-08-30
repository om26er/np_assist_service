from django.contrib import admin
from django.contrib.auth.models import Group

from main.models import User, Service


class UserAdmin(admin.ModelAdmin):
    fields = (
        'is_active',
        'email',
        'password',
        'first_name',
        'last_name',
        'mobile_phone',
        'home_phone',
        'default_property',
    )
    readonly_fields = (
        'email',
        'password',
        'default_property',
    )

    class Meta:
        model = User


class ServiceRequestAdmin(admin.ModelAdmin):
    class Meta:
        model = Service


admin.site.register(User, UserAdmin)
admin.site.register(Service, ServiceRequestAdmin)
admin.site.unregister(Group)
