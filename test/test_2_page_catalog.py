from selenium.webdriver.common.by import By


def test_page_catalog(browser):
    browser.get(f"{browser.base_url}")
    card_items = browser.find_element(By.LINK_TEXT, "Tablets")
    card_items.click()
    assert "Tablets" in browser.title, "Title страницы отличается от ожидаемого"
    assert "catalog" in browser.current_url
    browser.find_element(By.XPATH, "//*[@class='product-thumb']")
    browser.find_element(By.ID, "column-left")
    browser.find_element(By.ID, "button-list")
    browser.find_element(By.ID, "button-grid")
    browser.find_element(By.ID, "input-sort")
