from django.db import transaction
from django.db import models


class BusShift(models.Model):
    """
    Represents a shift a bus and driver will do.
    """
    bus = models.OneToOneField('fleet.Bus', on_delete=models.SET_NULL, null=True, blank=False,
                               related_name='bus')
    driver = models.OneToOneField('fleet.Driver', on_delete=models.SET_NULL, null=True, blank=False,
                                  related_name='driver')
    stops = models.ManyToManyField('shift.BusStop', related_name='stops', blank=False)
    # Move start/end in a Shift class
    start = models.DateTimeField("Start of the shift")
    end = models.DateTimeField("End of the shift")

    @staticmethod
    def update_bus_driver_status(bus, driver, is_on_shift):
        """
        Update driver and bus on availability inside the transaction block to ensure
        the consistency of the database.
        """
        with transaction.atomic():
            bus.is_on_shift = is_on_shift
            driver.is_on_shift = is_on_shift
            bus.save()
            driver.save()

    def bus_and_driver_available(self):
        """
        When a shift is over (done or after end time) update the status of bus and driver
        to available. (Script or action )
        """
        return self.update_bus_driver_status(self.bus, self.driver, False)

    def delete(self):
        """When deleting a shift, put the bus and the driver available."""
        self.update_bus_driver_status(self.bus, self.driver, False)
        return super().delete()
