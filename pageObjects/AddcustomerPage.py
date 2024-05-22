import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select

class Addcustomer:
    link_customer_xpath="//i[@class='nav-icon far fa-user']"
    link_subcustomer_xpath="//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btn_addnew_xpath="//a[normalize-space()='Add new']"
    txt_email_id = "Email"
    txt_password_id = "Password"
    txt_firstname_id = "FirstName"
    txt_lastname_id = "LastName"
    rd_male_id="Gender_Male"
    rd_female_id="Gender_Female"
    txt_dob_id="DateOfBirth"
    txt_company_id="Company"
    chkbox_tax_id="IsTaxExempt"
    list_newsltr_xpath="//*[@id='customer-info']/div[2]/div[9]/div[2]/div/div[1]/div/div"
    list_storename_xpath="//*[@id='SelectedNewsletterSubscriptionStoreIds_listbox']/li[1]"
    list_teststore_xpath="//*[@id='SelectedNewsletterSubscriptionStoreIds_listbox']/li[2]"
    list_custrole_xpath="//*[@id='customer-info']/div[2]/div[10]/div[2]/div/div[1]/div/div"
    list_admin_xpath="//li[contains(text(),'Administrators')]"
    list_forum_xapth="//li[contains(text(),'Forum Moderators')]"
    list_guest_xpath="//li[contains(text(),'Guests')]"
    list_registered_xapth="//li[contains(text(),'Registered')]"
    list_vendor_xpath="//li[contains(text(),'Vendors')]"
    drp_mngrofvendors_xpath="//select[@id='VendorId']"
    txt_admincomment_xpath="//textarea[@id='AdminComment']"
    btn_save_xapath="//button[@name='save']"

    def __init__(self,driver):
        self.driver=driver

    def clickonCustomer(self):
        self.driver.find_element(By.XPATH,self.link_customer_xpath).click()

    def clickonSubcustomer(self):
        self.driver.find_element(By.XPATH,self.link_subcustomer_xpath).click()

    def clickonAddcustomer(self):
        self.driver.find_element(By.XPATH,self.btn_addnew_xpath).click()

    def setEmail(self,email):
        self.driver.find_element(By.ID,self.txt_email_id).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element(By.ID,self.txt_password_id).send_keys(password)

    def setFastname(self,fname):
        self.driver.find_element(By.ID,self.txt_firstname_id).send_keys(fname)

    def setLname(self,lname):
        self.driver.find_element(By.ID,self.txt_lastname_id).send_keys(lname)

    def setGender(self,gender):
        if gender=="male":
            self.driver.find_element(By.ID,self.rd_male_id).click()
        else:
            self.driver.find_element(By.ID,self.rd_female_id).click()

    def setDob(self,dob):
        self.driver.find_element(By.ID,self.txt_dob_id).send_keys(dob)

    def setComany(self,company):
        self.driver.find_element(By.ID,self.txt_company_id).send_keys(company)

    def settax(self,tax):
        if tax=="yes":
            self.driver.find_element(By.ID,self.chkbox_tax_id).click()
        else:
            print("noexpt")

    def news_ltr(self,ltr):
        self.driver.find_element(By.XPATH,self.list_newsltr_xpath).click()
        time.sleep(3)
        if ltr=="Your store name":
            self.list=self.driver.find_element(By.XPATH,self.list_storename_xpath)
        else:
            self.list=self.driver.find_element(By.XPATH,self.list_teststore_xpath)
            time.sleep(3)
            self.driver.execute_script("arguments[0].click();", self.list)


    def setCustomrole(self,role):
        self.driver.find_element(By.XPATH,self.list_custrole_xpath).click()
        time.sleep(3)

        if role=="Administrators":
            self.listitems=self.driver.find_element(By.XPATH,self.list_admin_xpath)

        elif role=="Registered":
            self.listitems=self.driver.find_element(By.XPATH,self.list_registered_xapth)

        elif role=="Forum moderator":
            self.listitems=self.driver.find_element(By.XPATH,self.list_forum_xapth)

        elif role=="Vendor":
           self.listitems= self.driver.find_element(By.XPATH,self.list_vendor_xpath)

        elif role=="Guest":
            # Here user can be Registered( or) Guest, only one
            self.driver.find_element(By.XPATH,"//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listitems=self.driver.find_element(By.XPATH,self.list_guest_xpath)

        else:
            self.listitems=self.driver.find_element(By.XPATH,self.list_guest_xpath)
            time.sleep(3)
            # self.listitem.click()
            self.driver.execute_script("arguments[0].click();", self.listitems)

    def setManagerofvendor(self,value):
        drp=Select(self.driver.find_element(By.XPATH,self.drp_mngrofvendors_xpath))
        drp.select_by_visible_text(value)

    def setAdmincomment(self,comment):
        self.driver.find_element(By.XPATH,self.txt_admincomment_xpath).send_keys(comment)

    def clickonSave(self):
        self.driver.find_element(By.XPATH,self.btn_save_xapath).click()















