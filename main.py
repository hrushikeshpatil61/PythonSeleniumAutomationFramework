import os
import time
import unittest

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import sys
from Locators.Locators import Locators
from Pages.Cart import Cart
from Pages.HomePage import HomePage
from Pages.Login import Login
from Pages.ProductDetails import ProductDetails
from Pages.SideBar import SideBar
from Pages.XLUtils import XLUtils
import allure
from allure_commons.types import AttachmentType


# unittest.TestCase

class TestCases:
    ser_obj = Service("Drivers/chromedriver.exe")
    driver = webdriver.Chrome(service=ser_obj)

    @classmethod
    def setup_class(cls):
        cls.driver.implicitly_wait(10)  # Implicit wait set at the class level

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    # @pytest.fixture()
    def test_001_login_by_excel(self):
        self.driver.get(Locators.baseURL)
        self.lp = Login(self.driver)
        self.xlutils = XLUtils(self.driver)
        username = self.xlutils.get_data(Locators.login_data_file_path, "Sheet1", 1, 1)
        password = self.xlutils.get_data(Locators.login_data_file_path, "Sheet1", 1, 2)
        self.lp.set_username(username)  # "standard_user" passing username into inputtext
        self.lp.set_password(password)  # "secret_sauce"  passing password into inputtext
        time.sleep(2)
        self.lp.click_login()  # call login function
        time.sleep(2)
        # after login browser will open HomePage below we are asserting if we are currently in homepage
        assert self.driver.current_url == Locators.all_items_URL, "Login failed"
        self.sb = SideBar(self.driver)
        self.sb.open_side_bar()
        self.sb.logout()

    def test_01_login_by_command_line(self, username, password):
        self.driver.get(Locators.baseURL)
        self.lp = Login(self.driver)
        self.lp.set_username(username)  # "standard_user" passing username into inputtext
        self.lp.set_password(password)  # "secret_sauce"  passing password into inputtext
        self.lp.click_login()  # call login function
        screenshot_path = "Screenshots/login.png"
        allure.attach(self.driver.get_screenshot_as_png(), name=screenshot_path, attachment_type=AttachmentType.PNG)
        assert self.driver.current_url == Locators.all_items_URL, "Login failed"

    def test_2_varify_application_name_text(self):
        # varify if application name is displayed properly without spelling-mistake
        assert "Swag Labs" == self.driver.find_element(By.CLASS_NAME,
                                                       Locators.app_logo_class_name).text, "Application name is wrong!"
        time.sleep(2)

    def test_03_open_and_close_sidebar_menu(self):
        # Test whether sidebar is properly opening and closing!
        self.sb = SideBar(self.driver)
        # calling open_side_bar function of class SideBar
        self.sb.open_side_bar()
        # checking that after opening sidebar value of area_hidden attribute is updated to false
        assert self.sb.get_area_hidden_value() == "false", "Enable to open SideBar from Menu options button!"
        time.sleep(1)  # if not waited then elementClickInterception error will occur!
        # closing sidebar using object of class SideBar
        self.sb.close_side_bar()
        # after closing sidebar checking if value of area_hidden attribute is updated to true or not!
        assert self.sb.get_area_hidden_value() == "true", "Enable to close SideBar from Menu cross button!"

    def test_04_validate_sidebar_link1_all_items(self):
        # create object of sidebar class
        self.sb = SideBar(self.driver)
        # open sidebar class
        self.sb.open_side_bar()
        time.sleep(2)
        # click on sidebar button all items
        self.sb.all_items()
        # close sidebar
        self.sb.close_side_bar()
        # validate whether current opened page is equal to all items page
        assert self.driver.current_url == Locators.all_items_URL, "Enable to open All Items tab from SideBar Menu!"
        time.sleep(2)

    def test_05_validate_sidebar_link_about(self):
        # create object of SideBar class and call method open sidebar!
        self.sb = SideBar(self.driver)
        self.sb.open_side_bar()
        time.sleep(1)
        # click about button from sidebar menu
        self.sb.about()
        # check if about page is opened by asserting with aboutURL
        if self.driver.current_url != Locators.aboutURL:
            self.sb.close_side_bar()
            assert "Enable to open About page from SideBar Menu!"
        # go back to main page
        self.driver.back()
        # close sidebar
        self.sb.close_side_bar()
        time.sleep(2)

    def test_06_validate_sidebar_link_reset_app_state(self):
        #  Create object of HomePage, SideBar, Cart classes
        self.cart = Cart(self.driver)
        self.homepage = HomePage(self.driver)
        self.sb = SideBar(self.driver)
        #  Retrieve one product from products inventory
        product_1 = self.homepage.get_one_product()
        #  add product to cart
        self.homepage.add_to_cart(product_1)
        self.sb.open_side_bar()
        time.sleep(1)
        #  Click app reset button
        self.sb.reset_app_state()
        time.sleep(2)
        #  close sidebar
        self.sb.close_side_bar()
        #  Varify if all cart is empty or not
        assert self.cart.cart_items_length() == 0, "Enable to reset cart items to zero!"
        assert self.cart.cart_badge_count_number() == 0, "Enable to reset Cart badge count icon to zero!"

    def test_07_varify_open_cart_page(self):
        #  Create object of HomePage class
        self.homepage = HomePage(self.driver)
        #  open cart page
        self.homepage.open_cart()
        time.sleep(2)
        #  check whether cart page is opened or not by validating URL
        assert self.driver.current_url == Locators.cart_URL, "Enable to open cart page from main-page!"
        self.driver.back()

    def test_08_varify_ascending_sorting_filter_by_name(self):
        #  create object of HomePage class
        self.homepage = HomePage(self.driver)
        #  call sort by name function
        self.homepage.sort_by_name()
        time.sleep(2)
        #  get all product list from HomePage
        all_products_name_list = self.homepage.get_all_product_names()
        #  assert if products are sorted according to selected filter or not
        assert all_products_name_list == sorted(
            all_products_name_list), "Enable to sort products in ascending order of names!"

    def test_09_varify_descending_sorting_filter_by_name(self):
        #  create object of HomePage
        self.homepage = HomePage(self.driver)
        #  call reverse sort by name function
        self.homepage.reverse_sort_by_name()
        #  get all product list from HomePage
        all_products_name_list = self.homepage.get_all_product_names()
        time.sleep(2)
        #  assert if products are sorted according to selected filter or not
        assert all_products_name_list == sorted(all_products_name_list,
                                                reverse=True), "Enable to sort products in reverse order of names!"

    def test_10_varify_ascending_sorting_filter_by_prices(self):
        #  create object of HomePage
        self.homepage = HomePage(self.driver)
        #  call function sort by price
        self.homepage.sort_by_price()
        #  get all product list from HomePage
        all_products_price_list = self.homepage.get_all_product_prices_in_numbers()
        time.sleep(2)
        #  assert if products are sorted according to selected filter or not
        assert all_products_price_list == sorted(
            all_products_price_list), "Enable to sort products by price low to high!"

    def test_11_varify_descending_sorting_filter_by_prices(self):
        #  create object of HomePage
        self.homepage = HomePage(self.driver)
        #  call function reverse sort by price
        self.homepage.reverse_sort_by_price()
        #  get all product list from HomePage
        all_products_price_list = self.homepage.get_all_product_prices_in_numbers()
        time.sleep(2)
        #  assert if products are sorted according to selected filter or not
        assert all_products_price_list == sorted(all_products_price_list,
                                                 reverse=True), "Enable to sort products from price high to low!"

    def test_12_varify_cart_page_back_button_continue_shopping(self):
        #  create object of HomePage, Cart classes
        self.homepage = HomePage(self.driver)
        self.cart = Cart(self.driver)
        #  open cart from homepage
        self.homepage.open_cart()
        time.sleep(1)
        #  get text of continue shopping button using get text method for validation
        continue_shopping_btn_text = self.cart.continue_shopping_btn_get_text()
        #  open continue shopping button
        self.cart.continue_shopping_btn_open()
        #  assert continue shopping button text is proper or not
        assert continue_shopping_btn_text == "Continue Shopping", "Text of shopping cart btn is changed!"
        #  assert if continue shopping button when clicked direct to MainPage
        assert Locators.all_items_URL == self.driver.current_url, "Enable to go back to main Page from Cart_Continue_Shopping button!"

    def test_13_varify_add_to_cart_and_and_remove_from_cart_main_page(self):
        #  create object of HomePage, Cart classes
        self.homepage = HomePage(self.driver)
        self.cart = Cart(self.driver)
        #  get total number of products for iterating, and adding to cart
        total_products_len = self.homepage.total_number_of_products()
        for index in range(total_products_len):  # range function gives list of numbers specified starting from 0
            time.sleep(1)
            # fetching all products by calling function
            products_list = self.homepage.get_all_products()
            # store name, description, price of each product to varify with cart page
            product_name = self.homepage.get_product_name(products_list[index])
            product_desc = self.homepage.get_product_description(products_list[index])
            product_price = self.homepage.get_product_price(products_list[index])
            #  add product to cart
            self.homepage.add_to_cart(products_list[index])
            #  open cart page to varify product data is same in cart page
            self.homepage.open_cart()
            #  fetch cart items
            cart_list = self.cart.get_cart_items()
            #  fetch currently added item from cart using index and get data
            cart_product_name = self.cart.get_product_name(cart_list[index])
            cart_product_desc = self.cart.get_product_description(cart_list[index])
            cart_product_price = self.cart.get_product_price(cart_list[index])
            #  varify data of product same on cart page and home page
            assert product_name == cart_product_name, "product name does not match with cart!"
            assert product_desc == cart_product_desc, "product description does not match with the cart!"
            assert product_price == cart_product_price, "product price does not match with the cart!"
            self.driver.back()
            #  varify for all elements using loop -> remove cart item from home page should update cart page
        for index in range(total_products_len - 1, -1, -1):
            time.sleep(1)
            products_list = self.homepage.get_all_products()
            # remove cart item from homepage remove button
            self.homepage.remove_from_cart(products_list[index])
            # open cart and see length of cart is updated or not
            self.homepage.open_cart()
            cart_items_length = self.cart.cart_items_length()
            assert cart_items_length == index, "Enable to remove cart_item from main page remove button!"
            self.driver.back()

    def test_14_varify_details_of_product_from_home_to_product_details_page(self):
        self.homepage = HomePage(self.driver)
        #  get count of products for adding one by one to cart
        total_products = self.homepage.total_number_of_products()
        for index in range(total_products):
            time.sleep(1)
            products_list = self.homepage.get_all_products()
            #  store details of each product for verifying with product detials page data
            product_name = self.homepage.get_product_name(products_list[index])
            product_desc = self.homepage.get_product_description(products_list[index])
            product_price = self.homepage.get_product_price(products_list[index])
            #  opening product details page
            self.homepage.open_product_details(products_list[index])
            time.sleep(1)

            #  getting product data from product details page
            self.productDetails = ProductDetails(self.driver)
            product_details_product_name = self.productDetails.get_product_name()
            product_details_product_desc = self.productDetails.get_product_description()
            product_details_product_price = self.productDetails.get_product_price()

            # verification of data from product details page to home page
            assert product_name == product_details_product_name, "Product name does not match!"
            assert product_desc == product_details_product_desc, "Product description does not match!"
            assert product_price == product_details_product_price, "Product price does not match!"
            self.driver.back()

    def test_16_validate_data_from_xl_file(self):
        self.xlutils = XLUtils(self.driver)
        self.homepage = HomePage(self.driver)
        rows, columns = self.xlutils.get_row_col_count(Locators.product_name_data_file_path, "Sheet1")
        product_name_list = self.homepage.get_all_product_names()
        for r in range(1, rows + 1):
            data = self.xlutils.get_data(Locators.product_name_data_file_path, "Sheet1", r, 1)
            assert data == product_name_list[r - 1], "UI data does not match with excel sheet!"

    def test_17_write_data_from_ui_to_xl_file(self):
        self.xlutils = XLUtils(self.driver)
        self.homepage = HomePage(self.driver)
        product_description_list = self.homepage.get_all_product_description()
        rows, columns = self.xlutils.get_row_col_count(Locators.product_name_data_file_path, "Sheet1")
        for r in range(1, rows + 1):
            data = product_description_list[r - 1]
            self.xlutils.write_data(Locators.product_name_data_file_path, "Sheet1", r, 2, data)

    def test_15_validate_sidebar_link_logout(self):
        # create object of sidebar
        self.sb = SideBar(self.driver)
        # open sidebar using sidebar object
        self.sb.open_side_bar()
        time.sleep(2)
        # click on logout button from sidebar
        self.sb.logout()
        # assert after logout page
        assert self.driver.current_url == Locators.baseURL, "Enable to logout from SideBar Menu!"
        time.sleep(2)

    # def test_11_varify_app_logo_text_at_center(self):
    #     app_logo = self.driver.find_element(By.CLASS_NAME, "app_logo")
    #     app_logo_location = app_logo.location
    #     window_width = self.driver.execute_script("return window.innerWidth")
    #     window_center = window_width / 2
    #     assert app_logo_location["x"] == window_center, "app logo text is not at the center of the screen!"
