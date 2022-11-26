# if we declare our fixture that fixture will be present to all testcases present in that particular fixture

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver = None  # should intialize this to take ss


@pytest.fixture(scope="class")
def setup(request):
    serviceObject = Service("C:\Driver\chromedriver107.exe")
    driver = webdriver.Chrome(service=serviceObject)
    driver.get("https://www.saucedemo.com/")
    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver = driver  # assinging local driver of this fixture to the class driver
    yield
    driver.close()

    # -----------Take screenshot out of html report----------


