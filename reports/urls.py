from django.urls import path
from . import views

urlpatterns = [
    path("report/all", views.overview, name="station-production-api-overview"),

    path("report/day/<str:pk>", views.getDayReport, name="day-production-report"),
    path("report/month/<str:pk>", views.getMonthReport, name="month-production-report"),
    path("report/year/<str:pk>", views.getYearReport, name="year-production-report"),
    path("report/all/day", views.getTotalDayReport, name="day-production-total-report"),
    path("report/all/month", views.getTotalMonthReport, name="month-production-total-report"),
    path("report/all/year", views.getTotalYearReport, name="year-production-total-report"),

]