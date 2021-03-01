class homePage:
    
    '''Home page objects'''
    logout_link_linktext = "Logout"
    cust_main_link_xpath = "//a[@href='#']//span[contains(text(), 'Customers')]"
    cust_sub_link_xpath = "//a[@href='/Admin/Customer/List']//span[contains(text(), 'Customers')]"
    
    '''Create constructor'''
    def __init__(self, driver):
        self.driver = driver
        
    '''Create actions'''
    def clickOnLogoutLink(self):
        self.driver.find_element_by_link_text(self.logout_link_linktext).click()
        
    def clickOnCustMainMenu(self):
        self.driver.find_element_by_xpath(self.cust_main_link_xpath).click()
    
    def clickOnCustSubMenu(self):
        self.driver.find_element_by_xpath(self.cust_sub_link_xpath).click()