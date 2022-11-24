from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serviceObject = Service("C:\Driver\chromedriver107.exe")

driver = webdriver.Chrome(service=serviceObject)

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
#displayed or enabled
status=driver.find_element(By.NAME,"RESULT_TextField-1").is_displayed()
print(status)



