
from selenium.webdriver.common.by import By
class HomeLocators:
    SEARCH_BAR = (By.CSS_SELECTOR, "input#txtFoodSearch")
    ProductSection = (By.XPATH, "/html/body/div[2]/section[3]")
    First_Product = (By.XPATH, "/html/body/div[2]/section[3]/div/div/div[2]/div/div[1]/a/img")
    PRODUCT_TITLE = (By.XPATH, "/html/body/div[2]/section[3]/div/div/div[2]/div/div[2]")
    Product_Category=(By.XPATH, "/html/body/div[2]/section[3]/div/div/div[2]/div/div[3]")


