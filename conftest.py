import os

from selenium import webdriver
import pytest
import pytest_html

from Pages.ReportUtils import ReportUtils


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
