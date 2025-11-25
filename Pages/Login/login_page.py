from Pages.Login.Login_Locators  import LoginLocators, HomeLocators
from Pages.Login.Login_Props import TestData

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def click_login_FORM(self):
        self.driver.find_element(*LoginLocators.LOGIN_FORM).click()

    def enter_email(self, email):
        self.driver.find_element(*LoginLocators.EMAIL).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*LoginLocators.PASSWORD).send_keys(password)

    def click_login(self):
        self.driver.find_element(*LoginLocators.LOGIN_BUTTON).click()

    def get_error_message(self):
        return self.driver.find_element(*LoginLocators.ERROR_MESSAGE).text


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def click_logout(self):
        self.driver.find_element(*HomeLocators.LOGOUT_BUTTON).click()
