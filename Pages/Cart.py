from selenium.webdriver.common.by import By
from Locators.Locators import Locators


class Cart:
    cart_items_class_name = "cart-item"
    cart_badge_count_class_name = "shopping_cart_badge"

    def __init__(self, driver):
        self.driver = driver

    def get_cart_items(self):
        return self.driver.find_elements(By.CLASS_NAME, "cart_item")

    def cart_items_length(self):
        return len(self.get_cart_items())

    def cart_badge_count_number(self):
        cart_badge_count_element = self.driver.find_elements(By.CLASS_NAME, self.cart_badge_count_class_name)
        if (len(cart_badge_count_element) == 0):
            return 0
        else:
            return cart_badge_count_element[0].text

    def continue_shopping_btn_get_text(self):
        continue_shopping_btn = self.driver.find_element(By.ID, Locators.shopping_cart_continue_shopping_btn)
        return continue_shopping_btn.text

    def continue_shopping_btn_open(self):
        self.driver.find_element(By.ID, Locators.shopping_cart_continue_shopping_btn).click()

    def get_product_name(self, product):
        return product.find_element(By.CLASS_NAME, Locators.product_item_name_class_name).text

    def get_product_description(self, product):
        return product.find_element(By.CLASS_NAME, Locators.product_item_description_class_name).text

    def get_product_price(self, product):
        return product.find_element(By.CLASS_NAME, Locators.product_item_price_class_name).text
