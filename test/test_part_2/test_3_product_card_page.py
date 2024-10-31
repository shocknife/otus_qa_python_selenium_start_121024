from page_objects.product_card_page import ProductPage


def test_page_product(browser):
    product_page = ProductPage(browser)
    product_page.open_main_page()
    product_page.select_first_product()
    product_page.verify_title(product_page.TITLE)
    product_page.check_elements()
