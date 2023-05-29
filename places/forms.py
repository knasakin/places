from django.forms import ModelForm
from .models import Place
from django.contrib.gis import forms


class PlaceForm(ModelForm):
    class Meta:
        model = Place
        fields = ('location', 'name', 'comment')
        widgets = {
            'location': forms.OSMWidget(attrs={
                'default_lat': 43.6028,
                'default_lon': 39.7342
            })
        }
