import time

from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass


class Period(BaseClass):

    period_spread_operator = "//*[@id='zr2:0:zt0:0:psDash:0:pC:tConsMn:2:cilPerActions::icon']"
    period_menu_import_PreMappedData_xpath = "//td[text()='Import Pre-Mapped Data']"
    period_menu_import_PreMappedBalances_xpath = "//td[text()='Import Pre-Mapped Balances']"
    # period_balance_import_choose_file_btn_xpath = ""

    period_bal_import_choose_file_btn_xpath = "//input[@type='file']"
    period_bal_import_bal_type_icon_xpath = "//a[@id='zr2:0:zt0:0:psDash:0:ImpBal:0:rimport:0:socBalType::drop']"
    # id = "zr2:0:zt0:0:psDash:0:ImpBal:0:rimport:0:socBalType::drop"
    period_bal_import_bal_type_srs_item_xpath = "//li[contains(text(),'Source System')]"
    period_bal_import_bal_type_sbs_item_xpath = "//li[contains(text(),'Subsystem')]"
    period_bal_import_curr_bucket_icon_xpath = "//a[@id='zr2:0:zt0:0:psDash:0:ImpBal:0:rimport:0:socCurrencyBucket::drop']"
    period_bal_import_curr_bucket_item_rpt_xpath = "//li[contains(text(),'Reporting')]"

    period_balance_import_import_btn_xpath = "//button[@id='zr2:0:zt0:0:psDash:0:cmdManagePremappedBalancesOK']"
    period_balance_import_information_close_btn_xpath = "//button[@id='zr2:0:zt0:0:fccErrorPopup:dE::ok']"
    period_balance_import_data_load_results_xpath = "//a[@id='zr2:0:zt0:0:psDash:0:ImpBal:0:cl2']"
    period_balance_import_load_status_xpath = "//td[text()='Completed']"
    period_import_expected_status = "Completed"
    period_pr22_load_result_close_xpath = "//button[@id='zr2:0:zt0:0:psDash:0:cmdManagePremappedBalancesClose']"
    period_home_xpath = "//*[@id='emh1:cil1::icon']"

    def __init__(self, driver):
        self.file_req_sbs = None
        self.file_req_src = None
        self.driver = driver

    def period_src_data_load(self,filename):
        # log = self.getLogger()
        # time.sleep(5)
        self.file_req_src = filename
        self.driver.find_element(By.XPATH, self.period_spread_operator).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.period_menu_import_PreMappedData_xpath ).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.period_menu_import_PreMappedBalances_xpath).click()
        time.sleep(5)
        d = self.driver.find_element(By.XPATH, self.period_bal_import_choose_file_btn_xpath)
        time.sleep(20)
        d.send_keys("C:\\Users\\613367\\OneDrive - Cognizant\\Desktop\\nms1\\" + self.file_req_src)
        time.sleep(10)
        self.driver.find_element(By.XPATH,  self.period_bal_import_bal_type_icon_xpath).click()
        time.sleep(10)
        self.driver.find_element(By.XPATH, self. period_bal_import_bal_type_srs_item_xpath).click()
        time.sleep(10)
        self.driver.find_element(By.XPATH, self.period_bal_import_curr_bucket_icon_xpath).click()
        time.sleep(10)
        self.driver.find_element(By.XPATH, self.period_bal_import_curr_bucket_item_rpt_xpath).click()
        time.sleep(10)
        self.driver.find_element(By.XPATH, self.period_balance_import_import_btn_xpath).click()
        time.sleep(15)
        self.driver.find_element(By.XPATH, self.period_balance_import_information_close_btn_xpath).click()
        time.sleep(10)
        self.driver.find_element(By.XPATH, self.period_balance_import_data_load_results_xpath).click()
        time.sleep(10)
        self.driver.find_element(By.XPATH, self.period_balance_import_load_status_xpath).click()
        time.sleep(10)
        # THIS BELOW code is applicable for  rc autoclose business case
        self.driver.find_element(By.XPATH, self.period_pr22_load_result_close_xpath).click()

        return self.driver

    def period_sbs_data_load(self, filename):
        # log = self.getLogger()
        # time.sleep(5)
        self.file_req_sbs = filename
        self.driver.find_element(By.XPATH, self.period_spread_operator).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.period_menu_import_PreMappedData_xpath).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.period_menu_import_PreMappedBalances_xpath).click()
        time.sleep(5)
        d = self.driver.find_element(By.XPATH, self.period_bal_import_choose_file_btn_xpath)
        time.sleep(20)
        d.send_keys("C:\\Users\\613367\\OneDrive - Cognizant\\Desktop\\nms1\\" + self.file_req_sbs)
        time.sleep(10)
        self.driver.find_element(By.XPATH, self.period_bal_import_bal_type_icon_xpath).click()
        time.sleep(10)
        self.driver.find_element(By.XPATH, self.period_bal_import_bal_type_sbs_item_xpath).click()
        time.sleep(10)
        self.driver.find_element(By.XPATH, self.period_bal_import_curr_bucket_icon_xpath).click()
        time.sleep(10)
        self.driver.find_element(By.XPATH, self.period_bal_import_curr_bucket_item_rpt_xpath).click()
        time.sleep(10)
        self.driver.find_element(By.XPATH, self.period_balance_import_import_btn_xpath).click()
        time.sleep(10)
        self.driver.find_element(By.XPATH, self.period_balance_import_information_close_btn_xpath).click()
        time.sleep(10)
        self.driver.find_element(By.XPATH, self.period_balance_import_data_load_results_xpath).click()
        time.sleep(10)
        self.driver.find_element(By.XPATH, self.period_balance_import_load_status_xpath).click()
        time.sleep(10)
        # THIS BELOW code is applicable for  rc autoclose business case
        self.driver.find_element(By.XPATH, self.period_pr22_load_result_close_xpath).click()

        return self.driver

