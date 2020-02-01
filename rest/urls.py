from django.urls import path
from . import views


app_name = 'rest'
urlpatterns = [
    path('index_car', views.index_car, name='index_car'),
    path('owner_car', views.owner_car, name='owner_car'),
    path('index_thief', views.index_thief, name='index_thief'),
    path('thief_car', views.thief_car, name='thief_car'),
    path('driver_car', views.driver_car, name='driver_car'),
    path('car', views.car, name='car'),
]