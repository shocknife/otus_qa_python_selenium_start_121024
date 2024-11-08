from page_objects.main_page import MainPage


def test_currency_change(browser):
    currency_main_page = MainPage(browser)
    currency_main_page.open()
    currency_main_page.check_current_prices()
    currency_main_page.change_currency_to_eur()
    currency_main_page.verify_currency_changed_to_eur()
    currency_main_page.change_currency_to_gbp()
    currency_main_page.verify_currency_changed_to_gbp()
