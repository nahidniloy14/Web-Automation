import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serviceObject = Service("C:\Driver\chromedriver107.exe")
#make sure you have downloaded the existing chrome version in your pc
driver = webdriver.Chrome(service=serviceObject)

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.NAME,"name").send_keys("Niloy")
driver.find_element(By.NAME,"email").send_keys("nahidniloysqa@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("1414")

driver.find_element(By.ID,"exampleCheck1").click()
time.sleep(3)

driver.close()