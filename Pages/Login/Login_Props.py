from Pages.Login.Login_Locators import LoginLocators


class LoginProps(LoginLocators):


    @property
    def login(self):
        return self.driver.find_element(*LoginLocators.LOGIN_FORM)


    @property
    def email(self):
        return self.driver.find_element(*LoginLocators.EMAIL)