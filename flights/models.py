from django.db import models
from django.forms import ModelForm


# Create your models here.

class Airport(models.Model):
    code = models.CharField(max_length=3 )
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.city} ({self.code})"

class AirportModelForm(ModelForm):
    class Meta:
        model  = Airport
        fields = '__all__' 


    
