import json
import os
import logging
import time
from datetime import datetime
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

@pytest.mark.usefixtures("setup_teardown")
class BaseTest:
    driver: WebDriver = None

    @pytest.fixture(scope="class", autouse=True)
    def setup_teardown(self, request):
        """Setup and teardown handled inside BaseTest"""
        chrome_options = Options()
        chrome_options.add_argument('--start-maximized')
        chrome_options.add_argument('--disable-extensions')
        chrome_options.add_argument('--disable-popup-blocking')
        chrome_options.add_argument('--disable-infobars')
        chrome_options.add_argument('--guest')

        prefs = {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection_enabled": False
        }
        chrome_options.add_experimental_option("prefs", prefs)

        driver = webdriver.Chrome(options=chrome_options)
        # Load credentials
        creds_path = r"creds/creds.json"

        with open(creds_path, "r") as f:
            self.creds = json.load(f)
        request.cls.driver = driver
        yield
        driver.quit()

    # --- Helpers ---
    def open_url(self, url):
        self.driver.get(url)
        logger.info(f"Opened URL: {url}")

    def get_page_title(self):
        title = self.driver.title
        logger.info(f"Title: {title}")
        return title

    def wait_for_element(self, locator, timeout=10):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            logger.info(f"Element located at {locator}")
            return element
        except Exception as e:
            logger.error(f"Element not found at {locator} | error: {e}")
            self.take_screenshot("element_not_found")
            raise

    def take_screenshot(self, name="screenshot"):
        """Save screenshot and register it for pytest-html report."""
        date = time.strftime("%d_%m_%Y_%H_%M_%S")
        homedir = os.getcwd()
        source_path = os.path.join(homedir, "screenshots")
        os.makedirs(source_path, exist_ok=True)

        ss_name = f"{name}_{date}.png"
        full_path = os.path.join(source_path, ss_name)

        log_msg = f"Saving screenshot as {full_path}"
        logger.info(log_msg)

        if not hasattr(self, "screenshots"):
            self.screenshots = []
        self.screenshots.append(ss_name)

        try:
            ss_created = self.driver.save_screenshot(full_path)
            if not ss_created:
                logger.warning("Could not screenshot")
        except Exception as e:
            logger.error(f"Screenshot failed: {e}")
