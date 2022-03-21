from django import forms
from django.core.exceptions import ValidationError

from padam_django.apps.fleet.models.buses import Bus
from padam_django.apps.fleet.models.drivers import Driver
from padam_django.apps.shift.models.bus_shifts import BusShift
from padam_django.apps.shift.models.bus_stops import BusStop


class BusShiftForm(forms.ModelForm):
    bus = forms.ModelChoiceField(queryset=Bus.objects.filter(is_on_shift=False))
    driver = forms.ModelChoiceField(queryset=Driver.objects.filter(is_on_shift=False))
    stops = forms.ModelMultipleChoiceField(queryset=BusStop.objects.all())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance is not None:
            bus, driver = self.instance.bus, self.instance.driver
            # Update status to available when editing an existing shift, and put bus and driver
            self.instance.update_bus_driver_status(bus=bus, driver=driver, is_on_shift=False)
            self.fields['bus'].initial = bus
            self.fields['driver'].initial = driver

    def clean(self):
        """
        Do all the validation processus.
        """
        stops = self.cleaned_data.get('stops')
        driver = self.cleaned_data.get('driver')
        start = self.cleaned_data.get('start')
        end = self.cleaned_data.get('end')
        bus = self.cleaned_data.get('bus')

        if stops.count() < 2:
            raise ValidationError("Need at least two bus stops to create a shift.")

        if start > end:
            raise ValidationError("The shift needs to start before its end.")

        # Fetch all the schedules from the BusStop
        schedules = list(stops.values_list("schedule", flat=True))

        if any(start.time() > schedule for schedule in schedules):
            raise ValidationError("The shift starts after the departure time.")

        if any(end.time() < schedule for schedule in schedules):
            raise ValidationError("The shift ends before the arrival time.")

        # The form is valide, the bus and driver status can be put on shift duty.
        self.instance.update_bus_driver_status(bus=bus, driver=driver, is_on_shift=True)

    class Meta:
        model = BusShift
        fields = ("bus", "driver", "stops", "start", "end")
