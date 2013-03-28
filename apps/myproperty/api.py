#from django.db import models

from tastypie.authentication import ApiKeyAuthentication  # , Authentication, BasicAuthentication
from tastypie.authorization import DjangoAuthorization  # , Authorization
from tastypie.resources import ModelResource

from myproperty.models import PaymentType


class PaymentTypeResource(ModelResource):
    class Meta:
        queryset = PaymentType.objects.all()
        resource_name = 'myproperty/paymenttype'
        #excludes = ['email', 'password', 'is_superuser']
        # Add it here.
        authentication = ApiKeyAuthentication()
        authorization = DjangoAuthorization()
