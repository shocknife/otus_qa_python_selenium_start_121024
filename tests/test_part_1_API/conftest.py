import pytest
import allure
import logging


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


