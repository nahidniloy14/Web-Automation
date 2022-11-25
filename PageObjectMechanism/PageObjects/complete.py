from selenium.webdriver.common.by import By

class page6:
    def __init__(self, driver):  # constructor
        self.driver = driver

    # message = driver.find_element(By.TAG_NAME, "h2").text
    com = (By.XPATH, "//div[@class='shopping_cart_container']")

    def complete(self):
        self.driver.find_element(*page6.com)
