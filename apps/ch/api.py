from django.conf.urls import url
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db import models

#from tastypie.authentication import BasicAuthentication
#from tastypie.authorization import DjangoAuthorization
from tastypie.http import HttpUnauthorized, HttpForbidden
from tastypie.models import ApiKey, create_api_key
from tastypie.resources import ModelResource
from tastypie.utils import trailing_slash


"""
class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'auth/user'
        excludes = ['email', 'password', 'is_superuser']
        # Add it here.
        authentication = BasicAuthentication()
        authorization = DjangoAuthorization()
"""


class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        fields = ['first_name', 'last_name', 'email']
        allowed_methods = ['get', 'post']
        resource_name = 'user'

    def override_urls(self):
        return [
            url(r"^(?P<resource_name>%s)/login%s$" %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('login'), name="api_login"),
            url(r'^(?P<resource_name>%s)/logout%s$' %
                (self._meta.resource_name, trailing_slash()),
                self.wrap_view('logout'), name='api_logout'),
        ]

    def login(self, request, **kwargs):
        self.method_check(request, allowed=['post'])
        #print 4444; import pdb;pdb.set_trace()

        data = self.deserialize(request, request.body, format=request.META.get('CONTENT_TYPE', 'application/json'))

        username = data.get('username', '')
        password = data.get('password', '')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)

                try:
                    key = ApiKey.objects.get(user=user)
                except ApiKey.DoesNotExist:
                    return self.create_response(
                        request, {
                            'success': False,
                            'reason': 'missing key',
                        },
                        HttpForbidden,
                    )

                ret = self.create_response(request, {
                    'success': True,
                    'username': user.username,
                    'key': key.key
                })
                #print 5656; import pdb;pdb.set_trace()
                return ret
            else:
                return self.create_response(
                    request, {
                        'success': False,
                        'reason': 'disabled',
                    },
                    HttpForbidden,
                )
        else:
            return self.create_response(
                request, {
                    'success': False,
                    'reason': 'invalid login',
                    'skip_login_redir': True,
                },
                HttpUnauthorized,
            )

    def logout(self, request, **kwargs):
        self.method_check(request, allowed=['get'])
        if request.user and request.user.is_authenticated():
            logout(request)
            return self.create_response(request, {'success': True})
        else:
            return self.create_response(request, {'success': False}, HttpUnauthorized)

models.signals.post_save.connect(create_api_key, sender=User)
