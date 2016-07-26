from django.db import models

from simple_login.models import BaseUser

SERVICE_STATUS_PENDING = 1
SERVICE_STATUS_IN_PROGRESS = 2
SERVICE_STATUS_DONE = 3

SERVICE_ACTIVE_STATES = [SERVICE_STATUS_PENDING, SERVICE_STATUS_IN_PROGRESS]


class User(BaseUser):
    first_name = models.CharField(max_length=255, blank=False)
    last_name = models.CharField(max_length=255, blank=False)
    home_phone = models.CharField(max_length=255, blank=True)
    mobile_phone = models.CharField(max_length=255, blank=False)


class Property(models.Model):
    owner = models.ForeignKey(User, blank=False, related_name='Owner')
    address = models.CharField(max_length=2000, blank=False)
    postcode = models.CharField(max_length=255, blank=False)
    category_primary = models.IntegerField(blank=False)
    category_secondary = models.IntegerField(blank=False)
    age = models.IntegerField(blank=False)


class Service(models.Model):
    site = models.ForeignKey(Property, blank=False, related_name='Property')
    status = models.IntegerField(default=SERVICE_STATUS_PENDING, blank=False)
    message = models.CharField(max_length=5000, blank=False)

    @property
    def requester(self):
        return self.site.owner.id
