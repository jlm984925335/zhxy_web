import unittest
from time import sleep
from selenium import webdriver
from PageObject.loginpage import Login_Page
import logging
from Common.my_log import My_Log
from Common.basepage import Base_Page



class Login_Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.url_1 ="https://console.2035kids.com/#/login?redirect=%2F"
        cls.driver.get(cls.url_1)
        cls.driver.maximize_window()

        cls.logging = My_Log().get_log()

        logging.info("******开始登陆测试******")

    @classmethod
    def tearDownClass(cls):
        # if sys.exc_info()[0]:
        #     test_method_name = cls._testMethodName
        #     print("1")
        #     cls.driver.save_screenshot("Screenshot/%s.png" % test_method_name)
        # super(Login_Test,cls).tearDownClass()
        cls.driver.quit()
        logging.info("******结束登陆测试******")
        # My_Log().close_handle()


    # 登录流程
    def login(self,driver,username,password):
        po=Login_Page(driver)
        # po.open()
        po.user_input(username)
        # logging.info("输入账号%s"%username)
        po.pass_input(password)
        # logging.info("输入密码%s"%password)
        po.login_button()



    #测试输入正确的用户名和密码
    def test1_login(self):
        # self.driver.get(self.url_1)
        driver=self.driver
        self.login(driver,"19216900003","123456xyz")
        sleep(3)
        current_url = self.driver.current_url
        url_2 = "https://console.2035kids.com/#/healthManage/morningNoonCheck/morningNoonCheckPreliminaryForOne"
        # self.assertEqual(current_url, url_2)
        try:
            self.assertEqual(current_url, url_2,msg="登录失败，网址不一致")
            logging.info("用例1通过")
        except Exception as e:
            logging.info(e)
            Base_Page(driver).save_screenshots("登录测试")
            raise
            
    # 测试输入正确的用户名和错误的密码
    def test2_login(self):
        self.driver.get(self.url_1)
        driver=self.driver
        po=Login_Page(driver)
        self.login(driver,"19216900003","123456")
        sleep(1)
        # driver.switch_to.alert
        message=po.get_message()
        try:
            self.assertEqual(message,'账号或密码错误')
            logging.info("用例2通过")
        except Exception as e:
            logging.info(e)
            Base_Page(driver).save_screenshots("登录测试")
            raise

    # 测试不输入用户名和密码
    def test3_login(self):
        # self.driver.get(self.url_1)
        driver = self.driver
        driver.refresh()
        po = Login_Page(driver)
        sleep(3)
        self.login(driver, "", "")
        sleep(5)
        prompts1 = po.get_prompts1()
        prompts2 = po.get_prompts2()
        try:
            self.assertEqual(prompts1, "请输入用户名")
            self.assertEqual(prompts2, "密码不能小于5位")
            logging.info("用例3通过")
        except Exception as e:
            logging.info(e)
            Base_Page(driver).save_screenshots("登录测试")
            raise
    # # 测试输入错误的用户名和错误的密码
    # def test_login3(self):
    #     # self.driver.get(self.url_1)
    #     driver=self.driver
    #     driver.refresh()
    #     sleep(3)
    #     po = Login_Page(driver)
    #     self.login(driver,"18143463881","12345")
    #     sleep(1)
    #     driver.switch_to.alert
    #     message = po.get_message()
    #     self.assertEqual(message, '账号或密码d错误')
    #
    # # 测试输入错误的用户名和正确的密码
    # def test_login4(self):
    #     # self.driver.get(self.url_1)
    #     driver=self.driver
    #     driver.refresh()
    #     sleep(3)
    #     po = Login_Page(driver)
    #     self.login(driver,"18143463881","123456xyz")
    #     sleep(1)
    #     driver.switch_to.alert
    #     message = po.get_message()
    #     self.assertEqual(message, '账号或密码d错误')


    # # 测试不输入用户名和输入密码
    # def test_login6(self):
    #     self.driver.get(self.url_1)
    #     driver=self.driver
    #     self.login(driver,"","123456xyz")
    #     sleep(3)
    #     current_url = self.driver.current_url
    #     url_2 = "https://console.2035kids.com/#/temperatureStu/temperatureReport"
    #     self.assertEqual(current_url, url_2, msg="登录失败")
    # # 测试输入用户名和不输入密码
    # def test_login7(self):
    #     self.driver.get(self.url_1)
    #     driver=self.driver
    #     self.login(driver,"19216900002","123456xyz")
    #     sleep(3)
    #     current_url = self.driver.current_url
    #     url_2 = "https://console.2035kids.com/#/temperatureStu/temperatureReport"
    #     self.assertEqual(current_url, url_2, msg="登录失败")


if __name__=="__main__":
    unittest.main()
