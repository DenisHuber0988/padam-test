import factory
from faker import Faker

from padam_django.apps.fleet.models.buses import Bus
from padam_django.apps.fleet.models.drivers import Driver

fake = Faker(['fr'])


class DriverFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory('padam_django.apps.users.factories.UserFactory')

    class Meta:
        model = Driver


class BusFactory(factory.django.DjangoModelFactory):
    licence_plate = factory.LazyFunction(fake.license_plate)

    class Meta:
        model = Bus
