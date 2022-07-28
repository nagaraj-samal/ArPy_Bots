import time
from utilities.BaseClass import BaseClass
from selenium import webdriver
from selenium.webdriver.common.by import By


class Reconciliation(BaseClass):

    rc_period_dropdown_xpath = "//*[@id='zr1:0:zt0:0:psDash:0:fb:tl1A']"
    rc_period_dropdown_item_xpath = "//div[@id='zr1:0:zt0:0:psDash:0:fb:tl1::ModEntDr']"
    rc_period_select_xpath = "//li[text()='Jan-20']"
    rc_period_rc_created_count_xpath = "//span[@style='white-space:nowrap']"
    rc_period_rc_created_expected_count = '12 Items'
    rc_header_xpath = "// h1[contains(text(), 'Reconciliations')]"
    rc_reconciliation_icon_xpath = "//div[@id='sdizr1::disAcr']"
    rc_created_count_xpath = "//*[@id='zr1:0:zt0:0:psDash:0:tCt::db']/table/tbody/tr/td/span/span"
    rc_created_existing_count = ''
    reconciliation_cluster_xpath ="//*[@id='EPM_CA_2_1']"

    reconciliation_action_icon_xpath = "//img[@src='/arm/oracle/apps/epm/fcm/common/ui/images/icons/fuse/fuse-icon-dropdown-lov-ena.png']"
    reconciliation_balance_import_xpath = "//tr[@id='zr1:0:zt0:0:psDash:0:mPreMappedDataload']"
    reconciliation_balance_import_preformload_xpath = "//tr[@id='zr1:0:zt0:0:psDash:0:cmiImportPreMappedBalances']"
    reconciliation_balance_import_file_text_xpath = "//input[@name='zr1:0:zt0:0:psDash:0:ImpBal:0:rimport:0:if1']"
    reconciliation_balance_import_choose_file_btn_xpath = "//input[@type='file']"
    reconciliation_balance_import_balancetype_icon_xpath = "//a[@id='zr1:0:zt0:0:psDash:0:ImpBal:0:rimport:0:socBalType::drop']"
    reconciliation_balance_import_balancetype_srs_item_xpath = "//li[contains(text(),'Source System')]"
    reconciliation_balance_import_balancetype_sbs_item_xpath = "//li[contains(text(),'Subsystem')]"
    reconciliation_balance_import_currency_bucket_icon_xpath = "//a[@id='zr1:0:zt0:0:psDash:0:ImpBal:0:rimport:0:socCurrencyBucket::drop']"
    reconciliation_balance_import_currency_bucket_item_rpt_xpath = "//li[contains(text(),'Reporting')]"
    reconciliation_balance_import_currency_bucket_item_ent_xpath_xpath = "//li[contains(text(),'Entered')]"
    reconciliation_balance_import_currency_bucket_item_fn_xpath = "//li[contains(text(),'Functional')]"
    reconciliation_balance_import_import_btn_xpath = "//button[@id='zr1:0:zt0:0:psDash:0:cmdManagePremappedBalancesOK']"
    reconciliation_balance_import_information_close_btn_xpath = "//button[@id='zr1:0:zt0:0:fccErrorPopup:dE::ok']"
    reconciliation_balance_import_data_load_results_xpath = "//a[@id='zr1:0:zt0:0:psDash:0:ImpBal:0:cl2']"
    reconciliation_balance_import_load_status_xpath = "//*[@id='zr1:0:zt0:0:psDash:0:ImpBal:0:rresult:1:plmStatus']"

    reconciliation_import_expected_status = "Status Completed"

    reconciliation_rc22_load_result_close_xpath = "//button[@id='zr1:0:zt0:0:psDash:0:cmdManagePremappedBalancesClose']"


    rc_created_status_xpath = "//*[@id='zr1:0:zt0:0:psDash:0:tblList::db']/table/tbody/tr[1]/td[1]/div/table/tbody/tr/td[3]/span/span"

    rc_created_src_data_load_filepath_mar22 ="C:\\Users\\613367\\OneDrive - Cognizant\\Desktop\\nms1\\b1_src.csv"

    rc_created_ac_status_xpath = "//span[@title='Closed']"

    rc_search_box_xpath = "// input[ @ id = 'zr1:0:zt0:0:psDash:0:search::content']"
    rc_created_ac_expected_status = "Closed"







    def __init__(self,driver):
        self.file_req_src = None
        self.file_req_sbs = None
        # self.filereqsrc = None
        self.driver = driver


    def rc_created_count_check(self):

        # self.driver.find_element(By.XPATH,self.rc_period_dropdown_item_xpath).click()
        # time.sleep(20)
        # self.driver.find_element(By.XPATH,self.rc_period_select_xpath).click()
        # time.sleep(30)
        # self.driver.find_element(By.XPATH,self.rc_reconciliation_icon_xpath).click()
        time.sleep(20)
        rc=self.driver.find_element(By.XPATH,self.rc_created_count_xpath)
        #print(rc_count_list)
        #for item1 in rc_count_list:
            #print(item1.text)
        if rc.text == self.rc_period_rc_created_expected_count:
            assert True
            print("RC created total count matched successfully")
            print(rc.text)
        else:
            print("RC created count not matching")


            return  self.driver



    def rc_balance_import(self,filename):
        self.file_req_src = filename
        print("hi")
        time.sleep(20)
        self.driver.find_element(By.XPATH,self.reconciliation_action_icon_xpath).click()
        time.sleep(20)
        self.driver.find_element(By.XPATH,self.reconciliation_balance_import_xpath).click()
        time.sleep(20)
        self.driver.find_element(By.XPATH,self.reconciliation_balance_import_preformload_xpath).click()
        time.sleep(20)
        d = self.driver.find_element(By.XPATH,self.reconciliation_balance_import_choose_file_btn_xpath)
        time.sleep(20)
        d.send_keys("C:\\Users\\613367\\OneDrive - Cognizant\\Desktop\\nms1\\"+self.file_req_src)
        # // a[ @ title = '{}']".format(str(p[i]))).click()

        #d.send_keys("C:\\Users\\613367\\OneDrive - Cognizant\\Desktop\\nms1\\b1.csv")
        # d = self.driver.find_element(By.XPATH, self.reconciliation_balance_import_choose_file_btn_xpath)
        # d.send_keys("C:\\Users\\613367\\OneDrive - Cognizant\\Desktop\\nms1\\b1.csv")
        time.sleep(20)
        self.driver.find_element(By.XPATH,self.reconciliation_balance_import_balancetype_icon_xpath).click()
        time.sleep(20)
        self.driver.find_element(By.XPATH,self.reconciliation_balance_import_balancetype_srs_item_xpath).click()
        time.sleep(20)
        self.driver.find_element(By.XPATH,self.reconciliation_balance_import_currency_bucket_icon_xpath).click()
        time.sleep(20)
        self.driver.find_element(By.XPATH,self.reconciliation_balance_import_currency_bucket_item_rpt_xpath).click()
        time.sleep(30)
        self.driver.find_element(By.XPATH,self.reconciliation_balance_import_import_btn_xpath).click()
        time.sleep(30)
        self.driver.find_element(By.XPATH,self.reconciliation_balance_import_information_close_btn_xpath).click()
        time.sleep(20)
        self.driver.find_element(By.XPATH,self.reconciliation_balance_import_data_load_results_xpath).click()
        time.sleep(20)
        # THIS BELOW code is applicable for  rc autoclose business case
        self.driver.find_element(By.XPATH, self.reconciliation_rc22_load_result_close_xpath).click()




        return self.driver



    def rc_bulk_balance_import(self):

        print("hi")
        time.sleep(20)
        self.driver.find_element(By.XPATH,self.reconciliation_action_icon_xpath).click()
        time.sleep(20)
        self.driver.find_element(By.XPATH,self.reconciliation_balance_import_xpath).click()
        time.sleep(20)
        self.driver.find_element(By.XPATH,self.reconciliation_balance_import_preformload_xpath).click()
        time.sleep(20)
        d = self.driver.find_element(By.XPATH,self.reconciliation_balance_import_choose_file_btn_xpath)
        time.sleep(20)
        d.send_keys("C:\\Users\\613367\\OneDrive - Cognizant\\Desktop\\nms1\\b2.csv")
        # d = self.driver.find_element(By.XPATH, self.reconciliation_balance_import_choose_file_btn_xpath)
        # d.send_keys("C:\\Users\\613367\\OneDrive - Cognizant\\Desktop\\nms1\\b1.csv")
        time.sleep(20)
        self.driver.find_element(By.XPATH,self.reconciliation_balance_import_balancetype_icon_xpath).click()
        time.sleep(20)
        self.driver.find_element(By.XPATH,self.reconciliation_balance_import_balancetype_srs_item_xpath).click()
        time.sleep(20)
        self.driver.find_element(By.XPATH,self.reconciliation_balance_import_currency_bucket_icon_xpath).click()
        time.sleep(20)
        self.driver.find_element(By.XPATH,self.reconciliation_balance_import_currency_bucket_item_rpt_xpath).click()
        time.sleep(30)
        self.driver.find_element(By.XPATH,self.reconciliation_balance_import_import_btn_xpath).click()
        time.sleep(30)
        self.driver.find_element(By.XPATH,self.reconciliation_balance_import_information_close_btn_xpath).click()
        time.sleep(20)
        self.driver.find_element(By.XPATH,self.reconciliation_balance_import_data_load_results_xpath).click()
        time.sleep(20)

        return self.driver


    def rc_sbs_balance_import(self,filename):
        self.file_req_sbs = filename
        print("hi")
        time.sleep(20)
        self.driver.find_element(By.XPATH,self.reconciliation_action_icon_xpath).click()
        time.sleep(20)
        self.driver.find_element(By.XPATH,self.reconciliation_balance_import_xpath).click()
        time.sleep(20)
        self.driver.find_element(By.XPATH,self.reconciliation_balance_import_preformload_xpath).click()
        time.sleep(20)
        d = self.driver.find_element(By.XPATH,self.reconciliation_balance_import_choose_file_btn_xpath)
        time.sleep(20)
        d.send_keys("C:\\Users\\613367\\OneDrive - Cognizant\\Desktop\\nms1\\"+self.file_req_sbs)
        # d.send_keys("C:\\Users\\613367\\OneDrive - Cognizant\\Desktop\\nms1\\b4.csv")
        # d = self.driver.find_element(By.XPATH, self.reconciliation_balance_import_choose_file_btn_xpath)
        # d.send_keys("C:\\Users\\613367\\OneDrive - Cognizant\\Desktop\\nms1\\b1.csv")
        time.sleep(20)
        self.driver.find_element(By.XPATH,self.reconciliation_balance_import_balancetype_icon_xpath).click()
        time.sleep(20)
        self.driver.find_element(By.XPATH,self.reconciliation_balance_import_balancetype_sbs_item_xpath).click()
        time.sleep(20)
        self.driver.find_element(By.XPATH,self.reconciliation_balance_import_currency_bucket_icon_xpath).click()
        time.sleep(20)
        self.driver.find_element(By.XPATH,self.reconciliation_balance_import_currency_bucket_item_rpt_xpath).click()
        time.sleep(30)
        self.driver.find_element(By.XPATH,self.reconciliation_balance_import_import_btn_xpath).click()
        time.sleep(30)
        self.driver.find_element(By.XPATH,self.reconciliation_balance_import_information_close_btn_xpath).click()
        time.sleep(20)
        self.driver.find_element(By.XPATH,self.reconciliation_balance_import_data_load_results_xpath).click()
        time.sleep(20)

        #THIS BELOW code is applicable for  rc autoclose business case
        self.driver.find_element(By.XPATH,self.reconciliation_rc22_load_result_close_xpath).click()




        return self.driver



    def rc_sbs_bulk_balance_import(self):

        print("hi")
        time.sleep(20)
        self.driver.find_element(By.XPATH,self.reconciliation_action_icon_xpath).click()
        time.sleep(20)
        self.driver.find_element(By.XPATH,self.reconciliation_balance_import_xpath).click()
        time.sleep(20)
        self.driver.find_element(By.XPATH,self.reconciliation_balance_import_preformload_xpath).click()
        time.sleep(20)
        d = self.driver.find_element(By.XPATH,self.reconciliation_balance_import_choose_file_btn_xpath)
        time.sleep(20)
        d.send_keys("C:\\Users\\613367\\OneDrive - Cognizant\\Desktop\\nms1\\b3.csv")
        # d = self.driver.find_element(By.XPATH, self.reconciliation_balance_import_choose_file_btn_xpath)
        # d.send_keys("C:\\Users\\613367\\OneDrive - Cognizant\\Desktop\\nms1\\b1.csv")
        time.sleep(20)
        self.driver.find_element(By.XPATH,self.reconciliation_balance_import_balancetype_icon_xpath).click()
        time.sleep(20)
        self.driver.find_element(By.XPATH,self.reconciliation_balance_import_balancetype_sbs_item_xpath).click()
        time.sleep(20)
        self.driver.find_element(By.XPATH,self.reconciliation_balance_import_currency_bucket_icon_xpath).click()
        time.sleep(20)
        self.driver.find_element(By.XPATH,self.reconciliation_balance_import_currency_bucket_item_rpt_xpath).click()
        time.sleep(30)
        self.driver.find_element(By.XPATH,self.reconciliation_balance_import_import_btn_xpath).click()
        time.sleep(30)
        self.driver.find_element(By.XPATH,self.reconciliation_balance_import_information_close_btn_xpath).click()
        time.sleep(20)
        self.driver.find_element(By.XPATH,self.reconciliation_balance_import_data_load_results_xpath).click()
        time.sleep(20)

        return self.driver



    def rc_created_status(self):

        time.sleep(20)

        self.actual_rc_status_ele = self.driver.find_element(By.XPATH,self.rc_created_status_xpath)

        self.actual_rc_created_status = self.actual_rc_status_ele.text


        return self.driver








