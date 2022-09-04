from django.urls import path
from . import views

urlpatterns = [
    path("staion-production/", views.overview, name="station-production-api-overview"),
    path("staion-production/all", views.getStation_Production, name="station-production-list"),
    path("staion-production/create", views.creategetStation_Production, name="station-production-create"),
    path("staion-production/<str:pk>", views.getgetStation_ProductionDetails, name="station-production-details"),
    path("staion-production/edit/<str:pk>", views.updategetStation_Production, name="station-production-update"),
    path("staion-production/delete/<str:pk>", views.deletegetStation_Production, name="station-production-delete"),

    path("rapport/jour/<str:pk>", views.getDayReport, name="day-production-report"),

]