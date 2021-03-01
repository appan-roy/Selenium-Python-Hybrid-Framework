class custSearchPage:
    
    '''Cust search page objects'''
    add_new_btn_xpath = "//a[@class='btn bg-blue']"
    email_txtbx_id = "SearchEmail"
    firstName_txtbx_id = "SearchFirstName"
    lastName_txtbx_id = "SearchLastName"
    search_btn_id = "search-customers"
    
    table_xpath = "//table[@id='customers-grid']"
    table_rows_xpath = "//table[@id='customers-grid']//tbody/tr"
    table_columns_xpath = "//table[@id='customers-grid']//tbody/tr/td"
    
    '''Create constructor'''
    def __init__(self, driver):
        self.driver = driver
        
    '''Create actions'''       
    def clickOnAddNewBtn(self):
        self.driver.find_element_by_xpath(self.add_new_btn_xpath).click()
    
    def enterEmail(self, email):
        self.driver.find_element_by_id(self.email_txtbx_id).clear()
        self.driver.find_element_by_id(self.email_txtbx_id).send_keys(email)
        
    def enterFirstName(self, fname):
        self.driver.find_element_by_id(self.firstName_txtbx_id).clear()
        self.driver.find_element_by_id(self.firstName_txtbx_id).send_keys(fname)
        
    def enterLastName(self, lname):
        self.driver.find_element_by_id(self.lastName_txtbx_id).clear()
        self.driver.find_element_by_id(self.lastName_txtbx_id).send_keys(lname)
        
    def clickOnSearchBtn(self):
        self.driver.find_element_by_id(self.search_btn_id).click()
        
    def getNoOfRows(self):
        return len(self.driver.find_elements_by_xpath(self.table_rows_xpath))
    
    def getNoOfColumns(self):
        return len(self.driver.find_elements_by_xpath(self.table_columns_xpath))
    
    def searchCustByEmail(self, email):
        flag = False
        for i in range(1, self.getNoOfRows()+1):
            table = self.driver.find_element_by_xpath(self.table_xpath)
            emailId = table.find_element_by_xpath("//table[@id='customers-grid']//tbody/tr["+str(i)+"]/td[2]").text
            if emailId == email:
                flag = True
                break
        return flag
    
    def searchCustByName(self, name):
        flag = False
        for i in range(1, self.getNoOfRows()+1):
            table = self.driver.find_element_by_xpath(self.table_xpath)
            custName = table.find_element_by_xpath("//table[@id='customers-grid']//tbody/tr["+str(i)+"]/td[3]").text
            if custName == name:
                flag = True
                break
        return flag