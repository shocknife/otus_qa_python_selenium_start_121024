import time

import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


from src.page_objects_UI.base_page import BasePage


class AdminPage(BasePage):
    USERNAME_INPUT = (By.XPATH, "//*[@id='input-username']")
    PASSWORD_INPUT = (By.XPATH, "//*[@id='input-password']")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    LOGOUT_LINK = (By.XPATH, "//*[contains(text(), 'Logout')]")
    LOGIN_MESSAGE = (
        By.XPATH,
        "//*[@class='card-header' and text()=' Please enter your login details.']",
    )
    DASHBOARD_TITLE = "Dashboard"
    CUSTOMERS = (By.XPATH, "//a[text()=' Customers']")
    CUSTOMERS_1 = (By.XPATH, "//a[text()='Customers']")
    BOX = (By.XPATH, "//text()[contains(.,'{}')]/../..//input")
    DELETE = (By.CSS_SELECTOR, ".btn.btn-danger")
    DELETE_OK = (By.CSS_SELECTOR, ".alert")
    CATALOG = (By.XPATH, "//ul[@id='menu']//li[@id='menu-catalog']")
    # CATALOG = (By.XPATH, "//*[@id='menu-catalog']")
    PRODUCT = (By.XPATH, "//a[text()='Products']")

    @allure.step("Выполняется вход на страницу")
    def go_to_administration(self):
        self.browser.get(f"{self.browser.base_url}/administration")

    @allure.step("Выполняется проверка элементов на странице admin")
    def check_elements(self):
        self.check_element_present(*self.USERNAME_INPUT)
        self.check_element_present(*self.PASSWORD_INPUT)
        self.check_element_present(*self.SUBMIT_BUTTON)
        self.check_element_present(*self.LOGIN_MESSAGE)

    @allure.step("Выполняется ввод в поле username и поле password")
    def login(self):
        self.send_keys(element=self._find_element(self.USERNAME_INPUT), text="user")
        entered_text_1 = self._find_element(self.PASSWORD_INPUT).get_attribute("value")

        self.logger.info(f"{self.class_name}: Текущий текст в поле: {entered_text_1}")

        self.send_keys(element=self._find_element(self.PASSWORD_INPUT), text="bitnami")
        entered_text_2 = self._find_element(self.PASSWORD_INPUT).get_attribute("value")

        self.logger.info(f"{self.class_name}: Текущий текст в поле: {entered_text_2}")

        self._find_element(self.SUBMIT_BUTTON).click()

        self.logger.info("Вход в систему выполнен")
        self.verify_title("Administration")

    @allure.step("Выполняется выход из учетной записи admin")
    def logout(self):
        self._find_element(self.LOGOUT_LINK).click()

    @allure.step("Удаление пользователя")
    def delete_user(self, new_person):
        self._find_element(self.CUSTOMERS).click()
        self.find_clickable_element(self.CUSTOMERS_1).click()
        self._find_element(
            (
                self.BOX[0],
                self.BOX[1].format(f"{new_person.name} {new_person.lastname}"),
            )
        ).click()
        self._find_element(self.DELETE).click()

    @allure.step("Пользователь успешно удален")
    def assert_delete_user(self):
        assert (
            self._find_element(self.DELETE_OK).text
            == "Success: You have modified customers!"
        )

    @allure.step("Открытие просмотра страницы продуктов")
    def open_product_page(self):
        self._find_element(self.CATALOG).click()
        self.find_clickable_element(self.PRODUCT).click()


class AdminProductPage(BasePage):
    ADD_NEW_PRODUCT = (By.XPATH, "//*[@class='float-end']//a[@aria-label='Add New']")
    MOVE_TO_ACTION_WITH_PRODUCT = (By.CSS_SELECTOR, ".btn.btn-primary")
    FILTER_NAME = (By.NAME, "filter_name")
    FILTER = (By.ID, "button-filter")
    ASSERT_PRODUCT = (By.CSS_SELECTOR, ".table.table-bordered.table-hover")
    BOX = (By.XPATH, "//text()[contains(.,'{}')]/../..//input")
    DELETE = (By.CSS_SELECTOR, ".btn.btn-danger")

    @allure.step("Переход на страницу добавления нового товара")
    def step_add_new_product(self, browser):
        ActionChains(self.browser).move_to_element(
            self._find_element(self.MOVE_TO_ACTION_WITH_PRODUCT)
        ).perform()
        self._find_element(self.ADD_NEW_PRODUCT).click()

    @allure.step("Фильтрация по имени товара")
    def filter_name(self, data):
        self.send_keys(element=self._find_element(self.FILTER_NAME), text=data.name)
        self._find_element(self.FILTER).click()

    @allure.step("Подтверждение товара на странице")
    def assert_product(self):
        time.sleep(0.5)  # Необходимо для того чтобы обновилась таблица на странице
        result = self._find_element(self.ASSERT_PRODUCT).text
        return result

    @allure.step("Удаление товара")
    def delete_product(self, name):
        self._find_element((self.BOX[0], self.BOX[1].format(f"{name}"))).click()
        self._find_element(self.DELETE).click()


class AddProductPage(BasePage):
    ADD_NEW_PRODUCT = (By.CSS_SELECTOR, "#input-username")
    PASSWORD = (By.CSS_SELECTOR, "#input-password")
    PRODUCT_NAME = (By.NAME, "product_description[1][name]")
    META_TAG_TITLE = (By.NAME, "product_description[1][meta_title]")
    MODEL = (By.NAME, "model")
    SAFE = (By.XPATH, "//button[@aria-label='Save']")
    BACK = (By.XPATH, "//*[@aria-label='Back']")
    GENERAL_TAB = (By.XPATH, "//a[@href='#tab-general']")
    DATA_TAB = (By.XPATH, "//a[@href='#tab-data']")
    SEO_TAB = (By.XPATH, "//a[@href='#tab-seo']")
    SEO_KEYWORD = (By.NAME, "product_seo_url[0][1]")
    MOVE_TO_ACTION_WITH_PRODUCT = (By.CSS_SELECTOR, ".btn.btn-primary")
    MOVE_TO_ACTION_BACK_TO_PRODUCTS = (By.CSS_SELECTOR, ".btn.btn-light")
    SAVE_ASSERT = (By.XPATH, "//*[@id='alert']")

    @allure.step("Ввод обязательных полей для карточки товара на вкладке General")
    def send_required_fields_general_tab(self, data):
        self._find_element(self.GENERAL_TAB).click()
        self.send_keys(element=self._find_element(self.PRODUCT_NAME), text=data.name)
        self.send_keys(
            element=self._find_element(self.META_TAG_TITLE), text=data.meta_tag
        )

    @allure.step("Ввод обязательных полей для карточки товара на вкладке Data")
    def send_required_fields_model_tab(self, data):
        self._find_element(self.DATA_TAB).click()
        self.send_keys(element=self._find_element(self.MODEL), text=data.model)

    @allure.step("Ввод обязательных полей для карточки товара на вкладке SEO")
    def send_required_fields_seo_tab(self, data):
        self._find_element(self.SEO_TAB).click()
        self.send_keys(element=self._find_element(self.SEO_KEYWORD), text=data.seo)

    @allure.step("Сохранение карточки товара")
    def safe_product(self, browser):
        ActionChains(self.browser).move_to_element(
            self._find_element(self.MOVE_TO_ACTION_WITH_PRODUCT)
        ).perform()
        self._find_element(self.SAFE).click()

    @allure.step("Возрат к списку товаров")
    def back_to_products(self, browser):
        ActionChains(self.browser).move_to_element(
            self._find_element(self.MOVE_TO_ACTION_BACK_TO_PRODUCTS)
        ).perform()
        self._find_element(self.BACK).click()

    @allure.step("Появление аллерта после сохранения карточки товара")
    def save_assert(self):
        time.sleep(0.5)
        save_assert = self.wait_find_element(self.SAVE_ASSERT).text
        return save_assert
