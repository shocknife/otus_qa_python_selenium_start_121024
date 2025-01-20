import allure

from page_objects.cart_page import CartPage


@allure.title("Проверка добавления товара в корзину, и проверка что они там есть")
def test_add_item_in_cart(browser):
    cart_item = CartPage(browser)
    cart_item.go_to_main_page()
    product_to_add = cart_item.add_item_to_cart(4)
    cart_item.verify_product_in_cart(product_to_add)
