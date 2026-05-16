"""
WebDriver factory for creating and managing browser instances.
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from config.settings import BROWSER, HEADLESS
from utils.logger import LoggerManager
import os

logger = LoggerManager.get_logger(__name__)


class DriverFactory:
    """Factory class for creating WebDriver instances."""
    
    @staticmethod
    def create_driver():
        """
        Create and return a WebDriver instance.
        
        Returns:
            WebDriver: Configured WebDriver instance
        """
        headless_mode = os.getenv("HEADLESS", "True").lower() == "true"
        logger.info(f"Creating {BROWSER} driver (headless={headless_mode})...")
        
        if BROWSER == "chrome":
            return DriverFactory._create_chrome_driver(headless_mode)
        elif BROWSER == "firefox":
            return DriverFactory._create_firefox_driver(headless_mode)
        else:
            logger.error(f"Unsupported browser: {BROWSER}")
            raise ValueError(f"Unsupported browser: {BROWSER}")
    
    @staticmethod
    def _create_chrome_driver(headless=True):
        """Create a Chrome WebDriver instance."""
        options = ChromeOptions()
        
        if headless:
            options.add_argument("--headless=new")
        
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--disable-gpu")
        options.add_argument("--start-maximized")
        options.add_argument("--window-size=1920,1080")
        
        try:
            chromedriver_path = ChromeDriverManager().install()
            logger.info(f"Using ChromeDriver: {chromedriver_path}")
            service = ChromeService(chromedriver_path)
            driver = webdriver.Chrome(service=service, options=options)
        except Exception as e:
            logger.warning(f"Error with managed ChromeDriver: {e}. Trying system Chrome...")
            # Fallback to system Chrome if managed driver fails
            driver = webdriver.Chrome(options=options)
        
        logger.info("Chrome driver created successfully")
        return driver
    
    @staticmethod
    def _create_firefox_driver(headless=True):
        """Create a Firefox WebDriver instance."""
        options = FirefoxOptions()
        
        if headless:
            options.add_argument("--headless")
        
        try:
            geckodriver_path = GeckoDriverManager().install()
            service = FirefoxService(geckodriver_path)
            driver = webdriver.Firefox(service=service, options=options)
        except Exception as e:
            logger.warning(f"Error with managed GeckoDriver: {e}. Trying system Firefox...")
            driver = webdriver.Firefox(options=options)
        
        logger.info("Firefox driver created successfully")
        return driver
    
    @staticmethod
    def quit_driver(driver):
        """
        Close and quit the WebDriver instance.
        
        Args:
            driver: WebDriver instance to quit
        """
        try:
            if driver:
                driver.quit()
                logger.info("WebDriver quit successfully")
        except Exception as e:
            logger.error(f"Error quitting WebDriver: {str(e)}")
