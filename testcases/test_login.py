from pages.LoginPage import loginPage
from configurations.config import Config
from utils.customLogger import LogGen
import pytest


class Test_Login:

    baseUrl = Config.appUrl
    uname = Config.username
    pwd = Config.password
    
    logger = LogGen.logGen()
    
    @pytest.mark.smoke
    @pytest.mark.sanity
    def test_login(self, setUp):
        
        self.logger.info("************ Test_Login **************")
        self.logger.info("************ Verifying login to the application **************")
        self.driver = setUp
        self.driver.maximize_window()
        self.driver.get(self.baseUrl)
        
        self.lp = loginPage(self.driver)
        self.lp.enterUsername(self.uname)
        self.lp.enterPassword(self.pwd)
        self.lp.clickOnLoginButton()
        
        home_title = self.driver.title
        
        if home_title == "Dashboard / nopCommerce administration":
            self.driver.quit()
            self.logger.info("************ Login test passed **************")
            assert True
        else:
            self.driver.save_screenshot("../screenshots/"+"test_login"+".png")
            self.driver.quit()
            self.logger.error("************ Login test failed **************")
            assert False