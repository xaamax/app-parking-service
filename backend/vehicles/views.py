from rest_framework import viewsets

from vehicles.models import Vehicle, VehicleBrand, VehicleType
from vehicles.serializers import VehicleSerializer, VehicleBrandSerializer, VehicleTypeSerializer

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    
class VehicleBrandViewSet(viewsets.ModelViewSet):
    queryset = VehicleBrand.objects.all()
    serializer_class = VehicleBrandSerializer    
    
class VehicleTypeViewSet(viewsets.ModelViewSet):
    queryset = VehicleType.objects.all()
    serializer_class = VehicleTypeSerializer        