from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import AirportForm
from .models import Airport,AirportModelForm
import os 

# Create your views here.

def index(request):
    return render(request, "flights/index.html")


def form_without_model(request):
    if request.method == "POST":
        code    = request.POST["code"]
        city    = request.POST["city"]
        A       = Airport(code=code, city=city)
        A.save() 
        return render(request, "flights/without_model.html",{
            "form": AirportForm,
            "airport": Airport.objects.last()
        }) 
    else:
        return render(request, "flights/without_model.html",{
            "form": AirportForm
        })
    
def form_with_model(request):
    if request.method == "POST":
        form    = AirportModelForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, "flights/with_model.html",{
            "form": AirportModelForm,
            "airport": Airport.objects.last()
        }) 
    else:
        return render(request, "flights/with_model.html",{
            "form": AirportModelForm
        })