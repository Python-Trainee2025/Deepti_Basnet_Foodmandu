import time

import  pytest
from Pages.Login.login_page import LoginPage
from Setup.base_test import BaseTest
from Pages.Login.Login_Props import TestData

@pytest.mark.usefixtures("setup")
class TestLoginNegative(BaseTest):
    def test_login_invalid_password(self):
        self.open_url(TestData.BASE_URL)
        driver = self.driver
        login_page = LoginPage(driver)
        login_page.click_login_FORM()
        login_page.enter_email(TestData.EMAIL)
        login_page.enter_password(TestData.Invalid_Password)
        self.take_screenshot("Invalid Password")
        login_page.click_login()
        time.sleep(5)


        assert "foodmandu.com" in self.driver.current_url
        error_text = login_page.get_error_message()
        assert "Invalid login attempt" in error_text, f"Unexpected error message: {error_text}"

    def test_login_invalidEmail(self):
        self.open_url(TestData.BASE_URL)
        driver = self.driver
        login_page = LoginPage(driver)
        login_page.click_login_FORM()
        login_page.enter_email(TestData.Invalid_Email)
        login_page.enter_password(TestData.PASSWORD)
        self.take_screenshot("Invalid Email")
        login_page.click_login()
        time.sleep(5)


        assert "foodmandu.com" in self.driver.current_url
        error_text = login_page.get_error_message()

