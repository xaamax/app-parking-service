from rest_framework.permissions import IsAdminUser, DjangoModelPermissions
from rest_framework import viewsets
from core.permissions import IsOwnerOfVehicleOrRecord
from vehicles.filters import VehicleBrandFilterClass, VehicleTypeFilterClass, VehicleFilterClass
from vehicles.models import Vehicle, VehicleBrand, VehicleType
from vehicles.serializers import VehicleSerializer, VehicleBrandSerializer, VehicleTypeSerializer


class VehicleBrandViewSet(viewsets.ModelViewSet):
    queryset = VehicleBrand.objects.all()
    serializer_class = VehicleBrandSerializer
    rql_filter_class = VehicleBrandFilterClass
    permission_classes = [DjangoModelPermissions, IsAdminUser]


class VehicleTypeViewSet(viewsets.ModelViewSet):
    queryset = VehicleType.objects.all()
    serializer_class = VehicleTypeSerializer
    rql_filter_class = VehicleTypeFilterClass
    permission_classes = [DjangoModelPermissions, IsAdminUser]


class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    rql_filter_class = VehicleFilterClass
    permission_classes = [DjangoModelPermissions, IsOwnerOfVehicleOrRecord]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Vehicle.objects.all()
        return Vehicle.objects.filter(owner__user=user)
