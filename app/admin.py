from django.contrib import admin
from app import models
from .models import Location, Polygon, PointType, Point

admin.site.register(Location)
admin.site.register(Polygon)
admin.site.register(PointType)
admin.site.register(Point)