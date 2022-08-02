from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import RegionSerializer
from .models import Region


@api_view(["GET"])
def overview(request):
    regionApi = {
        "List": "/api/region/all",
        "Details": "api/region/<str:pk>",
        "Create": "api/region/create",
        "Update": "api/region/edit/<str:pk>",
        "Delete": "api/region/delete/<str:pk>",
    }
    return Response(regionApi)

@api_view(["GET"])
def getRegions(request):
    data = Region.objects.all()
    regionList = RegionSerializer(data, many=True)
    return Response(regionList.data)

@api_view(["GET"])
def getRegionDetails(request, pk):
    data = Region.objects.get(id=pk)
    regionDetails = RegionSerializer(data, many=False)
    return Response(regionDetails.data)

@api_view(["POST"])
def createRegion(request):
    region = RegionSerializer(data=request.data)
    if region.is_valid():
        region.save()
    return Response("region saved successfully")

@api_view(["PUT"])
def updateRegion(request, pk):
    regionToUpdate = Region.objects.get(id=pk)
    data = RegionSerializer(instance=regionToUpdate,data=request.data)
    if data.is_valid():
        data.save()
    return Response("region updated successfully")

@api_view(["DELETE"])
def deleteRegion(request, pk):
    region = Region.objects.get(id=pk)
    region.delete()
    return Response("region deleted successfully")