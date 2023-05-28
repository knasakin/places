from django.urls import path
from .views import index, PlaceListView, PlaceCreateView

urlpatterns = [
    path('', index, name='index'),
    path('places/', PlaceListView.as_view(), name='places'),
    path('add/', PlaceCreateView.as_view(), name='add'),
]
