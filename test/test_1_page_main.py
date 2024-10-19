from selenium.webdriver.common.by import By


def test_main_page(browser):
    browser.get(f"{browser.base_url}")
    assert "Your Store" in browser.title, "Title страницы отличается от ожидаемого"
    browser.find_element(By.XPATH, "//button[@data-bs-toggle='dropdown']")
    card_items = browser.find_elements(By.XPATH, "//*[@class='product-thumb']")
    assert (
        len(card_items) == 4
    ), f"Количество найденных карточек {len(card_items)} не равно 4"
    banner_items = browser.find_elements(By.XPATH, "//*[@data-bs-ride='carousel']")
    assert (
        len(banner_items) == 2
    ), f"Количество найденных карточек {len(banner_items)} не равно 4"
    browser.find_element(
        By.XPATH, "//*[contains(@class,'d-none') and text()='My Account']"
    )
    browser.find_elements(By.LINK_TEXT, "Privacy Policy")
