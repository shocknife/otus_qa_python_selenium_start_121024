import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FFOptions


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome")
    parser.addoption("--base_url", default="http://192.168.1.242:8082")
    parser.addoption("--yad", default="D:\\Coding\\Drivers\\yandexdriver.exe")
    parser.addoption("--headless", action="store_true")


@pytest.fixture()
def browser(pytestconfig):
    browser_name = pytestconfig.getoption("browser")
    yad = pytestconfig.getoption("yad")
    base_url = pytestconfig.getoption("base_url")
    headless = pytestconfig.getoption("headless")

    driver = None

    if browser_name in ["ch", "chrome"]:
        options = ChromeOptions()
        if headless:
            options.add_argument("headless=new")
        driver = webdriver.Chrome(options=options)
    elif browser_name in ["ff", "firefox"]:
        options = FFOptions()
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)
    elif browser_name in ["ya", "yandex"]:
        options = ChromeOptions()
        if headless:
            options.add_argument("headless=new")
        options.binary_location = "C:\\Users\\PC\\AppData\\Local\\Yandex\\YandexBrowser\\Application\\browser.exe)"
        driver = webdriver.Chrome(options=options, service=Service(executable_path=yad))

    driver.maximize_window()
    driver.base_url = base_url

    yield driver

    driver.quit()
