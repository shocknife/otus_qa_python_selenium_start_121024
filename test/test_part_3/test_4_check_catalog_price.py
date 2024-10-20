from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_page_catalog(browser):
    browser.get(f"{browser.base_url}")
    wait = WebDriverWait(browser, 10)
    browser.find_element(
        By.XPATH, "//a[@data-bs-toggle='dropdown' and text()='Desktops']"
    ).click()
    browser.find_element(
        By.XPATH, "//*[@class='see-all' and text()='Show All Desktops']"
    ).click()
    assert "catalog" in browser.current_url

    price_button_cart = browser.find_element(
        By.XPATH, "//button[@data-bs-toggle='dropdown']"
    )
    assert (
        "$" in price_button_cart.text
    ), f"Цена на кнопке корзины не отображается со знаком $, отображается текст {price_button_cart.text}"

    products = browser.find_elements(By.XPATH, "//div[@class='price']")

    for item in products:
        price_element = item.find_element(By.XPATH, "//div[@class='price']/span")
        assert (
            "$" in price_element.text
        ), f"Цена на карточке товара не отображается со знаком $, отображается текст {price_element.text}"

    browser.find_element(
        By.XPATH, "//*[contains(@class,'d-none') and text()='Currency']"
    ).click()
    browser.find_element(By.XPATH, "//*[@href='GBP']").click()

    currency_price_button_cart = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//button[@data-bs-toggle='dropdown']")
        )
    )
    assert (
        "£" in currency_price_button_cart.text
    ), f"Цена на кнопке корзины не отображается со знаком £, отображается текст {price_button_cart.text}"

    currency_products = browser.find_elements(By.XPATH, "//div[@class='price']")

    for item in currency_products:
        price_element_currency = item.find_element(
            By.XPATH, "//div[@class='price']/span"
        )
        assert (
            "£" in price_element_currency.text
        ), f"Цена на карточке товара не отображается со знаком £, отображается текст {price_element_currency.text}"
