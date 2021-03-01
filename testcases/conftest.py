from selenium import webdriver
import pytest
from configurations.config import Config


@pytest.fixture()
def setUp(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome(Config.CHROME_DRIVER_PATH)
    elif browser == 'firefox':
        driver = webdriver.Chrome(Config.FIREFOX_DRIVER_PATH)
    else:
        driver = webdriver.Chrome(Config.CHROME_DRIVER_PATH)
    return driver

'''This will get the value from CLI / hooks'''
def pytest_addoption(parser):   
    parser.addoption("--browser")

'''This will return the browser to setup method'''
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

'''This will add env info to HTML report'''
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester Name'] = 'Appan Roy'
    
'''This will delete/modify env info to HTML report'''
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)