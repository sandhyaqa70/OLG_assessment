"""Pytest configuration and fixtures."""
import pytest
from config.settings import IMPLICIT_WAIT
from utils.driver_factory import DriverFactory
from utils.logger import LoggerManager
from utils.screenshot_manager import ScreenshotManager

logger = LoggerManager.get_logger(__name__)


@pytest.fixture(scope="function")
def driver():
    """Create a WebDriver for the test, clean up after."""
    logger.info("Starting WebDriver")
    
    driver_instance = DriverFactory.create_driver()
    driver_instance.implicitly_wait(IMPLICIT_WAIT)
    
    yield driver_instance
    
    logger.info("Closing WebDriver")
    DriverFactory.quit_driver(driver_instance)


@pytest.fixture(scope="function", autouse=True)
def screenshot_on_failure(request, driver):
    """Take a screenshot if test fails."""
    yield
    
    try:
        if hasattr(request.node, 'rep_call') and request.node.rep_call.failed:
            test_name = request.node.name
            ScreenshotManager.take_screenshot(driver, f"failure_{test_name}")
    except Exception as e:
        logger.warning(f"Could not capture screenshot: {e}")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Capture test results for the screenshot fixture."""
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)
