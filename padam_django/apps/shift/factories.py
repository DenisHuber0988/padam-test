import datetime
import factory
from faker import Faker

from padam_django.apps.shift.models.bus_shifts import BusShift
from padam_django.apps.shift.models.bus_stops import BusStop

fake = Faker(['fr'])


class BusShiftFactory(factory.django.DjangoModelFactory):
    bus = factory.SubFactory('padam_django.apps.fleet.factories.BusFactory')
    driver = factory.SubFactory('padam_django.apps.fleet.factories.DriverFactory')
    start = factory.LazyFunction(datetime.datetime.now)
    end = factory.LazyFunction(datetime.datetime.now)

    class Meta:
        model = BusShift


class BusStopFactory(factory.django.DjangoModelFactory):
    place = factory.SubFactory('padam_django.apps.geography.factories.PlaceFactory')
    schedule = factory.LazyFunction(datetime.time)

    class Meta:
        model = BusStop
