from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from rest.models import *
from rest.serializers import *


# Create your views here.
def index_car(request):
    cars = Car.objects.all()
    serializer_car = CarSerializer(cars, many=True)
    json_renderer = JSONRenderer()
    json_car = json_renderer.render(serializer_car.data)
    return HttpResponse(json_car, 200)


def index_thief(request):
    thieves = Thief.objects.all()
    serializer_thief = ThiefSerializer(thieves, many=True)
    json_renderer = JSONRenderer()
    json_thief = json_renderer.render(serializer_thief.data)
    return HttpResponse(json_thief, 200)


def owner_car(request):
    car = Car.objects.get(id=1)
    serializer_car = CarSerializer(car)
    json_renderer = JSONRenderer()
    json_car = json_renderer.render(serializer_car.data)
    return HttpResponse(json_car, 200)


def thief_car(request):
    thief = Thief.objects.get(id=1)
    serializer_thief = ThiefSerializer(thief)
    json_renderer = JSONRenderer()
    json_thief = json_renderer.render(serializer_thief.data)
    return HttpResponse(json_thief, 200)


def driver_car(request):
    driver = Driver.objects.get(name='driver 2')
    serializer_driver = DriverSerializer(driver)
    json_renderer = JSONRenderer()
    json_driver = json_renderer.render(serializer_driver.data)
    return HttpResponse(json_driver, 200)


def car(request):
    car = Car.objects.get(id=1)
    #print(vars(car.drivers.all()))
    #return HttpResponse('')
    serializer_car = CarSerializer(car)
    json_renderer = JSONRenderer()
    json_car = json_renderer.render(serializer_car.data)
    return HttpResponse(json_car, 200)
