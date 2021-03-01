class loginPage:
    
    '''Login page objects'''
    username_txtbx_id = "Email"
    password_txtbx_id = "Password"
    login_btn_xpath = "//input[@type='submit']"
    
    '''Create constructor'''
    def __init__(self, driver):
        self.driver = driver
        
    '''Create actions'''
    def enterUsername(self, username):
        self.driver.find_element_by_id(self.username_txtbx_id).clear()
        self.driver.find_element_by_id(self.username_txtbx_id).send_keys(username)
        
    def enterPassword(self, password):
        self.driver.find_element_by_id(self.password_txtbx_id).clear()
        self.driver.find_element_by_id(self.password_txtbx_id).send_keys(password)
        
    def clickOnLoginButton(self):
        self.driver.find_element_by_xpath(self.login_btn_xpath).click()