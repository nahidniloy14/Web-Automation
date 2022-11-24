import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

serviceObject = Service("C:\Driver\chromedriver107.exe")

driver = webdriver.Chrome(service=serviceObject)

driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")

driver.get_screenshot_as_file("screenshot.png")
