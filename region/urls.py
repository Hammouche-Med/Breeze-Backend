from django.urls import path
from . import views

urlpatterns = [
    path("region/", views.overview, name="region-api-overview"),
    path("region/all", views.getRegions, name="region-list"),
    path("region/create", views.createRegion, name="region-create"),
    path("region/<str:pk>", views.getRegionDetails, name="region-details"),
    path("region/edit/<str:pk>", views.updateRegion, name="region-update"),
    path("region/delete/<str:pk>", views.deleteRegion, name="region-delete"),
]