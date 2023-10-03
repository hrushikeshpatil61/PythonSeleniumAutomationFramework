from selenium.webdriver.common.by import By
from Locators.Locators import Locators


class Login:

    def __init__(self, driver):
        self.driver = driver

    def set_username(self, username):
        self.driver.find_element(By.ID, Locators.textbox_username_id).clear()
        self.driver.find_element(By.ID, Locators.textbox_username_id).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(By.ID, Locators.textbox_password_id).clear()
        self.driver.find_element(By.ID, Locators.textbox_password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.ID, Locators.button_login_id).click()

    def click_logout(self):
        self.driver.find_element(By.ID, Locators.button_logout_id).click()
