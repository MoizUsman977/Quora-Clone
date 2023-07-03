import factory
from faker import Faker
from authentication.models import User

fake = Faker()

class UserFactory(factory.django.DjangoModelFactory):
    email = factory.LazyAttribute(lambda _: fake.email())
    password = factory.PostGenerationMethodCall('set_password', 'password')
    username = factory.LazyAttribute(lambda _: fake.user_name())
    age = factory.LazyAttribute(lambda _: fake.random_int(min=18, max=60))
    gender = factory.Iterator(['M', 'F'])
    
    class Meta:
        model = User
