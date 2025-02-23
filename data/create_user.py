import random

from faker import Faker

fake = Faker("Ru-ru")


class CreateUserData:
    def __init__(self, name=None, lastname=None, email=None, password=None):
        self.name = name
        self.lastname = lastname
        self.email = email
        self.password = password

    @staticmethod
    def create_random():
        name = fake.first_name()
        lastname = fake.last_name()
        email = fake.email()
        password = f"ANrb{random.randint(0, 1000)}"
        return CreateUserData(name, lastname, email, password)
