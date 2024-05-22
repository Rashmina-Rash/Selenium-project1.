import random
import string
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import Loggen
from pageObjects.AddcustomerPage import Addcustomer
from utilities import XLUtils

class Test_003_Addcustm:
    baseURL=ReadConfig.getURL()
    username=ReadConfig.getUsername()
    password=ReadConfig.getPassword()
    logger=Loggen.loggen()

    def test_addCustomer(self,setup):
        self.logger.info("****************Test_003_Addcustm*********************")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp=Login(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        self.logger.info("****************login successful*********************")

        self.logger.info("****************Starting addcustomer*********************")
        self.addcust=Addcustomer(self.driver)
        self.addcust.clickonCustomer()
        self.addcust.clickonSubcustomer()
        self.logger.info("************* Providing customer info **********")

        self.email = self.random_generator(7) + "@gmail.com"
        self.addcust.clickonAddcustomer()
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setFastname("Rashmina")
        self.addcust.setLname("B")
        self.addcust.setGender("Female")
        self.addcust.setDob("12/5/1995")#m/d/y
        self.addcust.setComany("tesing")
        self.addcust.settax("yes")
        self.addcust.news_ltr("Your store name")
        self.addcust.setCustomrole("Registered")
        self.addcust.setManagerofvendor("Vendor 1")
        self.addcust.setAdmincomment("This is for testing")
        self.addcust.clickonSave()
        self.logger.info("************* Saving customer info **********")

        self.logger.info("********* Add customer validation started *****************")

        self.msg=self.driver.find_element(By.TAG_NAME,"body").text
        print(self.msg)

        if "The new customer has been added successfully." in self.msg:
            assert True
            self.logger.info("********* Add customer Test Passed *********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png")  # Screenshot
            self.logger.error("********* Add customer Test Failed ************")
            assert False

        self.driver.close()
        self.logger.info("******* Ending Add customer test **********")


    def random_generator(self,char_num):
        random_email = ''
        for x in range(char_num):
            random_email += ''.join(random.choice(string.ascii_lowercase))
        return random_email
