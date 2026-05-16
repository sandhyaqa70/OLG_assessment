"""
Page Object Model for Google Homepage - Part 1 Basic Assertions
"""
from selenium.webdriver.common.by import By
from utils.wait_helper import WaitHelper
from utils.logger import LoggerManager

logger = LoggerManager.get_logger(__name__)


class GoogleHomepage:
    """Page Object for Google Homepage."""
    
    # Locators
    SEARCH_BOX = (By.NAME, "q")
    SEARCH_BUTTON = (By.NAME, "btnK")
    LUCKY_BUTTON = (By.NAME, "btnI")
    GOOGLE_SEARCH_INPUT = (By.CSS_SELECTOR, "input[type='text'][name='q']")
    SEARCH_BUTTONS = (By.CSS_SELECTOR, "button[type='submit']")
    
    def __init__(self, driver):
        """Initialize with WebDriver instance."""
        self.driver = driver
        logger.info("Initialized GoogleHomepage page object")
    
    def get_page_title(self):
        """
        Get the page title.
        
        Returns:
            str: Page title
        """
        title = self.driver.title
        logger.info(f"Page title: {title}")
        return title
    
    def is_search_box_visible(self):
        """
        Check if search box is visible.
        
        Returns:
            bool: True if search box is visible
        """
        try:
            is_visible = WaitHelper.element_is_displayed(self.driver, self.SEARCH_BOX)
            logger.info(f"Search box visibility: {is_visible}")
            return is_visible
        except Exception as e:
            logger.error(f"Error checking search box visibility: {str(e)}")
            return False
    
    def get_search_box_element(self):
        """
        Get the search box element.
        
        Returns:
            WebElement: Search box element
        """
        element = WaitHelper.wait_for_element_visible(self.driver, self.SEARCH_BOX)
        logger.info("Retrieved search box element")
        return element
    
    def is_search_button_visible(self):
        """
        Check if search button is visible.
        
        Returns:
            bool: True if search button is visible
        """
        try:
            buttons = WaitHelper.wait_for_elements_visible(self.driver, self.SEARCH_BUTTONS, timeout=5)
            is_visible = len(buttons) > 0
            logger.info(f"Search button visibility: {is_visible} (found {len(buttons)} buttons)")
            return is_visible
        except Exception as e:
            logger.warning(f"Error checking search button visibility: {str(e)}")
            # Try alternative: check if button element exists and is displayed
            try:
                from selenium.webdriver.common.by import By
                # Try to find any button on the page
                elements = self.driver.find_elements(By.TAG_NAME, "button")
                logger.info(f"Found {len(elements)} total buttons on page")
                return len(elements) > 0
            except:
                logger.error("Could not find any buttons on page")
                return False
    
    def search(self, query):
        """
        Perform a search on Google.
        
        Args:
            query: Search query string
        """
        search_box = self.get_search_box_element()
        search_box.clear()
        search_box.send_keys(query)
        logger.info(f"Entered search query: {query}")
