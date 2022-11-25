from PageObjectMechanism.PageObjects.addToCart import page2
from PageObjectMechanism.PageObjects.complete import page6
from PageObjectMechanism.PageObjects.login import page1
from PageObjectMechanism.PageObjects.overview import page5
from PageObjectMechanism.PageObjects.yourCart import page3
from PageObjectMechanism.PageObjects.yourInfo import page4

from PageObjectMechanism.Utilities.baseClass import BaseClass
#@pytest.mark.usefixtures("setup") #inheited from BaseClass
class TestOne(BaseClass):
    def test_locator(self):
        #to access class variable in method we have to use self
        #self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        login1 = page1(self.driver)
        login1.username().send_keys("standard_user")
        login2 = page1(self.driver)
        login2.password().send_keys("secret_sauce")
        login3 = page1(self.driver)
        login3.login().click()
        atc1 = page2(self.driver)
        atc1.backpack().click()
        atc2 = page2(self.driver)
        atc2.bikelight().click()
        atc3 = page2(self.driver)
        atc3.container().click()
        # ----------Removing Object Creation every single time----
        # page3 = page2.checkout()
        co=page3(self.driver)
        co.checkout().click()
        n=page4(self.driver)
        n.firstName().send_keys("Nahid Hassan")
        l = page4(self.driver)
        l.lastName().send_keys("Niloy")
        p = page4(self.driver)
        p.postalCode().send_keys("1414")
        con = page4(self.driver)
        con.Continue().click()
        self.scroll(0,200)
        self.explicitWait(self)
        m= page5(self.driver)
        m.message().text()
        f=page5(self.driver)
        f.finish().click()
        com = page6(self.driver)
        com.complete().text()


