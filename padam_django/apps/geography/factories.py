import factory
from faker import Faker

from padam_django.apps.geography.models.places import Place


fake = Faker(['fr'])


class PlaceFactory(factory.django.DjangoModelFactory):
    name = factory.LazyFunction(fake.street_name)

    longitude = factory.LazyFunction(fake.longitude)
    latitude = factory.LazyFunction(fake.latitude)

    class Meta:
        model = Place
