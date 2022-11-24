from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time
driver = webdriver.Chrome()
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")

rb=driver.find_elements(By.XPATH,"//input[@name='radioButton']")
rb[2].click()
assert rb[2].is_selected()

