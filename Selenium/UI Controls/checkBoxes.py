from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time
driver = webdriver.Chrome()
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")

checkboxes=driver.find_elements(By.XPATH,"//input[@type='checkbox']")
print (len(checkboxes))

time.sleep(5)
for checkbox in checkboxes:
        if checkbox.get_attribute("value") == "option2" :
                checkbox.click()
                checkbox.is_selected()#this method returns true or false
                break
