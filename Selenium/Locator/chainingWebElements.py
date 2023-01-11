import time

import timer as timer
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serviceObject = Service("C:\Driver\chromedriver108.exe")

driver = webdriver.Chrome(service=serviceObject)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element(By.CLASS_NAME, "search-keyword").send_keys("ber")
time.sleep(5)
products = driver.find_elements(By.XPATH, "//div[@class='products']/div")
for product in products:
    product.find_element(By.XPATH, "div/button").click()

