from rest_framework import serializers

from . import models

class OrderRouteSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.OrderRoute
        fields = '__all__'


class CitySerializers(serializers.ModelSerializer):
    class Meta:
        model = models.City
        fields = '__all__'


class TransportSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Transport
        fields = '__all__'



class RouteStatusSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.RouteStatus
        fields = '__all__'



class StatusSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Status
        fields = '__all__'


class RetriveTypeSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.RetriveType
        fields = '__all__'


class OrderSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = '__all__'
