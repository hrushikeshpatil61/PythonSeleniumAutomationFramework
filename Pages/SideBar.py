import time

from selenium.webdriver.common.by import By

from Locators.Locators import Locators


class SideBar:

    def __init__(self, driver):
        self.driver = driver

    def open_side_bar(self):
        time.sleep(2)
        self.driver.find_element(By.ID, Locators.sidebar_menu_button_id).click()
        time.sleep(2)

    def close_side_bar(self):
        time.sleep(2)
        self.driver.find_element(By.ID, Locators.sidebar_cross_button_id).click()

    def all_items(self):
        self.driver.find_element(By.ID, Locators.sidebar_link1_all_items).click()

    def about(self):
        self.driver.find_element(By.ID, Locators.sidebar_link2_about).click()

    def logout(self):
        self.driver.find_element(By.ID, Locators.sidebar_link3_logout).click()

    def reset_app_state(self):
        self.driver.find_element(By.ID, Locators.sidebar_link4_reset_app_states).click()

    def get_area_hidden_value(self):
        return self.driver.find_element(By.CLASS_NAME, Locators.sidebar_block_class_name).get_attribute(
            "aria-hidden")
