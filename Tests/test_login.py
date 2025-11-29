import pytest
from Pages.Login.login_page import LoginPage
from Setup.base_test import BaseTest
from Pages.Login.Login_Props import TestData


@pytest.mark.usefixtures("setup")
class TestFoodManduLoginPage(BaseTest):
    def test_login_with_valid_credentials(self):
        self.open_url(TestData.BASE_URL)

        # Validate page title
        assert "foodmandu" in self.get_page_title().lower(), \
            f"Expected 'foodmandu' in title, got {self.get_page_title()}"

        # Login flow
        login_page = LoginPage(self.driver)
        login_page.click_login_FORM()  # If login requires popup
        login_page.enter_email(TestData.EMAIL)
        login_page.enter_password(TestData.PASSWORD)
        login_page.click_login()

        # Take screenshot after login
        self.take_screenshot("login_success")

        #  Assert current URL after login
        assert "foodmandu.com" in self.driver.current_url
