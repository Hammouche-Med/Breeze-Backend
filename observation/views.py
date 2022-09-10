from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import ObservationSerializer
from .models import Observation

from backend.permissions import  IsAdminUser, IsAuthenticated


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def overview(request):
    observationApi = {
        "List": "/api/observation/all",
        "Details": "api/observation/<str:pk>",
        "Create": "api/observation/create",
    }
    return Response(observationApi)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getObservations(request):
    data = Observation.objects.all()
    observationList = ObservationSerializer(data, many=True)
    return Response(observationList.data)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getObservationDetails(request, pk):
    data = Observation.objects.get(id=pk)
    observationDetails = ObservationSerializer(data, many=False)
    return Response(observationDetails.data)

@api_view(["POST"])
@permission_classes([IsAuthenticated, IsAdminUser])
def createObservation(request):
    observation = ObservationSerializer(data=request.data)
    if observation.is_valid():
        observation.save()
    return Response("observation saved successfully")

# @api_view(["PUT"])
# @permission_classes([IsAuthenticated, IsAdminUser])
# def updateObservation(request, pk):
#     observationToUpdate = Observation.objects.get(id=pk)
#     data = ObservationSerializer(instance=observationToUpdate,data=request.data)
#     if data.is_valid():
#         data.save()
#     return Response("observation updated successfully")

@api_view(["DELETE"])
@permission_classes([IsAuthenticated, IsAdminUser])
def deleteObservation(request, pk):
    observation = Observation.objects.get(id=pk)
    observation.delete()
    return Response("observation deleted successfully")

    
@api_view(["DELETE"])
def deleteAllObservation(request):
    observation = Observation.objects.all()
    observation.delete()
    return Response("observation deleted successfully")

