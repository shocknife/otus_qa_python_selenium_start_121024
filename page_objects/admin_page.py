import allure
from selenium.webdriver.common.by import By


from page_objects.base_page import BasePage


class AdminPage(BasePage):
    USERNAME_INPUT = (By.ID, "input-username")
    PASSWORD_INPUT = (By.NAME, "password")
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

    @allure.step("Выполняется вход на страницу")
    def go_to_administration(self):
        self.browser.get(f"{self.browser.base_url}/administration")

    @allure.step("Выполняется проверка элементов на странице admin")
    def check_elements(self):
        self.check_element_present(*self.USERNAME_INPUT)
        self.check_element_present(*self.PASSWORD_INPUT)
        self.check_element_present(*self.SUBMIT_BUTTON)
        self.check_element_present(*self.LOGIN_MESSAGE)

    @allure.step("Выполняется ввод username и password")
    def login(self, username, password):
        self.browser.find_element(*self.USERNAME_INPUT).send_keys(username)
        self.browser.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.browser.find_element(*self.SUBMIT_BUTTON).click()

    @allure.step("Выполняется выход из учетной записи admin")
    def logout(self):
        self.browser.find_element(*self.LOGOUT_LINK).click()

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
