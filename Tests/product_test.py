import pytest

from Pages.Login.login_page import LoginPage
from Pages.Product.Product_Props import ProductData
from Pages.Product.Product_pages import ProductPage
# from Pages.Cart.Cart_Page import CartPage
from Setup.base_test import BaseTest


@pytest.mark.usefixtures("setup")
class TestProductPage(BaseTest):

    def test_select_first_product_from_category(self):
        self.open_url(ProductData.BASE_URL)

        product_page = ProductPage(self.driver)

        product_page.click_category_by_name()
        login_page=LoginPage(self.driver)
        login_page.click_login()

        # product_title = product_page.get_first_product_title()
        # print("Selected product:", product_title)


        # product_page.click_add_to_cart()

        # assert cart_page.is_product_in_cart(product_title), \
        #     f"Expected '{product_title}' to be in cart"

