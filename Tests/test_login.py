import pytest
from Pages.Login.login_page import LoginPage
from setup.base_test import BaseTest


# @pytest.mark.usefixtures("setup") #no need to use fixtures
class TestFoodManduLoginPage(BaseTest):
    def test_login_with_valid_credentials(self):
        # Open website using BaseTest method
        url=self.creds['BASE_URL']
        self.open_url(url)

        # Validate page title
        assert "foodmandu" in self.get_page_title().lower(), \
            f"Expected 'foodmandu' in title, got {self.get_page_title()}"

        # Login flow
        login_page = LoginPage(self.driver)
        login_page.click_login_FORM()  # If login requires popup
        email=self.creds['EMAIL']
        password=self.creds['PASSWORD']
        login_page.enter_email("iuyiiuiuhhihui")
        login_page.enter_password(password)
        '''
        after login ensure you verify the home page loads,, right now it passes regardless of it logging in or not
        '''
        login_page.click_login()


        # Take screenshot after login
        # self.take_screenshot("login_success")

        # Optional: Assert current URL after login
        # assert "foodmandu.com" in self.driver.current_url
