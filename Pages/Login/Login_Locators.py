from selenium.webdriver.common.by import By

class LoginLocators:
    LOGIN_FORM = (By.XPATH,'/html/body/header/div[2]/div/div[3]/ul/li[2]/button')
    EMAIL = (By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div[3]/form[1]/div/div[1]/input")
    PASSWORD = (By.XPATH, '/html/body/div[1]/div/div/div/div/div[2]/div[3]/form[1]/div/div[2]/input')
    LOGIN_BUTTON = (By.XPATH, '//*[@id="modal-body"]/form[1]/div/div[4]/button')
    ERROR_MESSAGE = (By.XPATH, "/html/body/section[2]/div/div/div/p")  # Edit based on UI


class HomeLocators:
    LOGOUT_BUTTON = (By.ID, "logout")
