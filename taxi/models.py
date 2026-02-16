from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.urls import reverse


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)

    class Meta:
        ordering = ("name",)

    def __str__(self) -> CharField:
        return self.name


class Driver(AbstractUser):
    license_number = models.CharField(max_length=255, unique=True)


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(
        Manufacturer, on_delete=models.CASCADE, related_name="cars"
    )
    drivers = models.ManyToManyField(Driver, related_name="cars")
