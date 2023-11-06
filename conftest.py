import os
from selenium import webdriver
import pytest
import pytest_html
from Pages.Cart import Cart
from Pages.HomePage import HomePage
from Pages.Login import Login
from Pages.ReportUtils import ReportUtils
from Pages.SideBar import SideBar
from Pages.XLUtils import XLUtils
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--username")
    parser.addoption("--password")


@pytest.fixture(scope="class")
def get_driver(request):
    browser_name = request.config.getoption("--browser")

    if browser_name == "chrome":
        ser_obj = Service("Drivers/chromedriver.exe")  # Current Chromedriver version : 119.0.6045.105
        driver = webdriver.Chrome(service=ser_obj)
    elif browser_name == "firefox":
        ser_obj = Service("Drivers/geckodriver.exe")
        driver = webdriver.Firefox(service=ser_obj)
    elif browser_name == "edge":
        ser_obj = Service("Drivers/msedgedriver.exe")
        driver = webdriver.Edge(service=ser_obj)       # Current Edge driver version :  119.0.2151.44
    else:
        ser_obj = Service("Drivers/chromedriver.exe")  # Current Chromedriver version : 119.0.6045.105
        driver = webdriver.Chrome(service=ser_obj)

    yield driver
    driver.quit()


@pytest.fixture
def username(request):
    return request.config.getoption("--username")


@pytest.fixture
def password(request):
    return request.config.getoption("--password")

# @pytest.fixture(autouse=True)
# def load_resources(cls):
#     cls.driver.implicitly_wait(10)
#     cls.lp = Login(cls.driver)
#     cls.xlutils = XLUtils(cls.driver)
#     cls.sb = SideBar(cls.driver)
#     cls.cart = Cart(cls.driver)
#     cls.homepage = HomePage(cls.driver)
