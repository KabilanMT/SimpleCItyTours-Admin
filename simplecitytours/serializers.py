from django.contrib.auth import get_user_model
from rest_framework import serializers
from app.models import Polygon, LandingPage, Location, PointType, Point, Tourist, UserPayment, AdminActiveTime


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = (
            'id',
            'username',
            'password',
            'email'
        )
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        return super(UserSerializer, self).update(instance, validated_data)



class PolygonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Polygon
        fields = [
            'id',
            'points',
            'created',
            'last_updated',
            'strokeColor',
            'strokeWeight',
            'strokeOpacity',
            'fillColor',
            'strokeWeight',
            'fillOpacity',
        ]



class LandingPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = LandingPage
        fields = '__all__'




class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'



class PointTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PointType
        fields = [
            'id',
            'name',
        ]



class PointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Point
        fields = '__all__'



class TouristSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tourist
        fields = '__all__'




class UserPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPayment
        fields = '__all__'




class AdminActiveTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminActiveTime
        fields = '__all__'


