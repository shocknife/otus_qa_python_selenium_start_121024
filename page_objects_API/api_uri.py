from enum import Enum


class ApiUri(str, Enum):
    LOGIN = "api/account/login"
    CART = "api/cart"
    ORDER = "api/order"  # not tested
    CURRENCY = "api/currency"  # not tested

    def __str__(self):
        return self.value
