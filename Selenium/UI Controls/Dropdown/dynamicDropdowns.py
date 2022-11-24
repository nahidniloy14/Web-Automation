from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.find_element(By.ID,"autosuggest").send_keys("ind")
time.sleep(2)
countries=driver.find_elements(By.XPATH,"//li[@class='ui-menu-item']/a ")#should be plural elements
print(len(countries))
time.sleep(2)
for country in countries:
    if country.text == "India":
        country.click()
        break

