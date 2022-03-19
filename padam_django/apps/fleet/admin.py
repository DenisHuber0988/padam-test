from django.contrib import admin

from .models import Bus, Driver


@admin.register(Bus)
class BusAdmin(admin.ModelAdmin):
    pass


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    pass
