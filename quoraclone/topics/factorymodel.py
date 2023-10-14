import factory
from faker import Faker
from topics.models import Topic
from authentication.factorymodel import UserFactory

fake = Faker()

class TopicFactory(factory.django.DjangoModelFactory):
    title = factory.LazyAttribute(lambda _: fake.text(max_nb_chars=100))
    description = factory.LazyAttribute(lambda _: fake.text())
    creator = factory.SubFactory(UserFactory)   
    class Meta:
        model = Topic
        