from django.db import models


class Client(models.Model):
    phone_number = models.CharField(max_length=15)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    cars = models.ManyToManyField('clients.ClientCar')



class ClientCar(models.Model):
    car = models.ForeignKey('cars.Car', on_delete=models.CASCADE)
    vin_code = models.CharField(max_length=200)
    plate_number = models.CharField(max_length=20)
    year = models.IntegerField()
