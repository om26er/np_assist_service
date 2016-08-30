from django.db import models

from simple_login.models import BaseUser

SERVICE_STATUS_PENDING = 1
SERVICE_STATUS_IN_PROGRESS = 2
SERVICE_STATUS_DONE = 3

SERVICE_ACTIVE_STATES = [SERVICE_STATUS_PENDING, SERVICE_STATUS_IN_PROGRESS]
STATUS_CHOICES = ((1, 'Pending'), (2, 'InProgress'), (3, 'Done'),)


class User(BaseUser):
    first_name = models.CharField(max_length=255, blank=False)
    last_name = models.CharField(max_length=255, blank=False)
    home_phone = models.CharField(max_length=255, blank=True)
    mobile_phone = models.CharField(max_length=255, blank=False)
    default_property = models.OneToOneField('Property', blank=True, null=True)


class Property(models.Model):
    owner = models.ForeignKey('User', blank=False, related_name='Owner')
    address = models.CharField(max_length=2000, blank=False)
    postcode = models.CharField(max_length=255, blank=False)
    category_primary = models.CharField(max_length=255, blank=False)
    category_secondary = models.CharField(max_length=255, blank=False)
    age = models.IntegerField(blank=False)

    def __str__(self):
        return 'Property of {}'.format(self.owner.email)


class Service(models.Model):
    site = models.ForeignKey(Property, blank=False, related_name='Property')
    status = models.IntegerField(
        default=SERVICE_STATUS_PENDING, choices=STATUS_CHOICES, blank=False)
    description = models.CharField(max_length=5000, blank=False)
    purpose = models.CharField(max_length=255, blank=False)
    paid_for = models.BooleanField(default=False)

    @property
    def requester_email(self):
        return self.site.owner.email

    @property
    def address(self):
        return self.site.address

    @property
    def phone_number(self):
        return self.site.owner.mobile_phone

    def __str__(self):
        return '{} @ {}'.format(self.purpose, self.address)
