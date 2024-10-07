from django.db import models


class Wash(models.Model):
    body_type = models.CharField(max_length=100)
    instructions = models.CharField(max_length=150)
    price = models.IntegerField()


class Tire(models.Model):
    instructions = models.CharField(max_length=150)
    wheel_size = models.CharField(max_length=50)
    price = models.IntegerField()
    trac = models.BooleanField()


class Service(models.Model):
    instructions = models.CharField(max_length=150)
    price = models.IntegerField()
