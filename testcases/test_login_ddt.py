from pages.LoginPage import loginPage
from pages.HomePage import homePage
from configurations.config import Config
from utils.customLogger import LogGen
from utils import excelUtils as xl
from time import sleep
import pytest


class Test_Login_DDT:

    baseUrl = Config.appUrl
    
    logger = LogGen.logGen()
    
    @pytest.mark.regression
    @pytest.mark.endtoend
    def test_login_ddt(self, setUp):
        
        self.logger.info("************ Test_Login_DDT Started**************")
        self.logger.info("************ Verifying login to the application using DDT **************")
        self.driver = setUp
        self.driver.maximize_window()
        self.driver.get(self.baseUrl)
        
        self.lp = loginPage(self.driver)
        self.hp = homePage(self.driver)
        
        test_status = []
        
        self.rows = xl.getRowCount(Config.dataFile, Config.dataSheet)
        print("No. of rows : " + str(int(self.rows)-1))
        
        for row in range(2, self.rows+1):
            
            self.uname = xl.readData(Config.dataFile, Config.dataSheet, row, 1)
            self.pwd = xl.readData(Config.dataFile, Config.dataSheet, row, 2)
            self.exp = xl.readData(Config.dataFile, Config.dataSheet, row, 3)
            
            self.lp.enterUsername(self.uname)
            self.lp.enterPassword(self.pwd)
            self.lp.clickOnLoginButton()
            
            sleep(5)
            
            exp_title = "Dashboard / nopCommerce administration"
            act_title = self.driver.title
        
            if act_title == exp_title:
                
                if self.exp == "Pass":
                    self.logger.info("*** Passed ***")
                    self.hp.clickOnLogoutLink()
                    test_status.append("Pass")
                elif self.exp == "Fail":
                    self.driver.save_screenshot("../screenshots/"+"test_login_ddt"+self.uname+"_"+self.pwd+".png")
                    self.logger.info("*** Failed ***")
                    self.hp.clickOnLogoutLink()
                    test_status.append("Fail")
                    
            elif act_title != exp_title:
                
                if self.exp == "Pass":
                    self.driver.save_screenshot("../screenshots/"+"test_login_ddt"+self.uname+"_"+self.pwd+".png")
                    self.logger.info("*** Failed ***")
                    test_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("*** Passed ***")
                    test_status.append("Pass")
            
        if "Fail" not in test_status:
            self.logger.info("************ Login Test DDT Passed **************")
            self.driver.quit()
            assert True
        else:
            self.driver.quit()
            self.logger.error("************ Login Test DDT Failed **************")
            assert False
        
        self.logger.info("************ Test_Login_DDT Completed **************")
        