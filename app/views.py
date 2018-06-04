"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from .models import Location

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'SimpleCityTours',
            'year':datetime.now().year,
        }
    )

def locations(request):
    """Renders the contact page."""
    location_array = []
    location_set = Location.objects.all()
    for i in location_set:
        location_array.append(i.name)
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/locations.html',
        {
            'title':'Locations',
            'locations': location_array,
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
