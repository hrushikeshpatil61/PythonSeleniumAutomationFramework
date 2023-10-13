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


@pytest.fixture()
def setup(browser):
    print(browser)
    if (browser == "chrome"):
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()

    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--username")
    parser.addoption("--password")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


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
