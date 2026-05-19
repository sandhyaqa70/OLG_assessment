"""Google Search page object for restaurant searches."""
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.wait_helper import WaitHelper
from utils.logger import LoggerManager
import time

logger = LoggerManager.get_logger(__name__)


class GoogleMapsMaps:
    """Handles restaurant search on Google Search."""
    
    SEARCH_BOX = (By.NAME, "q")
    
    def __init__(self, driver):
        """Initialize with WebDriver."""
        self.driver = driver
    
    def get_page_title(self):
        """Get the page title."""
        return self.driver.title
    
    def search_restaurants(self, query="Restaurants", location=""):
        """Search for restaurants on Google."""
        try:
            search_box = WaitHelper.wait_for_element_visible(self.driver, self.SEARCH_BOX, timeout=10)
            search_box.click()
            search_box.clear()
            
            if location:
                search_query = f"{query} in {location}"
            else:
                search_query = query
            
            search_box.send_keys(search_query)
            logger.info(f"Entered search query: {search_query}")
            
            time.sleep(1)
            search_box.send_keys(Keys.RETURN)
            logger.info("Pressed Enter to search")
            
            time.sleep(4)
            WebDriverWait(self.driver, 10).until(
                lambda driver: driver.execute_script("return document.readyState") == "complete"
            )
            logger.info("Results page loaded")
            
        except Exception as e:
            logger.error(f"Error searching restaurants: {str(e)}")
            raise
    
    def get_restaurant_results(self):
        """
        Get restaurant results from the search results page.
        
        Returns:
            list: List of result elements (empty in headless/limited JS)
        """
        try:
            # Quick attempt - Google results require JS rendering
            results = []
            
            try:
                results = self.driver.find_elements(By.CSS_SELECTOR, "div.g")
                if len(results) > 0:
                    logger.info(f"Found {len(results)} results via div.g")
                    return results
            except Exception as e:
                logger.debug(f"Result search failed: {str(e)}")
            
            logger.info("No results found")
            return []
            
        except Exception as e:
            logger.error(f"Error getting results: {str(e)}")
            return []
    
    def get_restaurant_count(self):
        """
        Get the count of search results with actual content.
        
        Returns:
            int: Number of results with content
        """
        results = self.get_restaurant_results()
        content_results = [r for r in results if r.text and len(r.text.strip()) > 10]
        logger.info(f"Total results found: {len(content_results)} (from {len(results)} elements)")
        return len(content_results)
    
    def get_first_restaurant_name(self):
        """
        Get the text of the first search result with actual content.
        
        Returns:
            str: Text of first result or None if no content found
        """
        try:
            results = self.get_restaurant_results()
            if results:
                for result in results:
                    text = result.text.strip()
                    if text and len(text) > 10:
                        name = text[:100]
                        logger.info(f"First result: {name}")
                        return name
            logger.warning("No results with content found")
            return None
        except Exception as e:
            logger.error(f"Error getting first result: {str(e)}")
            return None
    
    def verify_results_contain_restaurants(self):
        """
        Verify that results contain at least one item.
        
        Returns:
            bool: True if at least one result is found
        """
        count = self.get_restaurant_count()
        result = count >= 1
        logger.info(f"Results verification: {result} (count: {count})")
        return result
