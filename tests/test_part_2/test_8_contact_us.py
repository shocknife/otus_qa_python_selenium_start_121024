import allure
import pytest

from data.create_contact_us import CreateContactUsData
from page_objects.contact_us_page import ContactUsPage
from page_objects.main_page import MainPage


@allure.title("Проверка корректной отправки запроса")
def test_positiv_send_enquiry(browser):
    main = MainPage(browser)
    contact_page = ContactUsPage(browser)
    message = CreateContactUsData.create_random()
    main.open_main_page()
    contact_page.open_contact_page(browser)
    contact_page.entering_name(message.name)
    contact_page.entering_email(message.email)
    contact_page.entering_enquiry(message.enquiry)
    contact_page.send_submit(browser)
    assert (
        "Your enquiry has been successfully sent to the store owner!"
        == contact_page.message_send_form
    )


@allure.title(
    "Проверка негативных сценариев отправки запроса с превышением текста запроса"
)
@pytest.mark.parametrize(
    "enquiry",
    ["less_10", "s" * 3001],
    ids=["Проверка до 10 символов", "Проверка больше 3000 символов"],
)
def test_add_to_card_negative_enquiry(browser, enquiry):
    main = MainPage(browser)
    contact_page = ContactUsPage(browser)
    message = CreateContactUsData.create_random()
    main.open_main_page()
    contact_page.open_contact_page(browser)
    contact_page.entering_name(message.name)
    contact_page.entering_email(message.email)
    contact_page.entering_enquiry(enquiry)
    contact_page.send_submit(browser)
    assert (
        "Enquiry must be between 10 and 3000 characters!"
        == contact_page.message_send_form_negative_enquiry
    )
