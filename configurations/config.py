'''All the config kept here'''

class Config:
    
    '''Webdriver path'''
    CHROME_DRIVER_PATH = "../drivers/chromedriver.exe"
    FIREFOX_DRIVER_PATH = "../drivers/geckodriver.exe"
    
    '''App info'''
    appUrl = "https://admin-demo.nopcommerce.com/"
    username = "admin@yourstore.com"
    password = "admin"
    
    '''Test data path'''
    dataFile = "../testdata/LoginData.xlsx"
    dataSheet = "Cred"