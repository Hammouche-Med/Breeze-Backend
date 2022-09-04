import imp
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from production.models import Production
from observation.models import Observation

from stations.models import Station
from .serializers import Station_ProductionSerializer
from .serializers import ReportSerializer
from .models import Station_Production

from backend.permissions import  IsAdminUser, IsAuthenticated

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def overview(request):
    Station_ProductionApi = {
        "List": "/api/station/all",
        "Details": "api/station/<str:pk>",
        "Create": "api/station/create",
        "Update": "api/station/edit/<str:pk>",
        "Delete": "api/station/delete/<str:pk>",
    }
    return Response(Station_ProductionApi)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getStation_Production(request):
    data = Station_Production.objects.all()
    stationProductionList = Station_ProductionSerializer(data, many=True)
    return Response(stationProductionList.data)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getgetStation_ProductionDetails(request, pk):
    data = Station_Production.objects.get(id=pk)
    stationProductionDetails = Station_ProductionSerializer(data, many=False)
    return Response(stationProductionDetails.data)

@api_view(["POST"])
@permission_classes([IsAuthenticated, IsAdminUser])
def creategetStation_Production(request):
    stationProduction = Station_ProductionSerializer(data=request.data)
    if stationProduction.is_valid():
        stationProduction.save()
    return Response("stationProduction saved successfully")

@api_view(["PUT"])
@permission_classes([IsAuthenticated, IsAdminUser])
def updategetStation_Production(request, pk):
    stationProductionToUpdate = Station_Production.objects.get(id=pk)
    data = Station_ProductionSerializer(instance=stationProductionToUpdate,data=request.data)
    if data.is_valid():
        data.save()
    return Response("stationProduction updated successfully")

@api_view(["DELETE"])
@permission_classes([IsAuthenticated, IsAdminUser])
def deletegetStation_Production(request, pk):
    stationProduction= Station_Production.objects.get(id=pk)
    stationProduction.delete()
    return Response("stationProduction deleted successfully")




@api_view(["POST"])
@permission_classes([IsAuthenticated])
def getDayReport(request, pk):
    print("--------",pk, request.data["date"])
    date = request.data["date"]
    station = Station.objects.get(id=pk)
    obs = Observation.objects.raw("SELECT * FROM Observation_observation WHERE rec_date >=" + date+ " AND rec_date <="+date)
    for bb in Observation.objects.raw("SELECT * FROM Observation_observation WHERE FORMAT(rec_date,'YYYY-MM-DD')=" + date):
        print(bb)
    print("--*****-",obs)
    return Response(True)