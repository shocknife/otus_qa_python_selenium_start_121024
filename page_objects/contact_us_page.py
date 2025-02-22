import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from page_objects.base_page import BasePage


class ContactUsPage(BasePage):
    LOGOUT_ASSERT = (By.CSS_SELECTOR, "h1")
    YOUR_NAME = (By.XPATH, "//*[@name='name']")
    EMAIL_ADDRESS = (By.XPATH, "//*[@name='email']")
    ENQUIRY = (By.XPATH, "//*[@name='enquiry']")
    NEGATIVE_ENQUIRY = (By.XPATH, "//*[@id='error-enquiry']")
    SUBMIT = (By.XPATH, "//button[text()='Submit']")
    CONTACT_US = (By.XPATH, "//a[text()='Contact Us']")
    SEND_FORM_MESSAGE = (By.XPATH, "//div[@id='common-success']//p")

    def open_contact_page(self, browser):
        element = self.find_presence_element(self.CONTACT_US)
        ActionChains(browser).move_to_element(element).perform()
        self.find_presence_element(self.CONTACT_US).click()

    def entering_name(self, name):
        with allure.step(f"Ввод {name}"):
            self.send_keys(element=self._find_element(self.YOUR_NAME), text=name)

    def entering_email(self, email):
        with allure.step(f"Ввод {email}"):
            self.send_keys(element=self._find_element(self.EMAIL_ADDRESS), text=email)

    def entering_enquiry(self, enquiry):
        with allure.step(f"Ввод {enquiry}"):
            self.send_keys(element=self._find_element(self.ENQUIRY), text=enquiry)

    def send_submit(self, browser):
        with allure.step("Отправка запроса"):
            element = self.find_presence_element(self.SUBMIT)
            ActionChains(browser).move_to_element(element).perform()
            self.find_presence_element(self.SUBMIT).click()

    @property
    def message_send_form(self):
        message = self._find_element(self.SEND_FORM_MESSAGE).text
        return message

    @property
    def message_send_form_negative_enquiry(self):
        message = self._find_element(self.NEGATIVE_ENQUIRY).text
        return message
