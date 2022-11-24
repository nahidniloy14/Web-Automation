
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument("--ignore-certificate-errors")
serviceObject = Service("C:\Driver\chromedriver107.exe")
driver = webdriver.Chrome(service=serviceObject,options=chrome_options)

driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
#we wont see any browser opening in the headless mode
#all the process will be executed in the backend

