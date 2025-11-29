
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from Pages.Home import Home_locators


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    #  Scroll to product section
    def scroll_to_product(self):
        try:
            WebDriverWait(self.driver, 20).until(
                lambda d: d.execute_script("return document.readyState") == "complete"
            )

            # Gradual scroll to trigger lazy loading
            for step in range(0, 5000, 500):
                self.driver.execute_script(f"window.scrollTo(0, {step});")
                WebDriverWait(self.driver, 1).until(lambda d: True)

            product_section = WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located(Home_locators.HomeLocators.PRODUCT_TITLE)
            )

            self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth'});", product_section)
            return product_section

        except TimeoutException:
            self.driver.save_screenshot("scroll_to_product_failed.png")
            raise AssertionError(" Product section not found within timeout. Screenshot saved.")

    #  Click first product
    def click_first_product(self):
        try:
            first_product = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(Home_locators.HomeLocators.First_Product)
            )
            self.driver.execute_script("arguments[0].click();", first_product)
        except TimeoutException:
            self.driver.save_screenshot("click_first_product_failed.png")
            raise AssertionError(" First product not clickable. Screenshot saved.")



