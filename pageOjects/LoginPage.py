import time
from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass

from selenium import webdriver


class Login(BaseClass):

    textbox_username_xpath = "//*[@id='idcs-signin-basic-signin-form-username']"
    textbox_password_xpath = "//oj-input-password[@id='idcs-signin-basic-signin-form-password']"
    #// *[ @ id = 'idcs-signin-basic-signin-form-password']
    button_login_xpath = "//*[@id='idcs-signin-basic-signin-form-submit']"
    user_saDropdown_xpath = "//*[@id='cil12::icon']"
    user_signOut_xpath = "//*[@id='ap1:i15:5:i12:0:cl5']"
    lp_title_xpath = "//span[text()='Account Reconciliation']"
    lp_title = "Account Reconciliation"



    def __init__(self, driver):
        self.z = None
        self.y = None
        self.driver = driver
        # self.driver = webdriver.Chrome(
        #     executable_path="C:\\Users\\613367\\OneDrive - Cognizant\\Documents\\ChromeDriverServer\\chromedriver_win32 (1)\\chromedriver.exe")
        # self.driver.maximize_window()

    def set_username(self, username):
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_username_xpath).send_keys(username)
        #return self.driver

    def set_password(self, password):
        #self.driver.find_element(By.XPATH, self.textbox_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.textbox_password_xpath).send_keys(password)
        #return self.driver

    def click_login(self):
        log=self.getLogger()
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()
        #return self.driver
        time.sleep(30)
        # self.y = Login(self.driver)
        # self.z = self.driver.find_element(By.XPATH,self.lp_title_xpath)
        #
        # if self.z.text == self.y.lp_title :
        #     assert True
        #     log.info("*********** Login Test passed")
        # else:
        #     self.driver.save_screenshot(".\\Screenshots\\"+"test_login_lp_title.png")
        #     assert False
        #     log.error("************** Login Test failed")
        return self.driver

    def click_user_sa(self):
        self.driver.find_element(By.XPATH, self.user_saDropdown_xpath).click()

    def click_logout(self):
        self.driver.find_element(By.XPATH, self.user_signOut_xpath).click()
