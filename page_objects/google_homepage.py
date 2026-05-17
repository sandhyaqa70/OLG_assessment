"""Google Homepage page object."""
from selenium.webdriver.common.by import By
from utils.wait_helper import WaitHelper
from utils.logger import LoggerManager

logger = LoggerManager.get_logger(__name__)


class GoogleHomepage:
    """Handles interactions with Google Homepage."""
    
    # Locators
    SEARCH_BOX = (By.NAME, "q")
    SEARCH_BUTTON = (By.NAME, "btnK")
    SEARCH_BUTTONS = (By.CSS_SELECTOR, "button[type='submit']")
    
    def __init__(self, driver):
        """Initialize with WebDriver."""
        self.driver = driver
    
    def get_page_title(self):
        """Get the page title."""
        return self.driver.title
    
    def is_search_box_visible(self):
        """Check if search box is visible on page."""
        try:
            return WaitHelper.element_is_displayed(self.driver, self.SEARCH_BOX)
        except Exception:
            return False
    
    def get_search_box_element(self):
        """Get the search box element."""
        return WaitHelper.wait_for_element_visible(self.driver, self.SEARCH_BOX)
    
    def is_search_button_visible(self):
        """Check if search button is visible."""
        try:
            buttons = WaitHelper.wait_for_elements_visible(self.driver, self.SEARCH_BUTTONS, timeout=5)
            return len(buttons) > 0
        except Exception:
            # Fallback: look for any button
            try:
                from selenium.webdriver.common.by import By
                elements = self.driver.find_elements(By.TAG_NAME, "button")
                return len(elements) > 0
            except:
                return False
    
    def search(self, query):
        """Perform a search."""
        search_box = self.get_search_box_element()
        search_box.clear()
        search_box.send_keys(query)
