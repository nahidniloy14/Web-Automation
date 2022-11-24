import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
serviceObject = Service("C:\Driver\chromedriver107.exe")
driver = webdriver.Chrome(service=serviceObject)

driver.get("https://rahulshettyacademy.com/client")
#traversing using X Path

# (//form/div/input)[1]
# //form ----- parent tag
# /div ---- first order child
# /input --- second order child
#[1]----correct order
driver.find_element(By.XPATH,"(//form/div/input)[1]").send_keys("demo@gmail.com")
time.sleep(3)


#traversing using CSS selector
#form div:nth-child(2) input
driver.find_element(By.CSS_SELECTOR,"form div:nth-child(2) input").send_keys("1414")
time.sleep(3)

driver.find_element(By.CSS_SELECTOR,"#login").click() #id is used
#driver.find_element(By.XPATH,"//div[@class='container']/form/div[1]/input")


