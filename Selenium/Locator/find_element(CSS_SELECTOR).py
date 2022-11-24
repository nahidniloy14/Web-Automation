from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
#CSS selector
#tagname#valueofID[#tagname is optional]
driver.find_element(By.CSS_SELECTOR,"input#Email").clear()
driver.find_element(By.CSS_SELECTOR,"#Email").clear()

#tagclass
#tagname.valueofclass[#tagname is optional]
driver.find_element(By.CSS_SELECTOR,"input.password").clear()
driver.find_element(By.CSS_SELECTOR,".password").send_keys("1414")

#tag attribute
#tagname[attribute=value]
driver.find_element(By.CSS_SELECTOR,"[button type=submit]").click()

