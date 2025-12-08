from dj_rql.filter_cls import AutoRQLFilterClass
from vehicles.models import VehicleBrand, VehicleType, Vehicle


class VehicleBrandFilterClass(AutoRQLFilterClass):
    MODEL = VehicleBrand


class VehicleTypeFilterClass(AutoRQLFilterClass):
    MODEL = VehicleType


class VehicleFilterClass(AutoRQLFilterClass):
    MODEL = Vehicle
