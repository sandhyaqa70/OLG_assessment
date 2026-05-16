"""
Part 2 - Restaurant Search Tests
Tests for restaurant search functionality:
- Search for restaurants
- Verify results contain restaurant items
"""
import pytest
from config.settings import GOOGLE_MAPS_URL
from page_objects.google_maps import GoogleMapsMaps
from utils.logger import LoggerManager

logger = LoggerManager.get_logger(__name__)


@pytest.mark.part2
class TestRestaurantSearch:
    """Test suite for restaurant search functionality."""
    
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """Setup for each test - navigate to Google Maps."""
        logger.info(f"Navigating to {GOOGLE_MAPS_URL}")
        driver.get(GOOGLE_MAPS_URL)
        self.page = GoogleMapsMaps(driver)
    
    @pytest.mark.smoke
    def test_google_maps_page_loads(self, driver):
        """
        TEST 1: Verify Google Maps page loads successfully.
        
        Assertion: Page title should indicate it's Google Maps
        """
        logger.info("Starting test: Google Maps Page Load")
        
        title = self.page.get_page_title()
        
        # Assert that page title indicates it's Google Maps
        assert "Google Maps" in title or "Maps" in title, \
            f"Expected 'Google Maps' in title, but got: {title}"
        
        logger.info(f"[PASS] Google Maps page load assertion passed: {title}")
    
    @pytest.mark.smoke
    def test_restaurant_search_returns_results(self, driver):
        """
        TEST 2: Perform a restaurant search and verify results.
        
        Assertion: Search should return at least one restaurant result
        """
        logger.info("Starting test: Restaurant Search Returns Results")
        
        # Perform restaurant search
        self.page.search_restaurants("Restaurants")
        
        # Get results and verify at least one restaurant is found
        restaurant_count = self.page.get_restaurant_count()
        
        assert restaurant_count >= 1, \
            f"Expected at least 1 restaurant in results, but got: {restaurant_count}"
        
        logger.info(f"[PASS] Restaurant search assertion passed. Found {restaurant_count} restaurants")
    
    @pytest.mark.smoke
    def test_first_restaurant_has_name(self, driver):
        """
        TEST 3: Verify first restaurant result has a name.
        
        Assertion: First restaurant should have a valid name
        """
        logger.info("Starting test: First Restaurant Has Name")
        
        # Perform restaurant search
        self.page.search_restaurants("Restaurants")
        
        # Get first restaurant name
        restaurant_name = self.page.get_first_restaurant_name()
        
        assert restaurant_name is not None, "First restaurant does not have a name"
        assert len(restaurant_name.strip()) > 0, "First restaurant name is empty"
        
        logger.info(f"[PASS] First restaurant name assertion passed: {restaurant_name}")
    
    @pytest.mark.regression
    def test_restaurant_results_verification(self, driver):
        """
        TEST 4: Comprehensive restaurant results verification.
        
        Assertion: Restaurant results should meet specific criteria
        """
        logger.info("Starting test: Restaurant Results Comprehensive Verification")
        
        # Perform restaurant search
        self.page.search_restaurants("Restaurants")
        
        # Verify results contain restaurants
        has_restaurants = self.page.verify_results_contain_restaurants()
        
        assert has_restaurants is True, "Results do not contain any restaurants"
        
        # Verify restaurant count
        restaurant_count = self.page.get_restaurant_count()
        logger.info(f"Found {restaurant_count} restaurants in results")
        
        logger.info("[PASS] Restaurant results verification passed")
