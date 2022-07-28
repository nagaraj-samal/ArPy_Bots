import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.BaseClass import BaseClass

from selenium import webdriver
from selenium import webdriver


class Home(BaseClass):

    appCluster_application_xpath = "//*[@id='EPM_CL_2_6']"
    appClusterCard_profile_xpath = "//*[@id='EPM_CA_106_1_1']"
    profile_title_xpath = "//h1[text()='Profiles']"
    actual_profileTitle = "Profiles"

    appClusterCard_period_xpath = "//*[@id='EPM_CA_116_2_2']"
    profile_title_xpath = "//h1[text()='Profiles']"
    actual_profileTitle = "Profiles"




    def __init__(self,driver):
        self.driver = driver


    def profile_launch(self):
        # log = self.getLogger()
        #time.sleep(5)
        self.driver.find_element(By.XPATH,self.appCluster_application_xpath).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.appClusterCard_profile_xpath).click()
        time.sleep(5)
        return self.driver


    def period_launch(self):
        # log = self.getLogger()
        time.sleep(5)
        self.driver.find_element(By.XPATH,self.appCluster_application_xpath).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.appClusterCard_period_xpath).click()
        time.sleep(5)
        return self.driver







