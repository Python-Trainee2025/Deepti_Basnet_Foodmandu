from Pages.Login.Login_Locators  import LoginLocators, HomeLocators
from Pages.Login.Login_Props import LoginProps
from setup.base_test import BaseTest


class LoginPage(LoginProps):
    def __init__(self, driver):
        self.driver = driver

    def click_login_FORM(self):
        self.login.click()


    def enter_email(self, email):
        self.email.send_keys(email)  #update it like this or create a new method

    # def login_form(self, email, password): create a seperate method just for login if needed like this
    #     self.login.click()
    #     self.enter_email(email)
    #     # self.enter_password(password)

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
