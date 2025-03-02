import allure
from selenium.webdriver.common.by import By
from src.page_objects_UI.base_page import BasePage


class RegistrationPage(BasePage):
    TITLE = "Register Account"
    FIRSTNAME_INPUT = (By.ID, "input-firstname")
    LASTNAME_INPUT = (By.ID, "input-lastname")
    EMAIL_INPUT = (By.ID, "input-email")
    PASSWORD_INPUT = (By.ID, "input-password")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    NEWSLETTER_INPUT = (By.XPATH, "//input[@id='input-newsletter']")
    AGREE_INPUT = (By.XPATH, "//input[@name='agree']")
    BOX_PRIVACY_POLICY = (By.CSS_SELECTOR, "[name ='agree']")
    CONTINUE = (By.CSS_SELECTOR, ".btn.btn-primary")
    GOOD_REGISTER = (By.XPATH, "//div[@id='common-success']//h1")
    ASSERT_TEXT = (By.XPATH, '//*[text()="{}"]')
    LOGIN = (By.XPATH, "//button[text()='Login']")
    LOGOUT_ASSERT = (By.XPATH, "//*[@id='content']/h1[1]")
    LOGIN_ASSERT = (By.XPATH, "//h2[text()='My Account']")
    WISH_LIST = (By.XPATH, "//a[@id='wishlist-total']")
    WISH_LIST_TOTAL = (By.XPATH, "//*[@id='wishlist-total']")
    WISH_LIST_ACCOUNT = (By.XPATH, "//div[@id='account-wishlist']//h1")
    NEW_CUSTOMER = (By.XPATH, "//*[@id='content']//h2[1]")

    @allure.step("Открытие страницы регистрации пользователя")
    def open_reg_user_page(self):
        super().open(f"{self.browser.base_url}/index.php?route=account/register")

    @allure.step("Открытие страницы логирования")
    def open_login_page(self, uri=None):
        super().open(self.browser.base_url + uri)

    @allure.step("Проверка элементов на странице регистрации пользователя")
    def check_registration_user_form(self):
        self.find_element(*self.FIRSTNAME_INPUT)
        self.find_element(*self.LASTNAME_INPUT)
        self.find_element(*self.EMAIL_INPUT)
        self.find_element(*self.PASSWORD_INPUT)
        self.find_element(*self.SUBMIT_BUTTON)
        self.find_element(*self.NEWSLETTER_INPUT)
        self.find_element(*self.AGREE_INPUT)

    @allure.step("Регистрация нового аккаунта")
    def created_account(self, new_person):
        with allure.step(
            f"fill fields {new_person.name}, {new_person.lastname}, "
            f"{new_person.email}, {new_person.password}"
        ):
            firstname = self.find_element(*self.FIRSTNAME_INPUT)
            self.send_keys(element=firstname, text=new_person.name)
            lastname = self.find_element(*self.LASTNAME_INPUT)
            self.send_keys(element=lastname, text=new_person.lastname)
            email = self.find_element(*self.EMAIL_INPUT)
            self.send_keys(element=email, text=new_person.email)
            self.send_keys(
                element=self.find_element(*self.PASSWORD_INPUT),
                text=new_person.password,
            )
            self.find_element(*self.BOX_PRIVACY_POLICY).click()
            self.find_element(*self.CONTINUE).click()
        assert (
            self._find_element(self.GOOD_REGISTER).text
            == "Your Account Has Been Created!"
        ), f"тут лежит {self.find_element(*self.GOOD_REGISTER).text}"

    @allure.step("Пользователь входит в аккаунт")
    def login_user(self, create_new_user):
        with allure.step(f"login {create_new_user.email}"):
            self.open_login_page("/en-gb?route=account/login")
            self.send_keys(
                element=self.wait_find_element(self.EMAIL_INPUT),
                text=create_new_user.email,
            )
            self.send_keys(
                element=self.wait_find_element(self.PASSWORD_INPUT),
                text=create_new_user.password,
            )
            self.wait_find_element(self.LOGIN).click()

    @allure.step("Пользователь выходит из аккаунта")
    def logout_assert(self):
        logout_assert = self.wait_find_element(self.LOGOUT_ASSERT).text
        return logout_assert
