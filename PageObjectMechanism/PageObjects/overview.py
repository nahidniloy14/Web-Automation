from selenium.webdriver.common.by import By


class page5:
    def __init__(self, driver):  # constructor #it will provide self for line 13,16,19
        self.driver = driver

    # message = driver.find_element(By.CSS_SELECTOR, ".summary_total_label").text
    # assert "$43.18" in message
    # driver.find_element(By.NAME, "finish").click()
    m = (By.CSS_SELECTOR, ".summary_total_label")
    f = (By.NAME, "finish")

    def message(self):
        self.driver.find_element(*page5.m)

    def finish(self):
        self.driver.find_element(*page5.f)
