from selenium.webdriver.common.by import By


def test_page_product(browser):
    browser.get(f"{browser.base_url}")
    card_items = browser.find_elements(By.XPATH, "//*[@class='product-thumb']")
    card_items[0].click()
    assert "MacBook" in browser.title, "Title страницы отличается от ожидаемого"
    browser.find_elements(By.LINK_TEXT, "MacBook")
    browser.find_element(By.ID, "button-cart")
    browser.find_element(By.XPATH, "//span[@class='price-new']")
    browser.find_elements(By.LINK_TEXT, "Description")
