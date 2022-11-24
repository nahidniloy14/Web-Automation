import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

serviceObject = Service("C:\Driver\chromedriver107.exe")

driver = webdriver.Chrome(service=serviceObject)

driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")

# window.scrollBy(0,document.body.scrollHeight) #this is a java script code
#driver.execute_script() is a method to run java script method

#scrolls all the way to the bottom
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);")
time.sleep(5)
#scrolls to the needed portion
# driver.execute_script("window.scrollBy(0,500);")
