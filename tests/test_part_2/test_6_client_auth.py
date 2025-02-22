import allure

from page_objects.main_page import MainPage
from page_objects.register_user_page import RegistrationPage


@allure.title("Проверка аутентификации нового пользователя")
def test_auth(create_new_user, browser):
    browser = create_new_user.driver
    browser.get(browser.base_url)
    main = MainPage(browser)
    reg_page = RegistrationPage(browser)
    reg_page.login_user(create_new_user)
    main.logout_user()
    logout = reg_page.logout_assert()
    assert logout == "Account Logout"
    main.start_login_user()
    reg_page.login_user(create_new_user)
    assert (
        reg_page.wait_find_element(RegistrationPage.LOGIN_ASSERT).text == "My Account"
    )
