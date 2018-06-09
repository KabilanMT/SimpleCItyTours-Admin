"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from .models import Location
from django.contrib.auth.models import User
from django.views import generic
from django.views.generic.edit import UpdateView


class DetailView(generic.DetailView):
    model = Location
    fields = ['name']
    template_name = "app/city.html"

class cityUpdate(UpdateView):
    model = Location
    fields = ['name', 'description' , 'visibility']
    template_name = 'app/location_form.html'

def home(request):
    """Renders the home page."""
    if request.user.is_authenticated():
        city = ''
        for i in Location.objects.all():
            if i.adminuser == request.user:
                city = i
        assert isinstance(request, HttpRequest)
        return render(
            request,
            'app/index.html',
            {
                'city' : city,
                'cityid' : str(city.id),
                'title':'SimpleCityTours',
                'year':datetime.now().year,
            })
    else:
        city = ''
        for i in Location.objects.all():
            if i.adminuser == request.user:
                city = i
        assert isinstance(request, HttpRequest)
        return render(
            request,
            'app/index.html',
            {
                'city' : city,
                'title':'SimpleCityTours',
                'year':datetime.now().year,
            })

def locations(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/locations.html',
        {
            'title':'Locations',
            'locations': Location.objects.all(),
            'year':datetime.now().year,
        }
    )

def city(request):
    """Renders the contact page."""
    city = ''
    for i in Location.objects.all():
        if i.adminuser == request.user:
            city = i
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/city.html',
        {
            'title':'City',
            'city': city,
            'user': request.user,
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def map(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/Superuser-MapPolygon.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )
