from faker import Faker

fake_ru = Faker("Ru-ru")
fake_eng = Faker("En-us")


class CreateProductData:
    def __init__(self, name=None, meta_tag=None, model=None, seo=None):
        self.name = name
        self.meta_tag = meta_tag
        self.model = model
        self.seo = seo

    @staticmethod
    def create_random():
        name = fake_ru.word()
        meta_tag = fake_ru.word()
        model = fake_ru.word()
        seo = fake_eng.word()
        return CreateProductData(name, meta_tag, model, seo)
