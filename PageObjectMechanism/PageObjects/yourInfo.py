from selenium.webdriver.common.by import By

class page4:
    def __init__(self, driver):  # constructor
        self.driver = driver

    # driver.find_element(By.NAME, "firstName").send_keys("Nahid Hassan")
    # driver.find_element(By.NAME, "lastName").send_keys("Niloy")
    # driver.find_element(By.NAME, "postalCode").send_keys("1414")
    #driver.find_element(By.ID, "continue").click()

    n=(By.NAME, "firstName")
    l=(By.NAME, "lastName")
    p=(By.NAME, "postalCode")
    con=(By.ID, "continue")

    def firstName(self):
        self.driver.find_element(*page4.n)

    def lastName(self):
        self.driver.find_element(*page4.l)

    def postalCode(self):
        self.driver.find_element(*page4.p)

    def Continue(self):
        self.driver.find_element(*page4.con)

    # name = (By.CSS_SELECTOR,"input[name='name']")
    # gender=(By.ID,"exampleFormControlSelect1")

    # pw = (By.ID, "password")
    # loginbtn = (By.ID, "login-button")

    # def username(self):
    #     return self.driver.find_element(*page1.un)  # * will read the particular variable as a tuple
    #
    # def password(self):
    #     return self.driver.find_element(*page1.pw)  # * will read the particular variable as a tuple
    #
    # def login(self):
    #     return self.driver.find_element(*page1.loginbtn)

    # def getname(self):
    #     return self.driver.find_element(*page4.name)

    # def getgender(self):
    #     return self.driver.find_element(*page4.gender)




