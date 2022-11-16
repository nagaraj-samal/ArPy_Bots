import time

#import Actions as Actions
from selenium import webdriver
from selenium.webdriver.common.by import By
from utilities.BaseClass import BaseClass
import pandas as pd
from selenium.webdriver.common.keys import Keys


# import Action chains
from selenium.webdriver.common.action_chains import ActionChains




class Profile(BaseClass):
    action_icon_xpath = "//*[@class='xfb']"
    profile_import_xpath = "//*[@id='zr1:0:zt0:0:psDash:0:importRec']"
    profile_choosefiletxt_xpath = "//input[@type='file']"
    profile_importbtn_xpath = "//*[@id='zr1:0:zt0:0:cmdImport']"
    profile_loadstatus_xpath = "//*[@id='zr1:0:zt0:0:rgnImp:0:dcRes:itProgressStatus::content']"
    profile_actual_status = "Completed Successfully."
    profile_uploaded_proof_xpath = "//span[contains(text(),'810001-104-p1')]"
    # need to use list for multiple profile upload validation ,we can currently use items changed after upload
    profile_existing_count = ''
    profile_uploaded_count = ''
    profile_expected_count = profile_existing_count + profile_uploaded_count
    profile_total_count = ''
    profile_existing_items = profile_existing_count + '' + 'Items'

    profile_existing_count_xpath = "//span[contains(text(),'2 Items')]"
    profile_ok_xpath = "//button[@_afrpdoc='ok']"

    profile_existing_count_xpath = "//span[@style='white-space:nowrap']"

    expected_profile_count = '12 Items'

    profile_rc_creation_xpath = "//td[contains(text(),'Create Reconciliations')]"

    profile_rc_period_dropdown_xpath = "//*[@id='zr1:0:zt0:0:psDash:0:actionPanel:0:socCopyToPeriod::glyph']"

    profile_rc_period_item_xpath = "//*[@title='Jan-20']"

    profile_rc22_period_item_xpath = "//*[@title='Mar-22']"

    profile_rc22_selected_profile_xpath = "//*[@id='zr1:0:zt0:0:psDash:0:actionPanel:0:sorPer1:_0']"

    profile_rc22_sel_profile_apply_xpath = "//button[@id='zr1:0:zt0:0:psDash:0:actionPanel:0:cmdPerConfirmationYes']"

    profile_rc22_creation_apply_xpath = "//button[@id='zr1:0:zt0:0:psDash:0:actionPanel:0:cbCopyToPeriod']"

    profile_rc_for_all_apply_xpath = "//button[@id='zr1:0:zt0:0:psDash:0:actionPanel:0:cmdPerConfirmationYes']"

    profile_rc_creation_close_xpath = "//button[@id='cmdCopyProfilesClose']"

    profile_rc_creation_error_status_xpath = "//*[@id='zr1:0:zt0:0:CpRsRg:0:plam5']/td[2]"

    profile_rc_creation_close_xpath = "//button[@id='cmdCopyProfilesClose']"

    profile_rc_period_popup_close_xpath = "//button[@id='actPnlDlgOk']"

    profile_home_xpath = "//*[@id='emh1:cil1::icon']"


    profile_account_id_list = []
    profile_account_id_xpath = ''

    profile_account_name_list = []
    profile_account_name_xpath = ''
    # profile_account_id_xpath = "//span[text()='810001-101-P1']"

    profile_rule_xpath = "//*[@id='zr1:0:zt0:0:psDash:0:RecDfn:0:sdiRule::disAcr']"

    profile_account_name = ''

    profile_account_name_xpath =''

    profile_rule_added_xpath = "//td[text()='Auto Approve Reconciliation']"

    d={}

    profile_rc22_load_result_close_xpath = "//button[@id='zr1:0:zt0:0:psDash:0:cmdManagePremappedBalancesClose']"

    pa2 = '810001-105-p1'


    def __init__(self,driver):
        self.driver = driver

    def set_profilefile(self):
        time.sleep(20)
        self.driver.find_element(By.XPATH,self.action_icon_xpath).click()
        time.sleep(20)
        self.driver.find_element(By.XPATH,self.profile_import_xpath).click()
        time.sleep(20)
        x = self.driver.find_element(By.XPATH,self.profile_choosefiletxt_xpath)
        #s = self.driver.find_element(By.XPATH, "//input[@type='file']")
        x.send_keys("C:\\Users\\613367\\OneDrive - Cognizant\\Desktop\\monthlymetadataload\\ProfilesUpdateed1.csv")
        self.driver.find_element(By.XPATH,self.profile_importbtn_xpath).click()
        time.sleep(30)

        return self.driver


    def get_existing_profile_count(self):
        time.sleep(10)
        log=self.getLogger()
        log.info("call in profile count validation method")

        wspl = self.driver.find_elements(By.XPATH,self.profile_existing_count_xpath)

        print(wspl[4])
        print("hello")
        
        for item in wspl:
            print("hi")
            if item.text == self.expected_profile_count:
                self.profile_existing_count = self.expected_profile_count
                print("Profile total count matches successfully")
                print(self.profile_existing_count)
            # else:
            #     print(self.profile_existing_count)
            #     print("expected and existing profile not matching please look into Profile page")

        return self.driver


    def rc_creation(self):

        time.sleep(5)
        self.driver.find_element(By.XPATH,self.action_icon_xpath).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,self.profile_rc_creation_xpath).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,self.profile_rc_period_dropdown_xpath).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,self.profile_rc_period_item_xpath).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,self.profile_rc_creation_apply_xpath).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,self.profile_rc_for_all_apply_xpath).click()
        time.sleep(5)

        self.driver.find_element(By.XPATH,self.profile_rc_creation_close_xpath).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH,self.profile_rc_period_popup_close_xpath).click()
        time.sleep(5)
        return self.driver


    def profile_Ruleadd(self):

        time.sleep(5)

        df = pd.read_csv("C:\\Users\\613367\OneDrive - Cognizant\Desktop\\profile.csv")


        x = df.Uname

        print(x)
        # print(x[0])


        for f in x:

            i = 0
            global p
            p=[]
            p.append(f)
            print(p[0])

            time.sleep(5)

            self.driver.find_element(By.XPATH,"//span[text()='810001-101-P1']").click()
            time.sleep(5)

            ## below line fix i took 8 hours  struggled like any thing to make below xpath dynamic
            self.driver.find_element(By.XPATH,"//a[@title='{}']".format(str(p[i]))).click()

            print("hello")

            time.sleep(10)

            self.driver.find_element(By.XPATH,"//a[@id='zr1:0:zt0:0:psDash:0:RecDfn:0:sdiRule::disAcr']").click()
            time.sleep(10)

            self.driver.find_element(By.XPATH,"//img[@id='zr1:0:zt0:0:psDash:0:RecDfn:0:dcRule:pcRules:cbRuleAdd::icon']").click()

            time.sleep(10)

            self.driver.find_element(By.XPATH,"//*[@id='zr1:0:zt0:0:psDash:0:RecDfn:0:RuleAR:1:selRule::drop']").click()

            self.driver.find_element(By.XPATH,"//li[text()='Auto Approve Reconciliation']").click()

            self.driver.find_element(By.XPATH,"//*[@for='zr1:0:zt0:0:psDash:0:RecDfn:0:RuleAR:1:smcLevel:_0']").click()

            #self.driver.find_element(By.XPATH,"//span[text()='Filter Criteria']").click()

            self.driver.find_element(By.XPATH,"//*[@id='zr1:0:zt0:0:psDash:0:RecDfn:0:RuleAR:1:rFilter:bAddCnd']").click()

            time.sleep(10)

            self.driver.find_element(By.XPATH,"//*[@id='zr1:0:zt0:0:psDash:0:RecDfn:0:RuleAR:1:rFilter:socSource::drop']").click()

            time.sleep(10)

            self.driver.find_element(By.XPATH,"//li[text()='Balance']").click()

            time.sleep(10)
            self.driver.find_element(By.XPATH,"//a[@id='zr1:0:zt0:0:psDash:0:RecDfn:0:RuleAR:1:rFilter:socAttr::drop']").click()
            time.sleep(10)

            self.driver.find_element(By.XPATH,"//li[text()='Unexplained Difference (Reporting)']").click()
            time.sleep(10)

            self.driver.find_element(By.XPATH,"//*[@id='zr1:0:zt0:0:psDash:0:RecDfn:0:RuleAR:1:rFilter:socOp::drop']").click()
            time.sleep(10)

            self.driver.find_element(By.XPATH,"//*[@id='zr1:0:zt0:0:psDash:0:RecDfn:0:RuleAR:1:rFilter:socOp::pop']/li[4]").click()

            self.driver.find_element(By.XPATH,"//input[@id='zr1:0:zt0:0:psDash:0:RecDfn:0:RuleAR:1:rFilter:itNumber::content']").send_keys("0")

            time.sleep(10)
            self.driver.find_element(By.XPATH,"//span[@id='zr1:0:zt0:0:psDash:0:RecDfn:0:RuleAR:1:rFilter:smcSecValue::cntrl']").click()
            time.sleep(10)
            self.driver.find_element(By.XPATH,"//span[@id='zr1:0:zt0:0:psDash:0:RecDfn:0:RuleAR:1:rFilter:smcSecValue::cntrl']").click()
            time.sleep(10)
            self.driver.find_element(By.XPATH,"//*[@id='zr1:0:zt0:0:psDash:0:RecDfn:0:RuleAR:1:rFilter:smcSecValue::pop']/li[4]/ul/li[3]/label").click()
            time.sleep(5)
            print("hello")

            self.driver.find_element(By.TAG_NAME,'body').send_keys(Keys.CONTROL + Keys.HOME)
            time.sleep(10)
            self.driver.find_element(By.XPATH,"/html/body/div[1]/form/div[2]/div[2]/div[3]/div[1]/table/tbody/tr/td/div/div/table/tbody/tr[1]/td[2]/table/tbody/tr/td[3]/div/div[2]/button[1]").click()
            print("hi")
            time.sleep(10)
            self.driver.find_element(By.XPATH,"//button[@id='cmdReconciliationDefinitionOK']").click()
            time.sleep(10)
            self.driver.find_element(By.XPATH, "//span[text()='810001-101-P1']").click()
            time.sleep(10)
            self.driver.find_element(By.XPATH, "//a[@title='{}']".format(str(p[i]))).click()
            time.sleep(10)

            self.driver.find_element(By.XPATH, "//a[@id='zr1:0:zt0:0:psDash:0:RecDfn:0:sdiRule::disAcr']").click()
            time.sleep(10)

            rule_element=self.driver.find_element(By.XPATH,"//td[text()='Auto Approve Reconciliation']")
            global rulename
            rulename=rule_element.text
            # global d

            self.d[p[i]]= rulename
            self.driver.find_element(By.XPATH,"//button[@id = 'cmdReconciliationDefinitionCancel']").click()
            time.sleep(10)
            i=i+1
            print(self.d)

            print(x)

        return self.driver




    def  rc_creation_selected_profile(self):
        time.sleep(5)
        global pa1
        global pa2
        pa1='810001-104-p1'
        self.pa2='810001-105-p1'

        # self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + Keys.ARROW_DOWN)
        #
        # self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + Keys.ARROW_DOWN)

        time.sleep(15)
        self.driver.find_element(By.XPATH,"//span[text()='810001-105-p1']").click()
        print("clickked with ctrl")
        #time.sleep(10)
        #'810001-105-p1'

        time.sleep(5)
        self.driver.find_element(By.XPATH, self.action_icon_xpath).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.profile_rc_creation_xpath).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.profile_rc_period_dropdown_xpath).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.profile_rc22_period_item_xpath).click()
        time.sleep(5)

        # self.driver.find_element(By.XPATH, self.profile_rc_creation_apply_xpath).click()
        self.driver.find_element(By.XPATH, self.profile_rc22_creation_apply_xpath).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, self. profile_rc22_sel_profile_apply_xpath).click()
        time.sleep(5)

        self.driver.find_element(By.XPATH, self.profile_rc_creation_close_xpath).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.profile_rc_period_popup_close_xpath).click()
        time.sleep(5)

        return self.driver





















            #self.driver.find_element(By.XPATH,"//input[@id='zr1:0:zt0:0:psDash:0:RecDfn:0:RuleAR:1:rFilter:smcSecValue::content']").click()


           #self.driver.find_element(By.XPATH,"//*[@id='zr1:0:zt0:0:psDash:0:RecDfn:0:cmdAddRuleOK']").click()












        #self.driver.find_element(By.XPATH,self.profile_account_id_xpath).click()




        
        







