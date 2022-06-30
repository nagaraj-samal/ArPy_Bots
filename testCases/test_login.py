import time
import traceback
import self as self
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from pageOjects.HomePage import Home
from pageOjects.LoginPage import Login
import pytest

from pageOjects.ProfilePage import Profile
from pageOjects.ReconciliationPage import Reconciliation
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
    rule_name = 'Auto Approve Reconciliation'




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
            self.log.info("***************homepage_title test failed*****************")
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homepage_title.png")
            assert False
            #self.log.info("***************homepage_title test failed*****************")



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

    def test_profilelaunch(self):
        log = self.getLogger()
        log.info("***********Verifying Profile Launch test***********")

        driver = self.driver

        # self.driver.get(self.baseURL)
        self.o2 = Test_001_Login()
        time.sleep(20)
        self.lp = Login(self.driver)
        time.sleep(30)
        self.lp.set_username(self.o2.username)
        time.sleep(15)

        self.driver = self.lp.set_password(self.o2.password)
        time.sleep(15)

        self.driver = self.lp.click_login()
        time.sleep(20)
        self.homePageObject = Home(self.driver)
        self.driver = self.homePageObject.profile_launch()
        self.profileTitle = Home(self.driver)

        self.prT = self.driver.find_element(By.XPATH,self.profileTitle.profile_title_xpath)

        if self.prT.text == self.profileTitle.actual_profileTitle:
            assert True
            log.info("*********** Login Test passed")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login_lp_title.png")
            assert False
            log.error("************** Login Test failed***************")



    def test_profileupload(self):

        log = self.getLogger()
        log.info("***********Verifying Profile upload test***********")

        driver = self.driver

        # self.driver.get(self.baseURL)
        self.o2 = Test_001_Login()
        time.sleep(20)
        self.lp = Login(self.driver)
        time.sleep(30)
        self.lp.set_username(self.o2.username)
        time.sleep(15)

        self.driver = self.lp.set_password(self.o2.password)
        time.sleep(15)

        self.driver = self.lp.click_login()
        time.sleep(20)
        self.homePageObject = Home(self.driver)
        self.driver = self.homePageObject.profile_launch()
        self.profileImport = Profile(self.driver)
        self.driver = self.profileImport.set_profilefile()

        self.prloadstatus = self.driver.find_element(By.XPATH,self.profileImport.profile_loadstatus_xpath)


        self.profileImport1 = Profile(self.driver)
        self.driver = self.driver.find_element(By.XPATH, self.profileImport1.profile_ok_xpath).click()
        time.sleep(20)
        driver.refresh()
        time.sleep(20)
        self.driver = self.profileImport1.get_existing_profile_count()

        if self.profileImport1.expected_profile_count == self.profileImport1.profile_existing_count:
            #self.prloadstatus.text == self.profileImport.profile_actual_status #and \

            assert True
            log.info("***********ProfileUpload Test validation passed")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login_lp_title.png")
            assert False
            log.error("************** Login Test failed***************")


    def test_rc_creation(self):

        log = self.getLogger()
        log.info("***********Verifying Profile Launch test***********")

        driver = self.driver

        # self.driver.get(self.baseURL)
        self.o2 = Test_001_Login()
        time.sleep(20)
        self.lp = Login(self.driver)
        time.sleep(30)
        self.lp.set_username(self.o2.username)
        time.sleep(15)

        self.driver = self.lp.set_password(self.o2.password)
        time.sleep(15)

        self.driver = self.lp.click_login()
        time.sleep(20)
        self.homePageObject = Home(self.driver)
        self.driver = self.homePageObject.profile_launch()
        self.profile_page1 = Profile(self.driver)
        self.driver = self.profile_page1.rc_creation()
        time.sleep(30)

        self.driver.find_element(By.XPATH,self.profile_page1.profile_home_xpath).click()

        time.sleep(20)

        self.rc_pageobj1 = Reconciliation(self.driver)
        self.driver.find_element(By.XPATH,self.rc_pageobj1.reconciliation_cluster_xpath).click()
        time.sleep(20)
        self.driver = self.rc_pageobj1.rc_created_count_check()
        if self.rc_pageobj1.rc_period_rc_created_expected_count == self.rc_pageobj1.rc_created_existing_count:
            #log.info("rc_created count matched successfully")
            assert True
            log.info("rc_created count matched successfully")
        else:
            log.info("rc created count not matched  successfully")


    def test_rc_srs_balance_data_load(self):

        log = self.getLogger()
        log.info("***********Verifying balance load  test***********")

        driver = self.driver

        # self.driver.get(self.baseURL)
        self.o2 = Test_001_Login()
        time.sleep(20)
        self.lp = Login(self.driver)
        time.sleep(30)
        self.lp.set_username(self.o2.username)
        time.sleep(15)

        self.driver = self.lp.set_password(self.o2.password)
        time.sleep(15)

        self.driver = self.lp.click_login()
        time.sleep(20)

        self.rc_pageobj1 = Reconciliation(self.driver)
        self.driver.find_element(By.XPATH, self.rc_pageobj1.reconciliation_cluster_xpath).click()
        time.sleep(20)
        self.driver = self.rc_pageobj1.rc_bulk_balance_import()
        print("hi")
        time.sleep(20)
        y = self.driver.find_element(By.XPATH, self.rc_pageobj1.reconciliation_balance_import_load_status_xpath)
        print(self.rc_pageobj1.reconciliation_import_expected_status)
        print(y.text)

        if y.text == self.rc_pageobj1.reconciliation_import_expected_status:
            assert True
            log.info("rc balance imported successfully  ")
        else:
            log.info("rc balance not imported successfully")

    def test_rc_srs_bulk_balance_data_load(self):

        log = self.getLogger()
        log.info("***********Verifying balance load  test***********")

        driver = self.driver

        # self.driver.get(self.baseURL)
        self.o2 = Test_001_Login()
        time.sleep(20)
        self.lp = Login(self.driver)
        time.sleep(30)
        self.lp.set_username(self.o2.username)
        time.sleep(15)

        self.driver = self.lp.set_password(self.o2.password)
        time.sleep(15)

        self.driver = self.lp.click_login()
        time.sleep(20)

        self.rc_pageobj1 = Reconciliation(self.driver)
        self.driver.find_element(By.XPATH, self.rc_pageobj1.reconciliation_cluster_xpath).click()
        time.sleep(20)
        self.driver = self.rc_pageobj1.rc_bulk_balance_import()
        print("hi")
        time.sleep(20)
        y = self.driver.find_element(By.XPATH, self.rc_pageobj1.reconciliation_balance_import_load_status_xpath)
        print(self.rc_pageobj1.reconciliation_import_expected_status)
        print(y.text)

        if y.text == self.rc_pageobj1.reconciliation_import_expected_status:
            assert True
            log.info("rc balance imported successfully  ")
        else:
            log.info("rc balance not imported successfully")


    def test_rc_sbs_balance_data_load(self):

        log = self.getLogger()
        log.info("***********Verifying balance load  test***********")

        driver = self.driver

        # self.driver.get(self.baseURL)
        self.o2 = Test_001_Login()
        time.sleep(20)
        self.lp = Login(self.driver)
        time.sleep(30)
        self.lp.set_username(self.o2.username)
        time.sleep(15)

        self.driver = self.lp.set_password(self.o2.password)
        time.sleep(15)

        self.driver = self.lp.click_login()
        time.sleep(20)

        self.rc_pageobj1 = Reconciliation(self.driver)
        self.driver.find_element(By.XPATH, self.rc_pageobj1.reconciliation_cluster_xpath).click()
        time.sleep(20)
        self.driver = self.rc_pageobj1.rc_sbs_balance_import()
        print("hi")
        time.sleep(20)
        y = self.driver.find_element(By.XPATH, self.rc_pageobj1.reconciliation_balance_import_load_status_xpath)
        print(self.rc_pageobj1.reconciliation_import_expected_status)
        print(y.text)

        if y.text == self.rc_pageobj1.reconciliation_import_expected_status:
            assert True
            log.info("rc balance imported successfully  ")
        else:
            log.info("rc balance not imported successfully")



    def test_rc_sbs_bulk_balance_data_load(self):

        log = self.getLogger()
        log.info("***********Verifying balance load  test***********")

        driver = self.driver

        # self.driver.get(self.baseURL)
        self.o2 = Test_001_Login()
        time.sleep(20)
        self.lp = Login(self.driver)
        time.sleep(30)

        self.lp.set_username(self.o2.username)
        time.sleep(15)

        self.driver = self.lp.set_password(self.o2.password)
        time.sleep(15)

        self.driver = self.lp.click_login()
        time.sleep(20)

        self.rc_pageobj1 = Reconciliation(self.driver)
        self.driver.find_element(By.XPATH, self.rc_pageobj1.reconciliation_cluster_xpath).click()
        time.sleep(20)
        self.driver = self.rc_pageobj1.rc_sbs_bulk_balance_import()
        print("hi")
        time.sleep(20)
        y = self.driver.find_element(By.XPATH, self.rc_pageobj1.reconciliation_balance_import_load_status_xpath)
        print(self.rc_pageobj1.reconciliation_import_expected_status)
        print(y.text)

        if y.text == self.rc_pageobj1.reconciliation_import_expected_status:
            assert True
            log.info("rc sbs bulk balance imported successfully  ")
        else:
            log.info("rc balance not imported successfully")








    def test_profile_rule_update(self):

        log = self.getLogger()
        log.info("***********Verifying rule updation for multiple profiles***********")

        driver = self.driver

        # self.driver.get(self.baseURL)
        self.o2 = Test_001_Login()
        time.sleep(5)
        self.lp = Login(self.driver)
        time.sleep(5)
        self.lp.set_username(self.o2.username)
        time.sleep(5)
        self.driver = self.lp.set_password(self.o2.password)
        time.sleep(5)
        self.driver = self.lp.click_login()
        time.sleep(5)
        self.hapr= Home(self.driver)
        self.driver = self.hapr.profile_launch()
        self.pro1 = Profile(self.driver)
        self.driver = self.pro1.profile_Ruleadd()
        self.pro2 = Profile(self.driver)
        # print(self.pro1.profile_rule_added_xpath)
        # self.pro1 = Profile(self.driver)
        print(self.pro2.d)

        print("dict global accessed")

        if (self.pro2.d['GL to Bank Profile']==self.rule_name) and (self.pro2.d['GL to Bank1 Profile']==self.rule_name):
            assert True
            print("condition passed")
            log.info("rule added successfully for two profiles")
        else:
            log.info("rule is not added successfully")
        print("after if")

        # print(y.text)
        # if y.text == self.rc_pageobj1.reconciliation_import_expected_status:
        #     assert True
        #     log.info("rc sbs bulk balance imported successfully  ")
        # else:
        #     log.info("rc balance not imported successfully")





    def test_Rc_status_autoclose(self):

        log = self.getLogger()
        log.info("***********Verifying rc status autoClose***********")

        driver = self.driver

        # self.driver.get(self.baseURL)
        self.o2 = Test_001_Login()
        time.sleep(10)
        self.lp = Login(self.driver)
        time.sleep(10)
        self.lp.set_username(self.o2.username)
        time.sleep(10)
        self.driver = self.lp.set_password(self.o2.password)
        time.sleep(10)
        self.driver = self.lp.click_login()
        time.sleep(10)
        self.hapr= Home(self.driver)
        self.driver = self.hapr.profile_launch()
        self.pro1 = Profile(self.driver)
        self.driver = self.pro1.rc_creation_selected_profile()
        self.driver.find_element(By.XPATH, self.profile_page1.profile_home_xpath).click()

        time.sleep(20)

        self.rc_pageobj1 = Reconciliation(self.driver)
        self.driver.find_element(By.XPATH, self.rc_pageobj1.reconciliation_cluster_xpath).click()
        time.sleep(20)

        self.driver.find_element(By.XPATH,  self.rc_pageobj1.rc  )


































