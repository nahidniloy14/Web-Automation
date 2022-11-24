from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serviceObject = Service("C:\Driver\chromedriver107.exe")
driver = webdriver.Chrome(service=serviceObject)

driver.get("https://rahulshettyacademy.com/client")
#any thing with tag <a   > is called link
#<a _ngcontent-vqb-c43="" class="forgot-password-link" href="/client/auth/password-new">Forgot password?</a>
#forgot-password-link is the link text here
driver.find_element(By.LINK_TEXT,"forgot-password-link").click()
driver.find_element(By.PARTIAL_LINK_TEXT,"forgot").click()
#driver.quit()  # closes all the tab after execution

