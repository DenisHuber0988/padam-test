from django.db import models


class BusStop(models.Model):
    place = models.ForeignKey('geography.Place', on_delete=models.RESTRICT)
    schedule = models.TimeField()

    def __str__(self):
        """Display the name of the place for more readability"""
        return f"Stop : {self.place.name} at {self.schedule}"
