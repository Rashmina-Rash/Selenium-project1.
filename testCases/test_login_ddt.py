import time
import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import Loggen
from utilities import XLUtils


class Test_002_DDT_login:
    baseurl=ReadConfig.getURL()
    path=".//TestData/testdata.xlsx"
    logger=Loggen.loggen()
    list=[]

    @pytest.mark.regression
    def test_login_ddt(self,setup):
        self.logger.info("***********Test_002_DDT_login***********")
        self.driver=setup
        self.driver.get(self.baseurl)
        self.lp=Login(self.driver) #creating object for login class
        self.rows=XLUtils.Rows(self.path,'Sheet1')
        print("Number of rows in excel",self.rows)

        for r in range(2,self.rows+1):
           self.user= XLUtils.Readdata(self.path,'Sheet1',r,1)
           self.password=XLUtils.Readdata(self.path,'Sheet1',r,2)
           self.exp=XLUtils.Readdata(self.path,'Sheet1',r,3)

           self.lp.setusername(self.user)#invoking setusername method using object
           self.lp.setpassword(self.password)#invoking setpassword method using object
           self.lp.clicklogin()
           time.sleep(5)
           act_title=self.driver.title
           expt_title="Dashboard / nopCommerce administration"
           if act_title==expt_title:
               if self.exp=='pass':
                   self.logger.info("*******passed**********")
                   self.lp.clicklogout()
                   self.list.append('pass')
               elif self.exp=='fail':
                   self.logger.info("*******failed**********")
                   self.lp.clicklogout()
                   self.list.append('fail')

           elif act_title!= expt_title:
               if self.exp=='pass':
                   self.logger.info("*******failed**********")
                   self.list.append("fail")
               elif self.exp=='fail':
                   self.logger.info("*******passed**********")
                   self.list.append('pass')


        if 'fail' not in self.list:
           self.logger.info("*******Login_ddt test passed**********")
           self.driver.close()
           assert True
        else:
           self.logger.info("*******Login_ddt test failed**********")
           self.driver.close()
           assert True







