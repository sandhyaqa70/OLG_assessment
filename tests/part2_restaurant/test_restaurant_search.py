"""Tests for Google Maps restaurant search."""
import pytest
from config.settings import GOOGLE_MAPS_URL
from page_objects.google_maps import GoogleMapsMaps
from utils.logger import LoggerManager

logger = LoggerManager.get_logger(__name__)


@pytest.mark.part2
class TestRestaurantSearch:
    """Restaurant search tests on Google Maps."""
    
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """Navigate to Google Maps before each test."""
        logger.info(f"Going to {GOOGLE_MAPS_URL}")
        driver.get(GOOGLE_MAPS_URL)
        self.page = GoogleMapsMaps(driver)
    
    @pytest.mark.smoke
    def test_google_maps_page_loads(self, driver):
        """Verify Google Maps page loads."""
        title = self.page.get_page_title()
        assert "Maps" in title, f"Expected 'Maps' in title, got: {title}"
    
    @pytest.mark.smoke
    def test_restaurant_search_returns_results(self, driver):
        """Search for restaurants and verify results are found."""
        self.page.search_restaurants("Restaurants")
        count = self.page.get_restaurant_count()
        assert count >= 1, f"No restaurants found, expected at least 1"
    
    @pytest.mark.smoke
    def test_first_restaurant_has_name(self, driver):
        """Verify first restaurant has a name."""
        self.page.search_restaurants("Restaurants")
        name = self.page.get_first_restaurant_name()
        assert name and len(name.strip()) > 0, "Restaurant name is empty"
    
    @pytest.mark.regression
    def test_restaurant_results_verification(self, driver):
        """Verify restaurant results are valid."""
        self.page.search_restaurants("Restaurants")
        has_results = self.page.verify_results_contain_restaurants()
        assert has_results is True, "No restaurant results found"
        restaurant_count = self.page.get_restaurant_count()
        logger.info(f"Found {restaurant_count} restaurants in results")
        
        logger.info("[PASS] Restaurant results verification passed")
