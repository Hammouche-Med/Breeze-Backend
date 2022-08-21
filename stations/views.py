from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import StationsSerializer
from .models import Station

from backend.permissions import  IsAdminUser, IsAuthenticated

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def overview(request):
    stationApi = {
        "List": "/api/station/all",
        "Details": "api/station/<str:pk>",
        "Create": "api/station/create",
        "Update": "api/station/edit/<str:pk>",
        "Delete": "api/station/delete/<str:pk>",
    }
    return Response(stationApi)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getStations(request):
    data = Station.objects.all()
    stationList = StationsSerializer(data, many=True)
    return Response(stationList.data)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getStationDetails(request, pk):
    data = Station.objects.get(id=pk)
    stationDetails = StationsSerializer(data, many=False)
    return Response(stationDetails.data)

@api_view(["POST"])
@permission_classes([IsAuthenticated, IsAdminUser])
def createStation(request):
    station = StationsSerializer(data=request.data)
    if station.is_valid():
        station.save()
    return Response("station saved successfully")

@api_view(["PUT"])
@permission_classes([IsAuthenticated, IsAdminUser])
def updateStation(request, pk):
    stationToUpdate = Station.objects.get(id=pk)
    data = StationsSerializer(instance=stationToUpdate,data=request.data)
    if data.is_valid():
        data.save()
    return Response("station updated successfully")

@api_view(["DELETE"])
@permission_classes([IsAuthenticated, IsAdminUser])
def deleteStation(request, pk):
    station = Station.objects.get(id=pk)
    station.delete()
    return Response("station deleted successfully")