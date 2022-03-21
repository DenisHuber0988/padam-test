from django.contrib import admin

from padam_django.apps.fleet.models.buses import Bus
from padam_django.apps.fleet.models.drivers import Driver


@admin.register(Bus)
class BusAdmin(admin.ModelAdmin):
    pass


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    pass
