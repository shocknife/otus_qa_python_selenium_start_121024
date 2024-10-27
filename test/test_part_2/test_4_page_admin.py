from selenium.webdriver.common.by import By


def test_admin_page(browser):
    browser.get(f"{browser.base_url}/administration")
    assert "Administration" in browser.title, "Title страницы отличается от ожидаемого"
    browser.find_element(By.ID, "input-username")
    browser.find_element(By.NAME, "password")
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    browser.find_element(
        By.XPATH,
        "//*[@class='card-header' and text()=' Please enter your login details.']",
    )
