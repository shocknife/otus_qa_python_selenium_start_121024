import allure

from page_objects.main_page import MainPage


@allure.title("Проверка изменения отображения цены в валюте на главной странице")
def test_currency_change(browser):
    currency_on_page = MainPage(browser)
    currency_on_page.open_main_page()
    currency_on_page.check_current_prices()
    currency_on_page.change_currency_to_eur()
    currency_on_page.verify_currency_changed_to_eur()
    currency_on_page.change_currency_to_gbp()
    currency_on_page.verify_currency_changed_to_gbp()
