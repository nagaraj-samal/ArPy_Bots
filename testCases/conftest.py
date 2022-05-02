import time
import pytest
from selenium import webdriver
from  webdriver_manager.chrome import ChromeDriverManager
#@pytest.fixture(scope="class")
from selenium.webdriver.ie.service import Service

# def pytest_addoption(parser):
#     parser.addoption("--browser",action="store",default="chrome")
#
# @pytest.fixture()
# def getBrowser(request):
#     _browser = request.config.getoption("--browser")
#     return _browser
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(autouse=True)
def setup(request,browser):
    if browser == "chrome":
        _driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        _driver.get("https://easinstance3-ctsoraclecloudaccount.epm.us-phoenix-1.ocs.oraclecloud.com/epmcloud")

    elif browser =="ff":
        print("launch firefox")
        _driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        _driver.get("https://easinstance3-ctsoraclecloudaccount.epm.us-phoenix-1.ocs.oraclecloud.com/epmcloud")
    else:
        print ("provide valid browser")

    #driver.get("https://google.co.in")
    _driver.maximize_window()
    request.cls.driver = _driver
    yield
    request.cls.driver.quit()
    #print("close browser")

#def pytest_adoption(parser):

# def getBrowsername(browsername):
#     _browsername = browsername
#     return _browsername

def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture(scope="class",autouse=True)
def browser(request):
    return request.config.getoption("--browser")
# driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
# driver.get(https://www.)


# def getDriver(request,getBrowsername):
#     _browsername = getBrowsername("Chrome")
#     if _browsername=="Chrome":
#         _driver = webdriver.Chrome(
#                 executable_path="C:\\Users\\613367\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe")
#     _driver.get("https://easinstance3-ctsoraclecloudaccount.epm.us-phoenix-1.ocs.oraclecloud.com/epmcloud")
#     _driver.maximize_window()
#     time.sleep(30)
#
#     request.cls.driver = _driver
#     yield request.cls.driver
#     time.sleep(2)
#     request.cls.driver.quit()






    # _driver = None
    # if getBrowser == "chrome":
    #     _driver = webdriver.Chrome(
    #         executable_path="C:\\Users\\613367\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe")
    #     _driver.get("https://easinstance3-ctsoraclecloudaccount.epm.us-phoenix-1.ocs.oraclecloud.com/epmcloud")
    #     _driver.maximize_window()
    #     time.sleep(30)
    # elif getBrowser == "ie":
    #     _driver = None
    #     s = Service('C:\\Users\\613367\\Downloads\\IEDriverServer_Win32_4.0.0\\IEDriverServer.exe')
    #     _driver = webdriver.Ie(service=s)
    #     _driver.get("https://easinstance3-ctsoraclecloudaccount.epm.us-phoenix-1.ocs.oraclecloud.com/epmcloud")
    #     _driver.maximize_window()
    #     time.sleep(30)









    #getBrowser="chrome"
    #if getBrowser == "chrome":
    # if request.param == "chrome":
    #     _driver = webdriver.Chrome(executable_path="C:\\Users\\613367\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe")
    #elif getBrowser == "firefox":
        #pass
        # _driver.get("https://easinstance3-ctsoraclecloudaccount.epm.us-phoenix-1.ocs.oraclecloud.com/epmcloud")
        # _driver.maximize_window()
        # time.sleep(30)
    # if request.param == "ie":
    #     _driver = None
    #     s = Service('C:\\Users\\613367\\Downloads\\IEDriverServer_Win32_4.0.0\\IEDriverServer.exe')
    #     _driver = webdriver.Ie(service=s)
    #     _driver.get("https://easinstance3-ctsoraclecloudaccount.epm.us-phoenix-1.ocs.oraclecloud.com/epmcloud")
    #     _driver.maximize_window()
    #     time.sleep(30)


