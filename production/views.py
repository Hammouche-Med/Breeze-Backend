from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import ProductionSerializer
from .models import Production

from backend.permissions import  IsAdminUser, IsAuthenticated


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def overview(request):
    ProductionApi = {
        "List": "/api/production/all",
        "Details": "api/production/<str:pk>",
        "Create": "api/production/create",
        "Update": "api/production/edit/<str:pk>",
        "Delete": "api/production/delete/<str:pk>",
    }
    return Response(ProductionApi)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getProductions(request):
    data = Production.objects.all()
    productionList = ProductionSerializer(data, many=True)
    return Response(productionList.data)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getProductionDetails(request, pk):
    data = Production.objects.get(id=pk)
    productionDetails = ProductionSerializer(data, many=False)
    return Response(productionDetails.data)

@api_view(["POST"])
@permission_classes([IsAuthenticated, IsAdminUser])
def createProduction(request):
    production = ProductionSerializer(data=request.data)
    if production.is_valid():
        production.save()
    return Response("production saved successfully")

@api_view(["PUT"])
@permission_classes([IsAuthenticated, IsAdminUser])
def updateProduction(request, pk):
    productionToUpdate = Production.objects.get(id=pk)
    data = ProductionSerializer(instance=productionToUpdate,data=request.data)
    if data.is_valid():
        data.save()
    return Response("production updated successfully")

@api_view(["DELETE"])
@permission_classes([IsAuthenticated, IsAdminUser])
def deleteProduction(request, pk):
    production = Production.objects.get(id=pk)
    production.delete()
    return Response("production deleted successfully")