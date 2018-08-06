"""
Definition of urls for simplecitytours.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views
from django.conf import settings
from django.conf.urls.static import static

import app.forms
import app.views

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^$', app.views.home, name='home'),
    url(r'^locations/$', app.views.locations, name='locations'),
    url(r'^map/$', app.views.map, name='map'),
    url(r'^users/$', app.views.users, name='users'),
    url(r'^userCreation/$', app.views.userCreation.as_view(), name='userCreation'),
    url(r'^user/(?P<pk>[0-9]+)/update/$', app.views.userUpdate.as_view(), name='userUpdate'),
    url(r'^user/(?P<pk>[0-9]+)/test/$', app.views.userUpdate.get_context_data, name='userTest'),
    url(r'^user/(?P<pk>[0-9]+)/delete/$', app.views.userDelete.as_view(), name='userDelete'),
    url(r'^user/(?P<pk>[0-9]+)/password/$', app.views.changePassword.as_view(), name='changePassword'),
    url(r'^createCity/$', app.views.createCity, name='createCity'),
    url(r'^createPolygon/$', app.views.createPolygon, name='createPolygon'),
    url(r'^updatePolygon/$', app.views.updatePolygon, name='updatePolygon'),
    url(r'^city/(?P<pk>[0-9]+)/$', app.views.DetailView.as_view(), name='city'),
    url(r'^cityUpdate/(?P<pk>[0-9]+)/$', app.views.cityUpdate.as_view(), name='cityUpdate'),
    url(r'^cityUpdateAdmin/(?P<pk>[0-9]+)/$', app.views.cityUpdateAdmin.as_view(), name='cityUpdateAdmin'),
    url(r'^cityPolygonUpdate/(?P<pk>[0-9]+)/$', app.views.cityPolygonUpdate, name='cityPolygonUpdate'),
    url(r'^cityPointsUpdate/(?P<pk>[0-9]+)/$', app.views.cityPointsUpdate, name='cityPointsUpdate'),
    url(r'^createPoint/$', app.views.createPoint, name='createPoint'),
    url(r'^payment/$', app.views.payment, name='payment'),
    url(r'^audio/$', app.views.audio, name='audio'),
    url(r'^about', app.views.about, name='about'),
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'app/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Login',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
     url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 