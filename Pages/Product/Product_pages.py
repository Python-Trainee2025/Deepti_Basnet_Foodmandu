from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Pages.Product.Product_locators import ProductLocators
from Pages.Product.Product_Props import ProductData


class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    def click_category_by_name(self, name=None):
        if not name:
            name = ProductData.DEFAULT_CATEGORY  # <-- here we use DEFAULT_CATEGORY
        categories = self.driver.find_elements(*ProductLocators.CATEGORY_ITEM)
        for category in categories:
            if name.lower() in category.text.lower():
                category.click()
                break

    # Click the first product in the category
    def click_first_product(self):
        try:
            first_product = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable(ProductLocators.FIRST_PRODUCT)
            )
            first_product.click()
        except TimeoutException:
            self.driver.save_screenshot("click_first_product_failed.png")
            raise AssertionError("First product not clickable or not found. Screenshot saved.")

    # Get title of first product (optional)
    def get_first_product_title(self):
        return self.driver.find_element(*ProductLocators.PRODUCT_TITLE).text

    # Click Add to Cart on PDP
    # def click_add_to_cart(self):
    #     self.driver.find_element(*ProductLocators.ADD_TO_CART).click()
