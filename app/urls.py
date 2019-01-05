"""simplecitytour URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  url(r'blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include
from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
# from .views import Tour_cities
from simplecitytours import views

urlpatterns = [
    url(r'login/', obtain_jwt_token),
    url(r'verify_token/', verify_jwt_token),
    url(r'logout/', refresh_jwt_token),
    # url(r'testapi/', views.test_resp, name='testresp'),
    url(r'signup/', views.signup_user, name='signup'),
    url(r'getaudio/', views.get_audio, name='audio'),
    url(r'get_imgs/', views.get_cities_imgs, name='imgs'),
    url(r'check_update/', views.check_sequence, name='check-update'),
    url(r'get_points/', views.get_points, name='points'),
    url(r'get_all_locations/', views.get_all_locations, name='get-locations'),
    # url(r'accounts/', include('django.contrib.auth.urls')),
    url(r'types/', views.getPointTypes, name='check-types'),
]