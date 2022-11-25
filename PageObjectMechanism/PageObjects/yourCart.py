from selenium.webdriver.common.by import By

class page3:
    def __init__(self, driver):  # constructor
        self.driver = driver
    # self.driver.find_element(By.CSS_SELECTOR, "#checkout").click()
    co = (By.XPATH, "//div[@class='shopping_cart_container']")

    def checkout(self):
        self.driver.find_element(*page3.co).click()
