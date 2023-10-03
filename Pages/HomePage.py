from selenium import webdriver
from selenium.webdriver.common.by import By
from Locators.Locators import Locators
from selenium.webdriver.support.ui import Select


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def get_all_products(self):
        products = self.driver.find_elements(By.CLASS_NAME, Locators.inventory_item_class_name)
        return products

    def total_number_of_products(self):
        return len(self.get_all_products())

    def get_all_product_names(self):
        product_name_elements = self.driver.find_elements(By.CLASS_NAME, Locators.product_item_name_class_name)
        product_names = [element.text for element in product_name_elements]
        return product_names

    def get_all_product_description(self):
        product_description_elements = self.driver.find_elements(By.CLASS_NAME,Locators.product_item_description_class_name)
        product_descriptions = [element.text for element in product_description_elements]
        return product_descriptions

    def get_all_product_prices_in_numbers(self):
        product_price_elements = self.driver.find_elements(By.CLASS_NAME, Locators.product_item_price_class_name)
        product_prices_text = [element.text for element in product_price_elements]
        prices_in_numbers = [float(price.strip("$")) for price in product_prices_text]
        return prices_in_numbers

    def open_product_details(self, element):
        element.find_element(By.TAG_NAME, "a").click()

    def get_one_product(self):
        return self.driver.find_element(By.CLASS_NAME, Locators.inventory_item_class_name)

    def add_to_cart(self, product):
        product.find_element(By.CLASS_NAME, Locators.add_to_cart_btn).click()

    def remove_from_cart(self, product):
        product.find_element(By.CLASS_NAME, Locators.add_to_cart_btn).click()

    def open_cart(self):
        self.driver.find_element(By.CLASS_NAME, Locators.shopping_cart_btn_class_name).click()

    def open_product_details(self, product):
        product.find_element(By.TAG_NAME, "a").click()

    def sort_by_name(self):
        sort_filter = self.driver.find_element(By.CLASS_NAME, Locators.sort_filter_class_name)
        select_obj = Select(sort_filter)
        select_obj.select_by_value("az")

    def reverse_sort_by_name(self):
        sort_filter = self.driver.find_element(By.CLASS_NAME, Locators.sort_filter_class_name)
        select_obj = Select(sort_filter)
        select_obj.select_by_value("za")

    def sort_by_price(self):
        sort_filter = self.driver.find_element(By.CLASS_NAME, Locators.sort_filter_class_name)
        select_obj = Select(sort_filter)
        select_obj.select_by_value("lohi")

    def reverse_sort_by_price(self):
        sort_filter = self.driver.find_element(By.CLASS_NAME, Locators.sort_filter_class_name)
        select_obj = Select(sort_filter)
        select_obj.select_by_value("hilo")

    def get_product_name(self, product):
        return product.find_element(By.CLASS_NAME, Locators.product_item_name_class_name).text

    def get_product_description(self, product):
        return product.find_element(By.CLASS_NAME, Locators.product_item_description_class_name).text

    def get_product_price(self, product):
        return product.find_element(By.CLASS_NAME, Locators.product_item_price_class_name).text
