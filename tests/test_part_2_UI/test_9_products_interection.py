import allure

from data.create_product import CreateProductData
from src.page_objects_UI.admin_page import AdminPage, AddProductPage, AdminProductPage
from src.page_objects_UI.base_page import BasePage


@allure.title("Добавление нового товара")
def test_add_product(browser):
    admin_panel = AdminPage(browser)
    add_product = AddProductPage(browser)
    data = CreateProductData.create_random()
    product = AdminProductPage(browser)
    admin_panel.go_to_administration()
    admin_panel.login()
    admin_panel.open_product_page()
    product.step_add_new_product(browser)
    add_product.send_required_fields_general_tab(data)
    add_product.send_required_fields_model_tab(data)
    add_product.send_required_fields_seo_tab(data)
    add_product.safe_product(browser)
    assert add_product.save_assert() == "Success: You have modified products!"
    add_product.back_to_products(browser)
    product.filter_name(data)
    assert data.name in product.assert_product()


@allure.title("Удаление созданного товара")
def test_dell_product(browser, create_new_product):
    browser = create_new_product[0]
    data = create_new_product[1]
    alert_delete = BasePage(browser)
    product = AdminProductPage(browser)
    product.delete_product(data.name)
    alert_delete.alert_window()
    assert data.name not in product.assert_product()
