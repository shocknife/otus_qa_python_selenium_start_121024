import allure

from src.page_objects_UI.register_user_page import RegistrationPage


@allure.title("Проверка элементов на странице регистрации пользователя")
def test_page_register_users(browser):
    reg_user_page = RegistrationPage(browser)
    reg_user_page.open_reg_user_page()
    reg_user_page.verify_title("Register Account")
    reg_user_page.check_registration_user_form()
