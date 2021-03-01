
rem taskkill /im chromedriver.exe /f
rem taskkill /im chrome.exe /f

cd /d E:\Softwares\My PC Apps\Selenium Python\Workspace\SeleniumHybridFramework\testcases

rem pytest -v -s --html=reports\report.html test_login_page_title.py --browser chrome
rem pytest -v -s --html=reports\report.html test_login.py --browser chrome
rem pytest -v -s --html=reports\report.html test_login_ddt.py --browser chrome
rem pytest -v -s --html=reports\report.html test_add_customer.py --browser chrome
rem pytest -v -s --html=reports\report.html test_search_customer_by_email.py --browser chrome
rem pytest -v -s --html=reports\report.html test_search_customer_by_name.py --browser chrome
pytest -v -s --html=reports\report.html -m "smoke" --browser chrome
