from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login_logout_admin(browser):
    browser.get(f"{browser.base_url}/administration")
    assert "Administration" in browser.title, "Title страницы отличается от ожидаемого"
    browser.find_element(By.ID, "input-username").send_keys("user")
    browser.find_element(By.NAME, "password").send_keys("bitnami")
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    wait = WebDriverWait(browser, 2)
    wait.until(EC.title_is("Dashboard"))
    browser.find_element(By.XPATH, "//*[contains(text(), 'John Doe')]")
    browser.find_element(By.XPATH, "//*[contains(text(), 'Logout')]").click()
    assert "Administration" in browser.title, "Title страницы отличается от ожидаемого"
