from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains


class addCustPage:
    
    '''Add cust page objects'''
    email_txtbx_xpath = "//input[@id='Email']"
    pwd_txtbx_xpath = "//input[@id='Password']"
    fname_txtbx_xpath = "//input[@id='FirstName']"
    lname_txtbx_xpath = "//input[@id='LastName']"
    gender_radio_male_id = "Gender_Male"
    gender_radio_female_id = "Gender_Female"
    dob_txtbx_xpath = "//input[@id='DateOfBirth']"
    company_txtbx_xpath = "//input[@id='Company']"
    tax_chkbx_id = "IsTaxExempt"
    news_roles_listbx_xpath = "//div[@class='k-multiselect-wrap k-floatwrap']"
    list_item_newsletter_ysn_xpath = "//li[contains(text(), 'Your store name')]"
    list_item_newsletter_ts2_xpath = "//li[contains(text(), 'Test store 2')]"
    list_item_administrators_xpath = "//li[contains(text(), 'Administrators')]"
    list_item_forum_moderators_xpath = "//li[contains(text(), 'Forum Moderators')]"
    list_item_guests_xpath = "//li[contains(text(), 'Guests')]"
    list_item_regd_xpath = "//li[contains(text(), 'Registered')]"
    list_item_vendors_xpath = "//li[contains(text(), 'Vendors')]"
    mgr_vendor_drpdwn_xpath = "//*[@id='VendorId']"
    active_chkbx_id = "Active"
    admin_cmt_txtbx_xpath = "//textarea[@id='AdminComment']"
    save_btn_xpath = "//button[@name='save']"
    
    '''Create constructor'''
    def __init__(self, driver):
        self.driver = driver
        
    '''Create actions'''
    def enterCustEmail(self, email):
        self.driver.find_element_by_xpath(self.email_txtbx_xpath).clear()
        self.driver.find_element_by_xpath(self.email_txtbx_xpath).send_keys(email)
    
    def enterCustPassword(self, password):
        self.driver.find_element_by_xpath(self.pwd_txtbx_xpath).clear()
        self.driver.find_element_by_xpath(self.pwd_txtbx_xpath).send_keys(password)
        
    def enterFirstName(self, firstName):
        self.driver.find_element_by_xpath(self.fname_txtbx_xpath).clear()
        self.driver.find_element_by_xpath(self.fname_txtbx_xpath).send_keys(firstName)
        
    def enterLastName(self, lastName):
        self.driver.find_element_by_xpath(self.lname_txtbx_xpath).clear()
        self.driver.find_element_by_xpath(self.lname_txtbx_xpath).send_keys(lastName)
        
    def selectGender(self, gender):
        if gender == "Male":
            self.driver.find_element_by_id(self.gender_radio_male_id).click()
        elif gender == "Female":
            self.driver.find_element_by_id(self.gender_radio_female_id).click()
        else:
            self.driver.find_element_by_id(self.gender_radio_male_id).click()

    def enterDOB(self, dob):
        self.driver.find_element_by_xpath(self.dob_txtbx_xpath).clear()
        self.driver.find_element_by_xpath(self.dob_txtbx_xpath).send_keys(dob)
        
    def enterCompany(self, company):
        self.driver.find_element_by_xpath(self.company_txtbx_xpath).clear()
        self.driver.find_element_by_xpath(self.company_txtbx_xpath).send_keys(company)
    
    def checkTaxExempt(self):
        if self.driver.find_element_by_id(self.tax_chkbx_id).is_selected() == False:
            self.driver.find_element_by_id(self.tax_chkbx_id).click()
        
    def selectNewsletter(self, store):
        self.driver.find_elements_by_xpath(self.news_roles_listbx_xpath)[0].click()
        
        if store == "Your store name":
            self.store = self.driver.find_element_by_xpath(self.list_item_newsletter_ysn_xpath)
        elif store == "Test store 2":
            self.store = self.driver.find_element_by_xpath(self.list_item_newsletter_ts2_xpath)
        else:
            self.store = self.driver.find_element_by_xpath(self.list_item_newsletter_ysn_xpath)
        
        act_chains = ActionChains(self.driver)
        act_chains.move_to_element(self.store).perform()
        self.store.click()
    
    def selectCustRoles(self, role):
        self.driver.find_element_by_xpath("//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
        self.driver.find_elements_by_xpath(self.news_roles_listbx_xpath)[1].click()
        
        if role == "Administrators":
            self.role = self.driver.find_element_by_xpath(self.list_item_administrators_xpath)
        elif role == "Forum Moderators":
            self.role = self.driver.find_element_by_xpath(self.list_item_forum_moderators_xpath)
        elif role == "Guests":
            self.role = self.driver.find_element_by_xpath(self.list_item_guests_xpath)
        elif role == "Registered":
            self.role = self.driver.find_element_by_xpath(self.list_item_regd_xpath)
        elif role == "Vendors":
            self.role = self.driver.find_element_by_xpath(self.list_item_vendors_xpath)
        else:
            self.role = self.driver.find_element_by_xpath(self.list_item_guests_xpath)
        
        act_chains = ActionChains(self.driver)
        act_chains.move_to_element(self.role).perform()
        self.role.click()
    
    def selectManagerOfVendors(self, vendor):
        drp = Select(self.driver.find_element_by_xpath(self.mgr_vendor_drpdwn_xpath))
        drp.select_by_visible_text(vendor)
    
    def checkActive(self):
        if self.driver.find_element_by_id(self.active_chkbx_id).is_selected() == False:
            self.driver.find_element_by_id(self.active_chkbx_id).click()

    def enterAdminComment(self, comment):
        self.driver.find_element_by_xpath(self.admin_cmt_txtbx_xpath).clear()
        self.driver.find_element_by_xpath(self.admin_cmt_txtbx_xpath).send_keys(comment)
        
    def clickOnSaveBtn(self):
        self.driver.find_element_by_xpath(self.save_btn_xpath).click()