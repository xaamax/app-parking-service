from django.apps import AppConfig


class VehiclesConfig(AppConfig):
    name = 'vehicles'
    verbose_name = 'Veículo'

    def ready(self):
        import vehicles.signals  # noqa: F401
