"""
Definition of urls for simplecitytours.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

import app.forms
import app.views

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^$', app.views.home, name='home'),
    url(r'^locations$', app.views.locations, name='locations'),
    url(r'^map/$', app.views.map, name='map'),
    url(r'^userCreation$', app.views.userCreation.as_view(), name='userCreation'),
    url(r'^createCity/$', app.views.createCity, name='createCity'),
    url(r'^city/(?P<pk>[0-9]+)/$', app.views.DetailView.as_view(), name='city'),
    url(r'^cityUpdate/(?P<pk>[0-9]+)/$', app.views.cityUpdate.as_view(), name='cityUpdate'),
    url(r'^cityUpdateAdmin/(?P<pk>[0-9]+)/$', app.views.cityUpdateAdmin.as_view(), name='cityUpdateAdmin'),
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
