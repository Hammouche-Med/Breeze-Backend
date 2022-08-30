from django.urls import path
from . import views

urlpatterns = [
    path("production/", views.overview, name="production-api-overview"),
    path("production/all", views.getProductions, name="production-list"),
    path("production/create", views.createProduction, name="production-create"),
    path("production/<str:pk>", views.getProductionDetails, name="production-details"),
    path("production/edit/<str:pk>", views.updateProduction, name="production-update"),
    path("production/delete/<str:pk>", views.deleteProduction, name="production-delete"),
]