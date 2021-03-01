from configurations.config import Config
from utils.customLogger import LogGen
import pytest


class Test_Login_Page_Title:

    baseUrl = Config.appUrl
    
    logger = LogGen.logGen()
    
    @pytest.mark.smoke
    def test_login_page_title(self, setUp):
        
        self.logger.info("************ Test_Login **************")
        self.logger.info("************ Verifying login page title **************")
        self.driver = setUp
        self.driver.maximize_window()
        self.driver.get(self.baseUrl)
        
        login_title = self.driver.title
        
        if login_title == "Your store. Login":
            self.driver.quit()
            self.logger.info("************ Login page title is verified successfully **************")
            assert True
        else:
            self.driver.save_screenshot("../screenshots/"+"test_loginPageTitle"+".png")
            self.driver.quit()
            self.logger.error("************ Login page title verification failed **************")
            assert False