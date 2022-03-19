import factory
from faker import Faker

from .models import User


fake = Faker(['fr'])


class UserFactory(factory.django.DjangoModelFactory):
    username = factory.LazyFunction(fake.user_name)
    email = factory.LazyFunction(fake.ascii_email)
    first_name = factory.LazyFunction(fake.first_name)
    last_name = factory.LazyFunction(fake.last_name)

    class Meta:
        model = User
