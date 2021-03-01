from pages.LoginPage import loginPage
from pages.HomePage import homePage
from pages.CustSearchPage import custSearchPage
from pages.AddCustPage import addCustPage
from configurations.config import Config
from utils.customLogger import LogGen
from utils.commonUtils import Common_Utils as cu
from time import sleep
import pytest


class Test_Add_Customer:

    baseUrl = Config.appUrl
    uname = Config.username
    pwd = Config.password
    
    logger = LogGen.logGen()
    
    @pytest.mark.sanity
    @pytest.mark.regression
    def test_add_customer(self, setUp):
        
        self.logger.info("************ Test_Add_Customer **************")
        self.driver = setUp
        self.driver.maximize_window()
        self.driver.get(self.baseUrl)
        
        self.lp = loginPage(self.driver)
        self.lp.enterUsername(self.uname)
        self.lp.enterPassword(self.pwd)
        self.lp.clickOnLoginButton()
        
        self.logger.info("************ Starting Add Customer Test **************")
        
        self.hp = homePage(self.driver)
        self.hp.clickOnCustMainMenu()
        self.hp.clickOnCustSubMenu()
        
        self.custsearch = custSearchPage(self.driver)
        self.custsearch.clickOnAddNewBtn()
        
        self.addcust = addCustPage(self.driver)
        self.email = cu.random_generator(self) + "@gmail.com"
        self.addcust.enterCustEmail(self.email)
        self.addcust.enterCustPassword("test123")
        self.addcust.enterFirstName("Bobby")
        self.addcust.enterLastName("Fischer")
        self.addcust.selectGender("Male")
        self.addcust.enterDOB("09/03/1943")
        self.addcust.enterCompany("Chess Base")
        self.addcust.checkTaxExempt()
        self.addcust.selectNewsletter("Test store 2")
        self.addcust.selectCustRoles("Guests")
        self.addcust.selectManagerOfVendors("Vendor 1")
        self.addcust.checkActive()
        self.addcust.enterAdminComment("Customer details entered")
        
        sleep(2)
        self.addcust.clickOnSaveBtn()
        
        self.logger.info("************ Saving Customer Info **************")
        
        self.logger.info("************ Starting Add Customer Validation **************")
        
        self.msg = self.driver.find_element_by_xpath("//div[@class='alert alert-success alert-dismissable']").text
        
        if "The new customer has been added successfully" in self.msg:
            self.logger.info("************ Add Customer Test Passed **************")
            assert True
        else:
            self.driver.save_screenshot("../screenshots/"+"test_add_cust"+".png")
            self.logger.info("************ Add Customer Test Failed **************")
            assert False
        
        self.driver.quit()
        self.logger.info("************ Add Customer Test Completed **************")