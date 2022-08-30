from django.urls import path
from . import views

urlpatterns = [
    path("observation/", views.overview, name="observation-api-overview"),
    path("observation/all", views.getObservations, name="observation-list"),
    path("observation/create", views.createObservation, name="observation-create"),
    path("observation/<str:pk>", views.getObservationDetails, name="observation-details"),
]