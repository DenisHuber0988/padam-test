from django.db import models


class Bus(models.Model):
    licence_plate = models.CharField("Name of the bus", max_length=10)
    is_on_shift = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Buses"

    def __str__(self):
        return f"Bus: {self.licence_plate} (id: {self.pk})"
