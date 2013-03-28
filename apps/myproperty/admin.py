#import re

#from django import forms
from django.contrib import admin
#from django.contrib.auth.models import User
#from django.contrib.contenttypes import generic
#from django.contrib.flatpages.admin import FlatPageAdmin
#from django.contrib.flatpages.models import FlatPage
#from django.db.models import TextField  # , Q
#from django.forms import ModelForm
#from django.forms.widgets import RadioSelect
#from django.http import HttpResponseRedirect, HttpResponse

from myproperty.models import PaymentType


admin.site.register(PaymentType)
