#import datetime

from django.db import models
from django.contrib.auth.models import User

from tastypie.models import create_api_key

from utils import django_choices


PROPERTY_TYPE_CHOICES = django_choices(campground=1, bb=2)


class PaymentType(models.Model):
    """
    This is edited by us not clients.

    cash=1, check=2, stripe=3, square=4
    """
    name = models.CharField(max_length=35)

    def __unicode__(self):
        return self.name


#models.signals.post_save.connect(create_api_key, sender=User)
