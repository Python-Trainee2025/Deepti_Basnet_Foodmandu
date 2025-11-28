from selenium.webdriver.common.by import By


class ProductLocators:
    # Category list on homepage
    CATEGORY_ITEM = (By.XPATH, "/html/body/div[3]/section[3]/div[2]/div[1]/div/div[2]/div[3]")

    # First product in category
    FIRST_PRODUCT = (By.XPATH, "/html/body/div[3]/section[3]/div[2]/div[1]/div/div[2]/div[3]/div[1]/ul/li[1]")

    # Product title inside category listing (optional)
    # PRODUCT_TITLE = (By.XPATH, '//*[@id="Product"]/div[1]/a')

    # Add to cart button on PDP
    # ADD_TO_CART = (By.CSS_SELECTOR, ".btn-add-to-cart, button.add-to-cart")
