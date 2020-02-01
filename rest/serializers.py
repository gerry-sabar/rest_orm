from rest_framework import serializers
from rest.models import *


class OwnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Owner
        fields = [
            "name",
            "address",
        ]


class CarDriverSerializer(serializers.ModelSerializer):

    class Meta:
        model = Driver
        fields = [
            "name",
            "license_number",
        ]


class CarSerializer(serializers.ModelSerializer):
    owner = OwnerSerializer()  # one to one serializer
    drivers = CarDriverSerializer(many=True)  # many to many serializer

    class Meta:
        model = Car
        fields = ('name', 'type', 'owner', 'drivers')


class ThiefSerializer(serializers.ModelSerializer):
    cars = CarSerializer(many=True)  # one to many serializer

    class Meta:
        model = Thief
        fields = [
            "name",
            "address",
            "cars",
        ]


class DriverSerializer(serializers.ModelSerializer):
    cars = CarSerializer(many=True)  # many to many serializer

    class Meta:
        model = Driver
        fields = [
            "name",
            "license_number",
            "cars",
        ]
