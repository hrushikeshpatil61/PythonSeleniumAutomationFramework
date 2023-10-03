from selenium.webdriver.common.by import By
from Locators.Locators import Locators

class ProductDetails:
    def __init__(self, driver):
        self.driver = driver

    def get_product_name(self):
        return self.driver.find_element(By.CLASS_NAME, Locators.product_details_name_class_name).text

    def get_product_description(self):
        return self.driver.find_element(By.CLASS_NAME, Locators.product_details_description_class_name).text

    def get_product_price(self):
        return self.driver.find_element(By.CLASS_NAME, Locators.product_details_price_class_name).text