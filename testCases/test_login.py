import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import Loggen


class Test_001_login:
    baseurl=ReadConfig.getURL()
    username=ReadConfig.getUsername()
    password=ReadConfig.getPassword()
    logger=Loggen.loggen()

    @pytest.mark.sanity
    def test_homepagetitle(self,setup):
        self.logger.info("**********Test_001_Login***************")
        self.logger.info("**********verifying homepage title***************")
        self.driver=setup
        self.driver.get(self.baseurl)
        act_title=self.driver.title
        if act_title=="Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("**********homepage title test passed***************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homepageTitle.png")
            self.driver.close()
            self.logger.info("**********homepage title test failed***************")
            assert False

    @pytest.mark.regression
    def test_login(self,setup):
        self.driver=setup
        self.driver.get(self.baseurl)
        self.lp=Login(self.driver) #creating object for login class
        self.lp.setusername(self.username)#invoking setusername method using object
        self.lp.setpassword(self.password)#invoking setpassword method using object
        self.lp.clicklogin()
        act_title=self.driver.title
        if act_title=="Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("********* login test passed***************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png")
            self.driver.close()
            self.logger.info("********* login test failed***************")
            assert False







