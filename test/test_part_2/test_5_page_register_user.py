from selenium.webdriver.common.by import By


def test_page_register_users(browser):
    browser.get(f"{browser.base_url}/index.php?route=account/register")
    assert (
        "Register Account" in browser.title
    ), "Title страницы отличается от ожидаемого"
    browser.find_element(By.ID, "input-firstname")
    browser.find_element(By.ID, "input-lastname")
    browser.find_element(By.ID, "input-email")
    browser.find_element(By.ID, "input-password")
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    browser.find_element(By.XPATH, "//input[@id='input-newsletter']")
    browser.find_element(By.XPATH, "//input[@name='agree']")
