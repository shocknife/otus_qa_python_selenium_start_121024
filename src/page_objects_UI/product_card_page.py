import allure
from selenium.webdriver.common.by import By
from src.page_objects_UI.base_page import BasePage


class ProductPage(BasePage):
    TITLE = "MacBook"
    MACBOOK_LINK = (By.LINK_TEXT, "MacBook")
    ADD_TO_CART_BUTTON = (By.ID, "button-cart")
    PRICE_NEW = (By.XPATH, "//span[@class='price-new']")
    DESCRIPTION_LINK = (By.LINK_TEXT, "Description")

    @allure.step("Открытие главной страницы")
    def open_main_page(self):
        super().open(self.browser.base_url)

    @allure.step("Выбор первого продукта на главной странице")
    def select_first_product(self):
        card_items = self.find_elements(*self.MACBOOK_LINK)
        card_items[0].click()

    @allure.step("Проверка элементов на странице")
    def check_elements(self):
        self.check_element_present(*self.MACBOOK_LINK)
        self.check_element_present(*self.ADD_TO_CART_BUTTON)
        self.check_element_present(*self.PRICE_NEW)
        self.find_elements(*self.DESCRIPTION_LINK)
