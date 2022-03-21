from django.contrib import admin

from padam_django.apps.shift.forms.bus_shifts import BusShiftForm
from padam_django.apps.shift.models.bus_shifts import BusShift
from padam_django.apps.shift.models.bus_stops import BusStop


@admin.register(BusShift)
class BusShiftAdmin(admin.ModelAdmin):
    form = BusShiftForm
    list_display = ("bus", "driver")
    list_filter = ("bus", "driver")
    ordering = ("-pk",)


@admin.register(BusStop)
class BusStopAdmin(admin.ModelAdmin):
    pass
