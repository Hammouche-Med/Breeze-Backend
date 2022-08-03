from django.urls import path
from . import views

urlpatterns = [
    path("station/", views.overview, name="station-api-overview"),
    path("station/all", views.getStations, name="station-list"),
    path("station/create", views.createStation, name="station-create"),
    path("station/<str:pk>", views.getStationDetails, name="station-details"),
    path("station/edit/<str:pk>", views.updateStation, name="station-update"),
    path("station/delete/<str:pk>", views.deleteStation, name="station-delete"),
]