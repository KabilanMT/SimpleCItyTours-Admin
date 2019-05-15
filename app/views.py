"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.template import RequestContext
from datetime import datetime
from .models import Location, Polygon, Point, PointType, Audio
from django.contrib.auth.models import User
from django.views import generic
from django.views.generic.edit import DeleteView, UpdateView, CreateView, View
from .forms import UserForm, PasswordForm, CityForm
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from django.forms.models import modelform_factory
from django.forms import TextInput, Textarea, CheckboxInput, Select, NumberInput
import json


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
   form_class = modelform_factory(Location,
   widgets={
       "name": TextInput({
       'class': 'form-control','placeholder': 'city'
       }), 
       "description": Textarea({
       'class': 'form-control','placeholder': 'description'
       }),
       "adminuser": Select({
       'class': 'form-control',
       }),
       "price": NumberInput({
       'class': 'form-control',
       }),
       "visibility": CheckboxInput({
       'class': 'form-control'
       }),},
   fields=('name', 'description', 'adminuser', 'price', 'visibility','id'))
   template_name = 'app/mapEditForm.html'
   def get_pk(self):
        pk= self.kwargs['pk']
        return pk

class cityDelete(DeleteView):
    """Renders the user Creation page"""
    model = Location
    success_url = reverse_lazy('locations')

class userCreation(View):
    """Renders the user Creation page"""
    form_class = UserForm
    template_name = 'app/userCreation.html'

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            user.set_password(password)
            user.save()
            return redirect('users')

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

class cityedit(UpdateView):
    """Renders the user Creation page"""
    model = Location
    form_class = modelform_factory(Location,
    widgets={"name": TextInput()},
    fields=('name',))
    template_name = 'app/cityeditform.html'
    # success_url = reverse_lazy('locations')

class userUpdate(UpdateView):
    """Renders the user Creation page"""
    model = User
    fields = ['username', 'email']
    template_name = 'app/userUpdate.html'
    def get_pk(self):
        pk= self.kwargs['pk']
        return pk

class userDelete(DeleteView):
    """Renders the user Creation page"""
    model = User
    success_url = reverse_lazy('users')

class changePassword(View):
    """Renders the user Creation page"""
    form_class = PasswordForm
    template_name = 'app/changePassword.html'

    def post(self, request, pk):
        form = self.form_class(request.POST)
        user = User.objects.get(pk=pk)

        if form.is_valid():
            password = form.save(commit=False)
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()
            return redirect('users')

    def get(self, request, pk):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})


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

#def cityUpdateAdmin(request, pk):
#     """Renders the locations page."""
#     city = ''
#     usernames = []
#     location = Location.objects.filter(pk=pk)
    
#     for item in location:
#         city = item

#     userlist = User.objects.all()
#     for item in userlist:
#         usernames.append(item)
#     assert isinstance(request, HttpRequest)
#     return render(
#         request,
#         'app/Superuser-MapEdit.html',
#         {
#             'title':'Edit Location',
#             'city': city,
#             'users': User.objects.all(),
#             'usernames': usernames,
#             'year':datetime.now().year,
#         }
#     )

def cityPolygonUpdate(request, pk):
    """Renders the locations page."""
    location = Location.objects.get(pk=pk)
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/MapPolygonUpdate.html',
        {
            'title':'Edit City Bounds',
            'city': location,
            'polygon': location.polygon.points,
            'year':datetime.now().year,
        }
    )

def cityPointsUpdate(request, pk):
    """Renders the locations page."""
    if request.method == 'POST':
        exists = Point.objects.filter(name=request.POST['name']).count()
        if exists == 0:
            pointtypes = PointType.objects.get(name=request.POST.get('tourtype', False))
            point = Point()
            point.location = Location.objects.get(pk=pk)
            point.pointtypes = pointtypes
            point.lat = request.POST.get('lat')
            point.lng = request.POST.get('lng')
            point.name = request.POST['name']
            point.description = request.POST.get('description')
            point.audioFile = request.FILES['file']
            point.save()
        else:
            point = Point.objects.get(name=request.POST['name'])
            return HttpResponse(point)
            pointtypes = PointType.objects.get(name=request.POST.get('tourtype', False))
            point.location = Location.objects.get(pk=pk)
            point.pointtypes = pointtypes
            point.lat = request.POST.get('lat')
            point.lng = request.POST.get('lng')
            point.name = request.POST['name']
            point.description = request.POST.get('description')
            point.audioFile = request.FILES['file']
            point.save()

    location = Location.objects.get(pk=pk)
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/Superuser-MapPoints.html',
        {
            'title':'Edit Points of Interest',
            'city': location,
            'points': Point.objects.all(),
            'polygon': location.polygon.points,
            'year':datetime.now().year,
        }
    )

def users(request):
    """Renders the locations page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/users.html',
        {
            'title':'Users',
            'users': User.objects.all(),
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
            'city': city[0],
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
        'app/MapPolygonCreation.html',
        {
            'title':'Create a new city',
            'polygon': '',
            'users': User.objects.all(),
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def createPolygon(request):
    """Posting to database"""
    if request.is_ajax():
        if request.method == "POST":
            polyCount = Polygon.objects.filter(name=request.POST['name']).count()
            if polyCount > 0:
                oldPolygon = Polygon.objects.get(name=request.POST['name'])
                oldPolygon.delete()

            polygon = Polygon.objects.create(
                name=request.POST['name'],
                points=request.POST['points'],
                strokeColor=request.POST['strokeColor'],
                strokeWeight=request.POST['strokeWeight'],
                strokeOpacity=request.POST['strokeOpacity'],
                fillColor=request.POST['fillColor'],
                fillOpacity=request.POST['fillOpacity']
                )
            return redirect(polygon)

def updatePolygon(request):
    """Posting to database"""
    if request.is_ajax():
        if request.method == "POST":
            polygon = Polygon.objects.get(name=request.POST['name'])
            polygon.points = request.POST['points']
            polygon.save()
            return redirect(polygon)

def createCity(request):
    """Posting to database"""
    if request.is_ajax():
        if request.method == "POST":
            polygon = Polygon.objects.get(name=request.POST['name'])
            user = User.objects.get(username=request.POST['admin'])
            # user = User.objects.get(username="admin")
            # string = user.username + " " + polygon.name + " " + request.POST['description'] + " " + str(request.POST['lat']) + " " + str(request.POST['lng']) + " " + str(request.POST['zoom']) + " " + str(request.POST['price'])
            # return HttpResponse(string)
            city = Location.objects.create(
                name=str(request.POST['name']),
                description=str(request.POST['description']),
                lat=float(request.POST['lat']),
                lng=float(request.POST['lng']),
                price=float(request.POST['price']),
                zoom=int(request.POST['zoom']),
                adminuser=user,
                visibility=False,
                # img=request.POST['img'],
                polygon=polygon
                )
            return redirect(city)

def createPoint(request):
    """Posting to database"""
    if request.is_ajax():
        if request.method == "POST":
            exists = Point.objects.filter(name=request.POST['name']).count()
            if exists == 0:
                location = Location.objects.get(name=request.POST['locationName'])
                pointtypes = PointType.objects.get(name=request.POST['typeName'])
                point = Point()
                point.location = location
                point.pointtypes = pointtypes
                point.lat = request.POST['lat']
                point.lng = request.POST['lng']
                point.name = request.POST['name']
                point.description = request.POST['description']
                # point.audioFile = request.FILES['file']
                point.save()
                return redirect(home)
            else:
                return redirect(home)


def deletePoint(request):
    """Posting to database"""
    if request.is_ajax():
        if request.method == "POST":
            instance = Point.objects.get(name=request.POST['name'])
            instance.delete()
            return redirect('locations')

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

def payment(request):
    """Renders the city creation page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/Stripe.html',
        {
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def audio(request):
    """Renders the city creation page."""
    if request.method == 'POST':
        instance = Audio(fileUpload=request.FILES['file'], name=request.POST['name'])
        instance.save()
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/fileUpload.html',
        {
            'title':'file upload',
            'files': Audio.objects.all()
        }
    )

def purchase(request):
    """Adding user to city list"""
    if request.method == "POST":
        location = Location.objects.get(name=request.POST['locationName'])
        user = User.objects.get(username=request.POST['username'])
        location.users.add(user)