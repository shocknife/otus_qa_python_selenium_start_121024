import allure

from src.page_objects_UI.admin_page import AdminPage


@allure.title("Проверка элементов на странице входа в администратора")
def test_admin_page(browser):
    admin_page = AdminPage(browser)
    admin_page.go_to_administration()
    admin_page.verify_title("Administration")
    admin_page.check_elements()
