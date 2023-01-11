from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

"""
wait = WebDriverWait(driver,5)
wait.until(EC.presence_of_element_located(driver.find_element(By.CSS_SELECTOR,".promoBtn")))
"""
"""
wait=WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_all_elements_located((By.CSS_SELECTOR,".promoInfo")))
"""

"""
driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2Fl")
el = WebDriverWait(driver, timeout=3).until(lambda d: d.driver.find_element(By.NAME,"Email").send_keys("niloy123@yourstore.com"))
"""