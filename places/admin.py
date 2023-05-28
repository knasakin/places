from django.contrib.gis import admin
from .models import Place
from leaflet.admin import LeafletGeoAdmin


class PlaceAdmin(LeafletGeoAdmin):
    list_display = ('name', 'location', 'comment')


admin.site.register(Place, PlaceAdmin)
