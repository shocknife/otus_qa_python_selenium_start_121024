from faker import Faker

fake = Faker("Ru-ru")


class CreateProductData:
    def __init__(self, name=None, meta_tag=None, model=None):
        self.name = name
        self.meta_tag = meta_tag
        self.model = model

    @staticmethod
    def create_random():
        name = fake.word()
        meta_tag = fake.word()
        model = fake.word()
        return CreateProductData(name, meta_tag, model)
