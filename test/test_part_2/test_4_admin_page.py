from page_objects.admin_page import AdminPage


def test_admin_page(browser):
    admin_page = AdminPage(browser)
    admin_page.go_to_administration()
    admin_page.verify_title("Administration")
    admin_page.check_elements()
