"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.template import RequestContext
from datetime import datetime
from .models import Location
from django.contrib.auth.models import User
from django.views import generic
from django.views.generic.edit import UpdateView, CreateView, View
from .forms import UserForm
from django.shortcuts import render, redirect


class DetailView(generic.DetailView):
    """Renders the city details"""
    model = Location
    fields = ['name']
    template_name = "app/city.html"

class cityUpdate(UpdateView):
    """Renders the edit city page"""
    model = Location
    fields = ['name', 'description' , 'visibility']
    template_name = 'app/location_form.html'

class cityUpdateAdmin(UpdateView):
    """Renders the edit city page"""
    model = Location
    fields = ['name', 'description' , 'visibility', 'adminuser']
    template_name = 'app/location_form.html'

class userCreation(CreateView):
    """Renders the user Creation page"""
    model = User
    fields = ['username', 'password', 'email']
    template_name = 'app/userCreation.html'

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
    """Renders the locations page."""
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
    """Renders the cities page."""
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
    """Renders the city creation page."""
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


def createCity(request):
    """Posting to database"""
    if request.is_ajax():
        if request.method == "POST":
            city = Location.objects.create(
                name=request.POST['name'],
                description=request.POST['description'],
                lat=request.POST['lat'],
                lng=request.POST['lng'],
                price=request.POST['price'],
                zoom=request.POST['zoom'],
                adminuser=User.objects.all()[:1].get(),
                img=request.POST['img']
                )
            

#def userCreation(request):
#    """Renders the about page."""
#    assert isinstance(request, HttpRequest)
#    return render(
#        request,
#        'app/userCreation.html',
#        {
#            'title':'Create new User',
#            'message':'Your application description page.',
#            'year':datetime.now().year,
#        }
#    )