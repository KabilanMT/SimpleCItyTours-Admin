from django.contrib import admin
from app import models
from .models import Location, Polygon

admin.site.register(Location)
admin.site.register(Polygon)