"""
Part 1 - Basic Assertions Tests
Tests for verifying basic web page functionality:
- Page title assertion
- Visible elements assertions
"""
import pytest
from config.settings import GOOGLE_URL
from page_objects.google_homepage import GoogleHomepage
from utils.logger import LoggerManager

logger = LoggerManager.get_logger(__name__)


@pytest.mark.part1
class TestGoogleHomepageBasics:
    """Test suite for Google Homepage basic assertions."""
    
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """Setup for each test - navigate to Google homepage."""
        logger.info(f"Navigating to {GOOGLE_URL}")
        driver.get(GOOGLE_URL)
        self.page = GoogleHomepage(driver)
    
    @pytest.mark.smoke
    def test_page_title_assertion(self, driver):
        """
        TEST 1: Verify the page title matches expected value.
        
        Assertion: Page title should be 'Google' or contain 'Google'
        """
        logger.info("Starting test: Page Title Assertion")
        
        title = self.page.get_page_title()
        
        # Assert that page title contains 'Google'
        assert "Google" in title, f"Expected 'Google' in title, but got: {title}"
        
        logger.info(f"[PASS] Page title assertion passed: {title}")
    
    @pytest.mark.smoke
    def test_search_box_is_visible(self, driver):
        """
        TEST 2: Verify the search box element is visible.
        
        Assertion: Search input field should be visible on the page
        """
        logger.info("Starting test: Search Box Visibility Assertion")
        
        is_visible = self.page.is_search_box_visible()
        
        # Assert that search box is visible
        assert is_visible is True, "Search box element is not visible on the page"
        
        logger.info("[PASS] Search box visibility assertion passed")
    
    @pytest.mark.smoke
    def test_search_button_is_visible(self, driver):
        """
        TEST 3: Verify the search button element is visible.
        
        Assertion: Search button should be visible on the page
        """
        logger.info("Starting test: Search Button Visibility Assertion")
        
        is_visible = self.page.is_search_button_visible()
        
        # Assert that search button is visible
        assert is_visible is True, "Search button element is not visible on the page"
        
        logger.info("[PASS] Search button visibility assertion passed")
