from django.shortcuts import render
from .models import Wash, Tire, Service


def home(request):
    return render(request, "website/home.html")


def wash(request):
    wh = Wash.objects.all()
    context = {'wash': wh}
    return render(request, 'website/wash.html', context)


def tire_service(request):
    tr = Tire.objects.all()
    context = {'tire': tr}
    return render(request, 'website/tire_service.html', context)


def service(request):
    sr = Service.objects.all()
    context = {'service': sr}
    return render(request, 'website/service.html', context)
