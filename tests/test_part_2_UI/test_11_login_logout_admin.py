import allure

from src.page_objects_UI.admin_page import AdminPage


@allure.title("Проверка входа под учеткой администратора и выход из учетки")
def test_login_logout_admin(browser):
    admin_page = AdminPage(browser)
    admin_page.go_to_administration()
    admin_page.verify_title("Administration")
    admin_page.login()
    admin_page.verify_title_with_wait(2, "Dashboard")
    admin_page.logout()
    admin_page.verify_title("Administration")
