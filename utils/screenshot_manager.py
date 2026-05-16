"""
Screenshot management utility for test failures and validation.
"""
import os
from datetime import datetime
from config.settings import SCREENSHOT_DIR
from utils.logger import LoggerManager

logger = LoggerManager.get_logger(__name__)


class ScreenshotManager:
    """Manages taking and storing screenshots."""
    
    @staticmethod
    def take_screenshot(driver, name="screenshot"):
        """
        Take a screenshot and save it.
        
        Args:
            driver: WebDriver instance
            name: Name for the screenshot file
            
        Returns:
            str: Path to the saved screenshot
        """
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{name}_{timestamp}.png"
            filepath = os.path.join(SCREENSHOT_DIR, filename)
            
            driver.save_screenshot(filepath)
            logger.info(f"Screenshot saved: {filepath}")
            
            return filepath
        except Exception as e:
            logger.error(f"Error taking screenshot: {str(e)}")
            return None
