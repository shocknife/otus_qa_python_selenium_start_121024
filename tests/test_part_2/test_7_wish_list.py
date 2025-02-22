import allure

from page_objects.main_page import MainPage
from page_objects.register_user_page import RegistrationPage


@allure.title("Проверка работоспособности wish list")
def test_wish_list_not_register(browser):
    main_page = MainPage(browser)
    main_page.open_main_page()
    main_page._find_element(locator=RegistrationPage.WISH_LIST).click()
    assert (
        main_page._find_element(locator=RegistrationPage.NEW_CUSTOMER).text
        == "New Customer"
    )


@allure.title("Проверка перехода на страницу wish list")
def test_wish_list_with_register_user(browser, create_new_user):
    browser = create_new_user.driver
    main_page = MainPage(browser)
    main_page.open_main_page()
    main_page._find_element(locator=RegistrationPage.WISH_LIST).click()
    main_page._find_element(locator=RegistrationPage.WISH_LIST_TOTAL)
    assert (
        main_page._find_element(locator=RegistrationPage.WISH_LIST_ACCOUNT).text
        == "My Wishlist"
    )
