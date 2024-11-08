from page_objects.catalog_page import VerifyPrice


def test_page_catalog(browser):
    currency_catalog_page = VerifyPrice(browser)
    currency_catalog_page.go_to_catalog()
    currency_catalog_page.check_current_prices()
    currency_catalog_page.change_currency_to_eur()
    currency_catalog_page.verify_currency_changed_to_eur()
    currency_catalog_page.change_currency_to_gbp()
    currency_catalog_page.verify_currency_changed_to_gbp()