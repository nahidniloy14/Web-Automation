import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serviceObject = Service("C:\Driver\chromedriver107.exe")
#make sure you have downloaded the existing chrome version in your pc
driver = webdriver.Chrome(service=serviceObject)

#XPATH
#//tagname[@attribute='value']

driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element(By.XPATH,"//input[@value='Submit']").click()
time.sleep(5)
#driver.find_element(By.XPATH,"//div[@class='container']/form/div[1]/input").send_keys("Nahid Hassan Niloy")

