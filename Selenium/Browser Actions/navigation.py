from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.service import Service

serviceObject = Service("C:\Driver\chromedriver107.exe")
#make sure you have downloaded the existing chrome version in your pc
driver = webdriver.Chrome(service=serviceObject)


#forward navigation
driver.get("https://www.wikipedia.org/")#open this url in chrome
print(driver.title)#prints title of the url


#backward navigation
driver.get("https://www.quora.com/")#open this url in chrome
print(driver.title)#prints title of the url

driver.back()
print(driver.title)#prints title of the url
time.sleep(3) #sets timer{import}

driver.forward()
print(driver.title)#prints title of the url
time.sleep(5)

