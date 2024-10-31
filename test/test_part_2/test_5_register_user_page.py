from page_objects.register_user_page import RegistrationPage


def test_page_register_users(browser):
    reg_user_page = RegistrationPage(browser)
    reg_user_page.open()
    reg_user_page.verify_title("Register Account")
    reg_user_page.check_registration_user_form()
