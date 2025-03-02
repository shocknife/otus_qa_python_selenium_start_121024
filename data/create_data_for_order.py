from faker import Faker

fake = Faker()


class CreateDataForOrder:
    def __init__(
        self,
        firstname=None,
        lastname=None,
        street_address_1=None,
        city=None,
        country_code=None,
        area_code=None,
        email=None,
        telephone=None,
        product_id=None,
        quantity=None,
        payment_method=None,
        shipping_method=None,
    ):
        self.firstname = firstname
        self.lastname = lastname
        self.street_address_1 = street_address_1
        self.city = city
        self.country_code = country_code
        self.area_code = area_code
        self.email = email
        self.telephone = telephone
        self.product_id = product_id
        self.quantity = quantity
        self.payment_method = payment_method
        self.shipping_method = shipping_method

    @staticmethod
    def create_random():
        firstname = fake.first_name()
        lastname = fake.last_name()
        street_address_1 = fake.street_address()
        city = fake.city()
        country_code = fake.random_int(min=100, max=999)
        area_code = fake.random_int(min=100, max=999)
        email = fake.email()
        telephone = fake.phone_number()
        product_id = "40"
        quantity = "1"
        payment_method = "cod.cod"
        shipping_method = "flat.flat"
        return (
            firstname,
            lastname,
            street_address_1,
            city,
            country_code,
            area_code,
            email,
            telephone,
            product_id,
            quantity,
            payment_method,
            shipping_method,
        )
