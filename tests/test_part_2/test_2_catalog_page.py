import allure

from page_objects.catalog_page import CatalogPage


@allure.title("Проверка элементов на странице каталога")
def test_page_catalog(browser):
    catalog_page = CatalogPage(browser)
    catalog_page.open_main_page_for_catalog()
    catalog_page.select_tablets()
    catalog_page.verify_title(catalog_page.TITLE)
    catalog_page.verify_catalog_url()
    catalog_page.check_elements()
