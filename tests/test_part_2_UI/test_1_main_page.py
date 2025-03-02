import allure
from src.page_objects_UI.main_page import MainPage


@allure.title("Проверка элементов на главной странице сервиса")
def test_main_page(browser):
    main_page = MainPage(browser)
    main_page.open_main_page()
    main_page.verify_title(main_page.TITLE)
    main_page.verify_quantity_cards(4)
    main_page.verify_quantity_banner(2)
    main_page.check_privacy_policy()
