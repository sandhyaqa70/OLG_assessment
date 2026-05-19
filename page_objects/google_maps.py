"""Google Maps page object."""
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from utils.wait_helper import WaitHelper
from utils.logger import LoggerManager
import time

logger = LoggerManager.get_logger(__name__)


class GoogleMapsMaps:
    """Handles interactions with Google Maps."""
    
    # Locators
    SEARCH_BOX = (By.CSS_SELECTOR, "input[type='text'][placeholder*='Search']")
    RESTAURANT_RESULT = (By.CSS_SELECTOR, "div[role='listbox'] div[role='option']")
    PLACE_NAME = (By.CSS_SELECTOR, "div.fontTitleSmall")
    
    def __init__(self, driver):
        """Initialize with WebDriver."""
        self.driver = driver
    
    def get_page_title(self):
        """Get the page title."""
        return self.driver.title
    
    def search_restaurants(self, query="Restaurants", location=""):
        """Search for restaurants on Maps."""
        try:
            # Try to find and click the search box
            search_box = WaitHelper.wait_for_element_visible(self.driver, self.SEARCH_BOX, timeout=10)
            search_box.click()
            
            # Clear any existing text and enter search query
            search_box.clear()
            if location:
                search_query = f"{query} in {location}"
            else:
                search_query = query
            
            search_box.send_keys(search_query)
            logger.info(f"Entered search query: {search_query}")
            
            # Wait a bit for results to populate
            time.sleep(2)
            
            # Press Enter to search
            search_box.send_keys(Keys.RETURN)
            logger.info("Pressed Enter to search")
            
            # Wait for results to load
            time.sleep(3)
            
        except Exception as e:
            logger.error(f"Error searching restaurants: {str(e)}")
            raise
    
    def get_restaurant_results(self):
        """
        Get restaurant results from the page.
        
        Returns:
            list: List of restaurant elements
        """
        try:
            # Wait for results to be present
            results = WaitHelper.wait_for_elements_visible(self.driver, self.RESTAURANT_RESULT, timeout=10)
            logger.info(f"Found {len(results)} restaurant results")
            return results
        except Exception as e:
            logger.error(f"Error getting restaurant results: {str(e)}")
            return []
    
    def get_restaurant_count(self):
        """
        Get the count of restaurant results.
        
        Returns:
            int: Number of restaurants found
        """
        results = self.get_restaurant_results()
        logger.info(f"Total restaurants found: {len(results)}")
        return len(results)
    
    def get_first_restaurant_name(self):
        """
        Get the name of the first restaurant result.
        
        Returns:
            str: Name of first restaurant
        """
        try:
            results = self.get_restaurant_results()
            if results:
                first_restaurant = results[0]
                name = first_restaurant.text
                logger.info(f"First restaurant name: {name}")
                return name
            else:
                logger.warning("No restaurants found")
                return None
        except Exception as e:
            logger.error(f"Error getting first restaurant name: {str(e)}")
            return None
    
    def verify_results_contain_restaurants(self):
        """
        Verify that results contain at least one restaurant.
        
        Returns:
            bool: True if at least one restaurant is found
        """
        count = self.get_restaurant_count()
        result = count >= 1
        logger.info(f"Restaurant count verification: {result} (count: {count})")
        return result
