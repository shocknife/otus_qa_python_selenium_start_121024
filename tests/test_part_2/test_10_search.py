import allure

from page_objects.main_page import MainPage


@allure.title("Тестирование поиска товара через строку поиска")
def test_search(browser, create_new_product):
    browser = create_new_product[0]
    data = create_new_product[1]
    main = MainPage(browser)
    main.open_main_page()
    main.search_product(data)
    assert data.name in main.assert_search_product()
