import json
import logging
import allure
import pytest
import datetime
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FFOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

from config.configuration import BASE_URL, API_BASE_URL, API_USERNAME, API_KEY
from data.create_product import CreateProductData
from data.create_user import CreateUserData
from src.page_objects_API.api_token import ApiToken
from src.page_objects_UI.admin_page import AdminPage, AddProductPage, AdminProductPage
from src.page_objects_UI.app import Application
from src.page_objects_UI.base_page import BasePage
from src.page_objects_UI.main_page import MainPage
from src.page_objects_UI.register_user_page import RegistrationPage


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome", help="Browser for tests")
    parser.addoption(
        "--base_url",
        default=BASE_URL,
        help="Base URL of the application",
    )
    parser.addoption(
        "--yad",
        default="D:\\Coding\\Drivers\\yandexdriver.exe",
        help="Path to YandexDriver",
    )
    parser.addoption(
        "--headless", action="store_true", help="Run browser in headless mode"
    )
    parser.addoption(
        "--log_level", action="store", default="WARNING", help="Set the logging level"
    )
    parser.addoption(
        "--executor",
        default=None,
        nargs="?",
        const="127.0.0.1",
        help="Executor address (default: 127.0.0.1 if not specified)",
    )
    parser.addoption(
        "--mobile", action="store_true", help="Run tests on mobile emulation"
    )
    parser.addoption("--vnc", action="store_true", help="Enable VNC server")
    parser.addoption("--logs", action="store_true", help="Enable logging of tests")
    parser.addoption("--video", action="store_true", help="Record video during tests")
    parser.addoption("--bv", help="Browser version")
    parser.addoption("--no-sandbox")
    parser.addoption(
        "--url_api", default=API_BASE_URL, help="BaseUrl for api_tests API"
    )
    parser.addoption(
        "--username", default=API_USERNAME, help="Пользователь по умолчанию в админке"
    )
    parser.addoption("--key", default=API_KEY, help="Ключ по умолчанию в админке")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.outcome != "passed":
        item.status = "failed"
    else:
        item.status = "passed"

    # Создание скриншота
    if (rep.when == "call" or rep.when == "setup") and rep.outcome == "failed":
        try:
            if "browser" in item.funcargs:
                driver = item.funcargs["browser"]

                screenshots_dir = os.path.join(os.path.dirname(__file__), "screenshots")
                os.makedirs(screenshots_dir, exist_ok=True)

                current_date = datetime.datetime.now().strftime("%Y-%m-%d")
                date_dir = os.path.join(screenshots_dir, current_date)
                os.makedirs(date_dir, exist_ok=True)

                timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                screenshot_path = os.path.join(
                    date_dir, f"{item.name}_{timestamp}_{item.status}.png"
                )

                driver.save_screenshot(screenshot_path)

                logger = driver.logger
                logger.info(f"Скриншот сохранен: {screenshot_path}")
            else:
                logger = logging.getLogger(__name__)
                logger.warning(
                    f"Тест {item.name} не использует браузер, скриншот не создан."
                )
        except Exception as e:
            driver = item.funcargs["browser"]
            logger = driver.logger
            logger.info(f"Не удалось создать скриншот: {e}")

    # Создаем папку для результатов отчетов
    allure_results_dir = os.path.join(os.path.dirname(__file__), "allure-results")
    os.makedirs(allure_results_dir, exist_ok=True)


# Настройка параметров для запуска тестов UI


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("--browser")
    yad = request.config.getoption("--yad")
    base_url = request.config.getoption("--base_url")
    headless = request.config.getoption("--headless")
    log_level = request.config.getoption("--log_level")
    executor = request.config.getoption("--executor")
    vnc = request.config.getoption("--vnc")
    version = request.config.getoption("--bv")
    logs = request.config.getoption("--logs")
    video = request.config.getoption("--video")
    mobile = request.config.getoption("--mobile")

    # Если передан executor, но без конкретного адреса, то по умолчанию ставим "127.0.0.1"
    if executor is None:
        executor_url = None  # Локальный режим
    else:
        # Если executor передан, формируем URL для удаленного сервера
        executor_url = f"http://{executor}:4444/wd/hub"

    log_dir = os.path.join(os.path.dirname(__file__), "logs")

    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    logger = logging.getLogger(request.node.name)
    log_path = os.path.join(log_dir, f"{request.node.name}.log")
    file_handler = logging.FileHandler(log_path, encoding="utf-8")
    file_handler.setFormatter(logging.Formatter("%(levelname)s %(message)s"))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)

    logger.info(
        "===> Test %s started at %s" % (request.node.name, datetime.datetime.now())
    )

    if browser_name in ["ch", "chrome"]:
        browser_name = "chrome"
        options = ChromeOptions()
        if headless:
            options.add_argument("headless=new")
        if not executor:
            driver = webdriver.Chrome(options=options)
    elif browser_name in ["ff", "firefox"]:
        browser_name = "firefox"
        options = FFOptions()
        if headless:
            options.add_argument("--headless")
        if not executor:
            driver = webdriver.Firefox(options=options)
    elif browser_name in ["edge", "Edge", "MicrosoftEdge"]:
        browser_name = "MicrosoftEdge"
        options = EdgeOptions()
        if headless:
            options.add_argument("headless=new")
        if not executor:
            driver = webdriver.Edge(options=options)
    elif browser_name in ["ya", "yandex"]:
        browser_name = "yandex"
        options = ChromeOptions()
        if headless:
            options.add_argument("headless=new")
        if not executor:
            options.binary_location = "C:\\Users\\PC\\AppData\\Local\\Yandex\\YandexBrowser\\Application\\browser.exe"
            driver = webdriver.Chrome(
                options=options, service=Service(executable_path=yad)
            )

    caps = {
        "browserName": browser_name,
        "browserVersion": version,
        # "selenoid:options": {
        #     "enableVNC": vnc,
        #     "name": request.node.name,
        #     "screenResolution": "1280x2000",
        #      "enableVideo": video,
        #     "enableLog": logs,
        #     "timeZone": "Europe/Moscow",
        #     "env": ["LANG=ru_RU.UTF-8", "LANGUAGE=ru:en", "LC_ALL=ru_RU.UTF-8"],
        #  },
        # "acceptInsecureCerts": True,
    }

    if executor:
        for k, v in caps.items():
            options.set_capability(k, v)

        driver = webdriver.Remote(command_executor=executor_url, options=options)

    allure.attach(
        name=driver.session_id,
        body=json.dumps(driver.capabilities, indent=4, ensure_ascii=False),
        attachment_type=allure.attachment_type.JSON,
    )

    driver.log_level = log_level
    driver.logger = logger
    driver.test_name = request.node.name

    logger.info("Browser %s started" % browser)

    if not mobile:
        driver.maximize_window()

    driver.base_url = base_url

    def fin():
        driver.quit()
        logger.info(
            "===> Test %s finished at %s" % (request.node.name, datetime.datetime.now())
        )

    yield driver

    if request.node.status == "failed":
        allure.attach(
            name="failure_screenshot",
            body=driver.get_screenshot_as_png(),
            attachment_type=allure.attachment_type.PNG,
        )
        allure.attach(
            name="page_source",
            body=driver.page_source,
            attachment_type=allure.attachment_type.HTML,
        )

    request.addfinalizer(fin)


@pytest.fixture
def create_new_user(browser):
    register_account = RegistrationPage(browser)
    main_page = MainPage(browser)
    admin_panel = AdminPage(browser)
    alert_delete = BasePage(browser)
    main_page.open_main_page()
    main_page.find_user()
    new_person = CreateUserData.create_random()
    register_account.created_account(new_person)
    fixture = Application(driver=browser, data=new_person)
    yield fixture
    admin_panel.go_to_administration()
    admin_panel.login()
    admin_panel.delete_user(new_person)
    alert_delete.alert_window()
    admin_panel.assert_delete_user()


@pytest.fixture
def create_new_product(browser):
    admin_panel = AdminPage(browser)
    add_product = AddProductPage(browser)
    data = CreateProductData.create_random()
    product = AdminProductPage(browser)
    admin_panel.go_to_administration()
    admin_panel.login()
    admin_panel.open_product_page()
    product.step_add_new_product(browser)
    add_product.send_required_fields_general_tab(data)
    add_product.send_required_fields_model_tab(data)
    add_product.send_required_fields_seo_tab(data)
    add_product.safe_product(browser)
    add_product.back_to_products(browser)
    product.filter_name(data)
    assert data.name in product.assert_product()
    return browser, data


# Настройка параметров для запуска тестов API


@pytest.fixture(scope="session")
def base_url_api(request):
    return request.config.getoption("--url_api")


@pytest.fixture(scope="session")
def username(request):
    return request.config.getoption("--username")


@pytest.fixture(scope="session")
def key(request):
    return request.config.getoption("--key")


@pytest.fixture(scope="session")
def client(base_url_api, username, key):
    client = ApiToken(base_url_api=base_url_api, username=username, key=key)
    yield client


@pytest.fixture(scope="function")
def client_function(base_url_api, username, key):
    client = ApiToken(base_url_api=base_url_api, username=username, key=key)
    yield client
