import allure
from selenium.webdriver.common.by import By
from src.page_objects_UI.base_page import BasePage
from src.page_objects_UI.main_page import MainPage


class CatalogPage(BasePage):
    TITLE = "Tablets"
    TABLETS_LINK = (By.LINK_TEXT, "Tablets")
    PRODUCT_THUMB = (By.XPATH, "//*[@class='product-thumb']")
    COLUMN_LEFT = (By.ID, "column-left")
    BUTTON_LIST = (By.ID, "button-list")
    BUTTON_GRID = (By.ID, "button-grid")
    INPUT_SORT = (By.ID, "input-sort")
    SORT_NAME_DESC_Z_A = (By.XPATH, "//*[text()='Name (Z - A)']")
    SHOW = (By.XPATH, "//*[@id='input-limit']")
    SHOW_LIMIT_25 = (By.XPATH, "//*[@id='input-limit']/option[text()='25']")

    @allure.step("Выполняется вход на страницу")
    def open_main_page_for_catalog(self):
        super().open(self.browser.base_url)

    @allure.step("Выбора категории 'Планшеты'")
    def select_tablets(self):
        self.find_element(*self.TABLETS_LINK).click()

    @allure.step("Проверка элементов на странице каталога")
    def check_elements(self):
        self.check_element_present(*self.PRODUCT_THUMB)
        self.check_element_present(*self.COLUMN_LEFT)
        self.check_element_present(*self.BUTTON_LIST)
        self.check_element_present(*self.BUTTON_GRID)
        self.check_element_present(*self.INPUT_SORT)

    @allure.step("Проверка наличия слова 'catalog' в адресной строке")
    def verify_catalog_url(self):
        assert (
            "catalog" in self.browser.current_url
        ), "URL страницы не содержит 'catalog'"

    @allure.step("Проверка количества карточек на странице каталога")
    def check_product_carts(self):
        return self.find_elements(*self.PRODUCT_THUMB)

    @allure.step("Установка количества отображаемых карточек")
    def show_limit_carts(self):
        self.find_element(*self.SHOW).click()
        self.find_element(*self.SHOW_LIMIT_25).click()

    @allure.step("Выполнение сортировки на странице каталога")
    def sort_by_name(self):
        self.find_element(*self.INPUT_SORT).click()
        self.find_element(*self.SORT_NAME_DESC_Z_A).click()

    @allure.step("Выполняется вход на страницу")
    def open_catalog(self, uri=None):
        super().open(self.browser.base_url + uri)


class VerifyPrice(CatalogPage, MainPage):
    SELECT_DESKTOPS = (
        By.XPATH,
        "//a[@data-bs-toggle='dropdown' and text()='Desktops']",
    )
    SHOW_ALL_DESKTOPS = (
        By.XPATH,
        "//*[@class='see-all' and text()='Show All Desktops']",
    )

    @allure.step("Выполнение перехода на страницу каталога")
    def go_to_catalog(self):
        MainPage.open_main_page(self)
        self.find_element(*self.SELECT_DESKTOPS).click()
        self.find_element(*self.SHOW_ALL_DESKTOPS).click()
        self.verify_catalog_url()
