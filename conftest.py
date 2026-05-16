"""
Pytest configuration and fixtures.
"""
import pytest
from selenium import webdriver
from config.settings import IMPLICIT_WAIT
from utils.driver_factory import DriverFactory
from utils.logger import LoggerManager
from utils.screenshot_manager import ScreenshotManager

logger = LoggerManager.get_logger(__name__)


@pytest.fixture(scope="function")
def driver():
    """
    Fixture to provide WebDriver instance for each test.
    
    Yields:
        WebDriver: Configured WebDriver instance
    """
    logger.info("=" * 60)
    logger.info("Setting up WebDriver")
    
    driver_instance = DriverFactory.create_driver()
    driver_instance.implicitly_wait(IMPLICIT_WAIT)
    
    yield driver_instance
    
    logger.info("Tearing down WebDriver")
    DriverFactory.quit_driver(driver_instance)
    logger.info("=" * 60)


@pytest.fixture(scope="function", autouse=True)
def screenshot_on_failure(request, driver):
    """
    Fixture to take screenshot on test failure.
    """
    yield
    
    # If test failed, take screenshot
    try:
        if hasattr(request.node, 'rep_call') and request.node.rep_call.failed:
            test_name = request.node.name
            logger.warning(f"Test {test_name} failed. Taking screenshot...")
            ScreenshotManager.take_screenshot(driver, f"failure_{test_name}")
    except Exception as e:
        logger.warning(f"Could not take screenshot: {e}")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Hook to capture test result for screenshot_on_failure fixture.
    """
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)
