from _datetime import datetime
import logging
import os
import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Logging configuration
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

@pytest.mark.usefixtures("setup")
class BaseTest:
    driver: WebDriver
    def open_url(self, url):
        self.driver.get(url)
        logger.info(f"Opened URL: {url}")

    def get_page_title(self):
        title = self.driver.title
        logger.info(f"Title: {title}")
        return title

    def take_screenshot(self,name="screenshot"):
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        filename = f"{name}_{timestamp}.png"
        path=os.path.join(os.getcwd(),"screenshot")
        os.makedirs(path,exist_ok=True)
        full_path = os.path.join(path,filename)
        self.driver.save_screenshot(full_path)
        logger.info(f"Saved screenshot at {full_path}")
    def wait_for_element(self,locator,timeout=10):
        try:
            element=WebDriverWait(self.driver,timeout).until(EC.presence_of_element_located(locator))
            logger.info(f"Element located at {locator}")
            return element
        except Exception as e:
            logger.error(f"Element not found at {locator}| error: {e}")
            self.take_screenshot("element_not_found")
            raise