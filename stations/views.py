from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StationsSerializer
from .models import Station


@api_view(["GET"])
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
def getStations(request):
    data = Station.objects.all()
    stationList = StationsSerializer(data, many=True)
    return Response(stationList.data)

@api_view(["GET"])
def getStationDetails(request, pk):
    data = Station.objects.get(id=pk)
    stationDetails = StationsSerializer(data, many=False)
    return Response(stationDetails.data)

@api_view(["POST"])
def createStation(request):
    station = StationsSerializer(data=request.data)
    if station.is_valid():
        station.save()
    return Response("station saved successfully")

@api_view(["PUT"])
def updateStation(request, pk):
    stationToUpdate = Station.objects.get(id=pk)
    data = StationsSerializer(instance=stationToUpdate,data=request.data)
    if data.is_valid():
        data.save()
    return Response("station updated successfully")

@api_view(["DELETE"])
def deleteStation(request, pk):
    station = Station.objects.get(id=pk)
    station.delete()
    return Response("station deleted successfully")