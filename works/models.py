from django.db import models


class Serv(models.Model):
    time = models.CharField(max_length=5)
    data = models.DateField()
    instruction = models.CharField(max_length=200)


class Work(models.Model):
    price = models.IntegerField()
    instruction = models.CharField(max_length=100)
    time = models.TimeField(auto_now_add=True, blank=True)

