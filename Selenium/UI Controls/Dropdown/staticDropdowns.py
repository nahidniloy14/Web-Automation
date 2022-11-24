import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

serviceObject = Service("C:\Driver\chromedriver107.exe")

driver = webdriver.Chrome(service=serviceObject)

driver.get("https://rahulshettyacademy.com/angularpractice/")
#static options are fixed like(male,female)

driver.find_element(By.ID,"exampleFormControlSelect1").click()
#select class provides the method to handle the options of dropdown
dropdown=Select(driver.find_element(By.ID,"exampleFormControlSelect1"))#select must be present in the inspect{import}
time.sleep(5)
dropdown.select_by_visible_text("Female")
#time.sleep(5)
#dropdown.select_by_index(0)#male
#dropdown.select_by_value("Female)#if present