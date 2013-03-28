from django.conf import settings
from django.conf.urls import patterns, include, url
#from django.conf.urls.static import static
#from django.views.generic import TemplateView

from ch.api import UserResource
from myproperty.api import PaymentTypeResource


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    'ch.views',

    url(r'^api/', include(UserResource().urls)),
    url(r'^api/', include(PaymentTypeResource().urls)),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    #from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    #urlpatterns += staticfiles_urlpatterns()
    #urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += patterns(
        '',
        url(
            r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
            }
        ),
    )
