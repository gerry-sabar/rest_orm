from django.db import models


# Create your models here.
class Owner(models.Model):

    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True, null=True)


class Thief(models.Model):

    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True, null=True)


class Driver(models.Model):

    name = models.CharField(max_length=255)
    license_number = models.CharField(max_length=255)


class Car(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255, blank=True, null=True)
    owner = models.OneToOneField(
        Owner,
        on_delete=models.CASCADE,
        related_name='car'
    )
    thief = models.ForeignKey(
        Thief,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='cars'
    )
    drivers = models.ManyToManyField(
        Driver,
        related_name='cars'
    )
