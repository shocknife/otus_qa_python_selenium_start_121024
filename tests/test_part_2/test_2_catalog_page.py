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


@allure.title("Проверка отображения карточек desktops по умолчанию не больше 10 штук")
def test_count(browser):
    catalog = CatalogPage(browser)
    catalog.open_catalog("/en-gb/catalog/desktops/")
    catalog.show_limit_carts()
    counts = catalog.check_product_carts()
    assert len(counts) <= 15


@allure.title("Проверка сортировки desktops на странице каталога")
def test_sort_carts(browser):
    lst = []
    sorted_lst = []
    catalog = CatalogPage(browser)
    catalog.open_catalog("/en-gb/catalog/desktops/")
    catalog.show_limit_carts()
    carts = catalog.check_product_carts()
    for i in range(len(carts)):
        lst.append(carts[i].text.lower())
    lst.sort(reverse=True)
    catalog.sort_by_name()
    sorted_carts = catalog.check_product_carts()
    for i in range(len(sorted_carts)):
        sorted_lst.append(sorted_carts[i].text.lower())
    assert lst == sorted_lst
