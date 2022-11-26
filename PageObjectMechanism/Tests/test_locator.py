from PageObjectMechanism.PageObjects.addToCart import page2
from PageObjectMechanism.PageObjects.complete import page6
from PageObjectMechanism.PageObjects.login import page1
from PageObjectMechanism.PageObjects.overview import page5
from PageObjectMechanism.PageObjects.yourCart import page3
from PageObjectMechanism.PageObjects.yourInfo import page4
from PageObjectMechanism.Utilities.baseClass import BaseClass
from PageObjectMechanism.Utilities.dataSet import getData
#@pytest.mark.usefixtures("setup") #inheited from BaseClass
class Test1(BaseClass,getData):
    def test_locator(self,getData):
        log=self.getlogger()
        #to access class variable in method we have to use self
        #self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        login1 = page1(self.driver)
        login1.username().send_keys("standard_user")
        login2 = page1(self.driver)
        login2.password().send_keys("secret_sauce")
        login3 = page1(self.driver)
        login3.login().click()
        log.info("Login Successfull")
        atc1 = page2(self.driver)
        atc1.backpack().click()
        atc2 = page2(self.driver)
        atc2.bikelight().click()
        atc3 = page2(self.driver)
        atc3.container().click()
        log.info("Product added to cart")
        # ----------Removing Object Creation every single time----
        # page3 = page2.checkout()
        co=page3(self.driver)
        co.checkout().click()
        n=page4(self.driver)
        #---------Implemented Data driven mechanism (Tuple)------
        n.firstName().send_keys("Nahid Hassan")
        # ---------Implemented Data driven mechanism (dictionary)------
        n.firstName().send_keys(getData["firstName"])
        n.firstName().send_keys(getData[0])
        l = page4(self.driver)
        l.lastName().send_keys("Niloy")
        l.lastName().send_keys(getData["lastName"])
        l.lastName().send_keys(getData[1])
        p = page4(self.driver)
        p.postalCode().send_keys("1414")
        p.postalCode().send_keys(getData[2])
        p.postalCode().send_keys(getData["postalCode"])
        con = page4(self.driver)
        con.Continue().click()
        self.scroll(0,200)
        self.explicitWait(self)
        m= page5(self.driver)
        message=m.message().text
        log.info("Product Bill"+message)
        assert "$43.18" in message
        f=page5(self.driver)
        f.finish().click()
        com = page6(self.driver)
        message2=com.complete().text
        log.info("Product is ready to delivar")
        assert "THANK YOU" in message2
        self.driver.refresh() #this is a way to fill up both the data sets
        self.driver.quit()





