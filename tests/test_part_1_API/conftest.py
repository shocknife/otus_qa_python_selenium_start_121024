import pytest
import allure
import logging
from config.configuration import API_USERNAME, API_KEY, API_BASE_URL
from page_objects_API.api_token import ApiToken


def pytest_addoption(parser):
    parser.addoption("--url_api", default=API_BASE_URL, help="BaseUrl for api_tests API")
    parser.addoption("--username", default=API_USERNAME, help="Пользователь по умолчанию в админке")
    parser.addoption("--key", default=API_KEY, help="Ключ по умолчанию в админке")

@pytest.hookimpl(tryfirst=True)
def pytest_runtest_setup(item):
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    item.logger = logger

@pytest.hookimpl(tryfirst=True)
def pytest_runtest_call(item):
    if hasattr(item, 'logger'):
        logger = item.logger
        logger.info(f"Running test: {item.name}")


@pytest.hookimpl(tryfirst=True)
def pytest_runtest_teardown(item):
    if hasattr(item, 'logger'):
        logger = item.logger
        logger.info(f"Finished test: {item.name}")

@pytest.hookimpl(tryfirst=True)
def pytest_runtest_logreport(report):
    if report.failed and hasattr(report, 'longrepr'):
        allure.attach(str(report.longrepr), name="Error Log", attachment_type=allure.attachment_type.TEXT)


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