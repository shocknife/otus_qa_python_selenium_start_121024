import time
from random import randint
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_add_item_in_cart(browser):
    browser.get(f"{browser.base_url}")
    wait = WebDriverWait(browser, 10)
    products = browser.find_elements(By.XPATH, "//*[@class='description']/h4/a")
    list_products = [item.text for item in products]
    assert (
        len(products) == 4
    ), f"Количество найденных карточек {len(products)} не равно 4"
    cart_items = wait.until(
        EC.visibility_of_all_elements_located(
            (By.CSS_SELECTOR, 'button[formaction*="checkout/cart.add"]')
        )
    )
    """Выбираю между первыми 2 элементами (MacBook и iPhone), так как на двух других (Apple Cinema 30" и Canon EOS 5D) 
    совершенно противоположное поведение. Первые 2 сразу добавляются в корзину, а вторые, 
    сначала открывают карточку продукта, и там надо жать на кнопку добавление в корзину"""
    item = randint(0, 1)
    time.sleep(1)
    ActionChains(browser).move_to_element(cart_items[item]).perform()
    cart_items[item].click()
    cart = browser.find_element(
        By.XPATH, "//*[contains(@class,'d-none') and text()='Shopping Cart']"
    )
    ActionChains(browser).move_to_element(cart).perform()
    browser.find_element(By.XPATH, "//button[@class='btn-close']").click()
    wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//*[contains(@class,'d-none') and text()='Shopping Cart']")
        )
    ).click()
    product_name = browser.find_element(
        By.XPATH, "//td[contains(@class, 'text-wrap')]/a"
    )
    assert product_name.text in list_products, "Товар не найден в корзине"
