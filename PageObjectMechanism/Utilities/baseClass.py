import inspect
import logging

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class BaseClass:
    # dropdown method
    def dropdown(self, locator, text):
        dropdown = Select(locator)
        dropdown.select_by_visible_text(text)

    # explicit wait
    def explicitWait(self, text):
        element = WebDriverWait(self.driver, timeout=10).until(
            EC.presence_of_element_located((By.TAG_NAME, text)))

    # scroll
    def scroll(self, x, y):
        self.driver.execute_script("window.scrollTo(x,y)")
    # logging
    def getlogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(__name__)  # method to log everything#__name__ prints name
        fileHandler = logging.FileHandler('../logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s ")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)  # accept filehandler object #logger format and file
        logger.setLevel(logging.DEBUG)
        return logger

