from pages.LoginPage import loginPage
from pages.HomePage import homePage
from pages.CustSearchPage import custSearchPage
from configurations.config import Config
from utils.customLogger import LogGen
from time import sleep
import pytest


class Test_Search_Customer_By_Name:

    baseUrl = Config.appUrl
    uname = Config.username
    pwd = Config.password
    
    logger = LogGen.logGen()
    
    @pytest.mark.regression
    def test_search_customer_by_name(self, setUp):
        
        self.logger.info("************ Test_Search_Customer_By_Name **************")
        self.driver = setUp
        self.driver.maximize_window()
        self.driver.get(self.baseUrl)
        
        self.lp = loginPage(self.driver)
        self.lp.enterUsername(self.uname)
        self.lp.enterPassword(self.pwd)
        self.lp.clickOnLoginButton()
        
        self.logger.info("************ Starting Search Customer Test **************")
        
        self.hp = homePage(self.driver)
        self.hp.clickOnCustMainMenu()
        self.hp.clickOnCustSubMenu()
        
        self.custsearch = custSearchPage(self.driver)
        self.custsearch.enterFirstName("Arthur")
        self.custsearch.enterLastName("Holmes")
        self.custsearch.clickOnSearchBtn()
        
        self.logger.info("************ Searching Customer **************")
        
        sleep(5)
        search_status = self.custsearch.searchCustByName("Arthur Holmes")
        
        if search_status == True:
            self.logger.info("************ Search Customer Test Passed **************")
            assert True
        else:
            self.driver.save_screenshot("../screenshots/"+"test_search_cust_by_name"+".png")
            self.logger.info("************ Search Customer Test Failed **************")
            assert False
        
        self.driver.quit()
        self.logger.info("************ Search Customer Test Completed **************")