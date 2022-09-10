from django.urls import path
from . import views

urlpatterns = [
    path("observation/", views.overview, name="observation-api-overview"),
    path("observation/all", views.getObservations, name="observation-list"),
    path("observation/all/delete", views.deleteAllObservation, name="observation-del-all"),
    path("observation/create", views.createObservation, name="observation-create"),
    path("observation/delete/<str:pk>", views.deleteObservation, name="observation-delete"),
    path("observation/<str:pk>", views.getObservationDetails, name="observation-details"),
]