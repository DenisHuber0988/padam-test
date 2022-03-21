from django.contrib import admin

from padam_django.apps.geography.models.places import Place


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    pass
