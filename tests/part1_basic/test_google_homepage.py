"""Tests for Google Homepage."""
import pytest
from config.settings import GOOGLE_URL
from page_objects.google_homepage import GoogleHomepage
from utils.logger import LoggerManager

logger = LoggerManager.get_logger(__name__)


@pytest.mark.part1
class TestGoogleHomepageBasics:
    """Google Homepage tests."""
    
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """Navigate to Google homepage before each test."""
        logger.info(f"Going to {GOOGLE_URL}")
        driver.get(GOOGLE_URL)
        self.page = GoogleHomepage(driver)
    
    @pytest.mark.smoke
    def test_page_title_assertion(self, driver):
        """Verify page title contains 'Google'."""
        title = self.page.get_page_title()
        assert "Google" in title, f"Expected 'Google' in title, got: {title}"
    
    @pytest.mark.smoke
    def test_search_box_is_visible(self, driver):
        """Verify the search box element is visible."""
        logger.info("Starting test: Search Box Visibility Assertion")
        
        is_visible = self.page.is_search_box_visible()
        
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
