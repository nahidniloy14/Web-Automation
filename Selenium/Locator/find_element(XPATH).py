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

#------Multiple X Path Matching---------
# (//input[@type='text'])[3]
# simply put the Xpath in the bracket and initialize the row number
# by default it starts from top left
driver.find_element(By.XPATH,"(//input[@type='text'])[3]")


#X PATH Using Text
#//p[text()='Don't have an account?']
driver.find_element(By.XPATH,"//p[text()='Don't have an account?']")

