import time
import traceback
import self as self
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from pageOjects.LoginPage import Login
import pytest
from utilities.readProperties import ReadConfig
from utilities.BaseClass import BaseClass

@pytest.mark.usefixtures("setup")
class Test_001_Login(BaseClass):

    baseURL = "https://easinstance3-ctsoraclecloudaccount.epm.us-phoenix-1.ocs.oraclecloud.com/epmcloud"
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    exp_title_lp = "Account Reconciliation"
    exp_title_hp = "Identity Cloud Service"
    #driver = getDriver(request,chrome)
    act_title = ''
    o1 = ''
    log = ''


    #log = self.getLogger()
    def test_homepage_title(self):
        self.log = self.getLogger()
        self.log.info("************* homepage_title test started**************")
        driver = self.driver
        #self.driver.get(self.baseURL)
        #act_title = self.driver.title
        self.act_title = self.driver.title

        #self.driver.close()
        driver.close()
        self.o1 = Test_001_Login()

        if self.act_title == self.o1.exp_title_hp:
            assert True
            self.log.info("**************homepage_title test passed**********")

        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homepage_title.png")
            assert False
            self.log.info("***************homepage_title test failed*****************")



    def test_login(self):
        log = self.getLogger()
        log.info("***********Verifying Login test***********")
        driver = self.driver
        #self.driver.get(self.baseURL)
        self.o2 = Test_001_Login()
        time.sleep(20)
        self.lp = Login(self.driver)
        time.sleep(30)
        self.lp.set_username(self.o2.username)
        time.sleep(15)

        self.driver = self.lp.set_password(self.o2.password)
        time.sleep(15)

        self.driver = self.lp.click_login()
        self.xp1 = Login(self.driver)

        self.z = self.driver.find_element(By.XPATH,self.xp1.lp_title_xpath)

        if self.z.text == self.xp1.lp_title:
            assert True
            log.info("*********** Login Test passed")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login_lp_title.png")
            assert False
            log.error("************** Login Test failed***************")



        time.sleep(20)
        self.driver.close()
        #self.logger("*******Login test Passed********")

        # if act_title == self.o2.exp_title_lp:
        #     assert True
        # else:
        #     assert False



