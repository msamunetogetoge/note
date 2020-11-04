from django import forms


class AirportForm(forms.Form):
    code = forms.CharField(max_length=3 )
    city = forms.CharField(max_length=64 )