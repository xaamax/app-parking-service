from django.contrib import admin

from vehicles.models import VehicleType, VehicleBrand, Vehicle


@admin.register(VehicleType)
class VehicleTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    search_fields = ['name']


@admin.register(VehicleBrand)
class VehicleBrandAdmin(admin.ModelAdmin):
    list_display = ['brand']
    search_fields = ['brand']


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ['lincense_plate', 'vehicle_brand', 'model', 'color']
    search_fields = ['lincense_plate', 'vehicle_brand', 'model']
    list_filter = ['vehicle_type']
