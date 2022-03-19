from django.contrib import admin

from .models import BusShift, BusStop


@admin.register(BusShift)
class BusShiftAdmin(admin.ModelAdmin):
    pass


@admin.register(BusStop)
class BusStopAdmin(admin.ModelAdmin):
    pass
