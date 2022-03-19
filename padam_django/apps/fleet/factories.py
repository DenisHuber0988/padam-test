import factory
from faker import Faker

from .models import Bus, Driver

fake = Faker(['fr'])


class DriverFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory('padam_django.apps.users.factories.UserFactory')

    class Meta:
        model = Driver


class BusFactory(factory.django.DjangoModelFactory):
    licence_plate = factory.LazyFunction(fake.license_plate)

    class Meta:
        model = Bus
