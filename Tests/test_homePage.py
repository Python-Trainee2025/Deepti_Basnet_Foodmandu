import pytest
from Pages.Home.Home_props import FoodSearch
from Pages.Home.Home_page import HomePage
from Tests.base_test import BaseTest

@pytest.mark.usefixtures("setup")
class TestHomePage(BaseTest):

    def test_home_page(self):
        self.open_url(FoodSearch.Base_url)
        assert "foodmandu" in self.get_page_title().lower(), \
            f"Expected 'foodmandu' in title, got {self.get_page_title()}"

        home_page = HomePage(self.driver)

        # 2 Scroll to product list
        home_page.scroll_to_product()

        # Click first product
        home_page.click_first_product()


