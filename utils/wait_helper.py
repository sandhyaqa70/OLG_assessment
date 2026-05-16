"""
Wait helper utilities for explicit waits.
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from config.settings import EXPLICIT_WAIT
from utils.logger import LoggerManager

logger = LoggerManager.get_logger(__name__)


class WaitHelper:
    """Helper class for managing waits."""
    
    @staticmethod
    def wait_for_element_visible(driver, locator, timeout=EXPLICIT_WAIT):
        """
        Wait for element to be visible.
        
        Args:
            driver: WebDriver instance
            locator: Tuple (By.XPATH, "xpath_value")
            timeout: Maximum wait time in seconds
            
        Returns:
            WebElement: The visible element
        """
        try:
            wait = WebDriverWait(driver, timeout)
            element = wait.until(EC.visibility_of_element_located(locator))
            logger.info(f"Element {locator} is now visible")
            return element
        except TimeoutException:
            logger.error(f"Element {locator} was not visible within {timeout} seconds")
            raise
    
    @staticmethod
    def wait_for_element_present(driver, locator, timeout=EXPLICIT_WAIT):
        """
        Wait for element to be present in DOM.
        
        Args:
            driver: WebDriver instance
            locator: Tuple (By.XPATH, "xpath_value")
            timeout: Maximum wait time in seconds
            
        Returns:
            WebElement: The element
        """
        try:
            wait = WebDriverWait(driver, timeout)
            element = wait.until(EC.presence_of_element_located(locator))
            logger.info(f"Element {locator} is now present")
            return element
        except TimeoutException:
            logger.error(f"Element {locator} was not present within {timeout} seconds")
            raise
    
    @staticmethod
    def wait_for_elements_visible(driver, locator, timeout=EXPLICIT_WAIT):
        """
        Wait for multiple elements to be visible.
        
        Args:
            driver: WebDriver instance
            locator: Tuple (By.XPATH, "xpath_value")
            timeout: Maximum wait time in seconds
            
        Returns:
            list: List of visible elements
        """
        try:
            wait = WebDriverWait(driver, timeout)
            elements = wait.until(EC.visibility_of_all_elements_located(locator))
            logger.info(f"Elements {locator} are now visible (count: {len(elements)})")
            return elements
        except TimeoutException:
            logger.error(f"Elements {locator} were not visible within {timeout} seconds")
            raise
    
    @staticmethod
    def element_is_displayed(driver, locator, timeout=EXPLICIT_WAIT):
        """
        Check if element is displayed.
        
        Args:
            driver: WebDriver instance
            locator: Tuple (By.XPATH, "xpath_value")
            timeout: Maximum wait time in seconds
            
        Returns:
            bool: True if element is displayed
        """
        try:
            element = WaitHelper.wait_for_element_visible(driver, locator, timeout)
            return element.is_displayed()
        except TimeoutException:
            return False
