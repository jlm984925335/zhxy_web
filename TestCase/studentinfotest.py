import unittest
from selenium import webdriver
from PageObject.studentinfopage import Studentinfo_Page
from PageObject.loginpage import Login_Page
from time import sleep
import os
import logging
from Common.my_log import My_Log
from Common.basepage import Base_Page


class Studentinfo_Test(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome()
        cls.url="https://console.2035kids.com/#/login?redirect=%2F"
        cls.driver.get(cls.url)
        cls.driver.maximize_window()
        cls.login(self=cls,driver=cls.driver, username="19216900003", password="123456xyz")
        # cls.logging = My_Log().get_log()
        logging.info("******开始学生信息测试******")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        logging.info("******结束学生信息测试******")
        My_Log().close_handle()

    # 登录流程
    def login(self, driver, username, password):
        po = Login_Page(driver)
        # po.open()
        po.user_input(username)
        po.pass_input(password)
        po.login_button()

    # @unittest.skip
    # 测试新增功能
    def test1_add(self):
        driver=self.driver
        # self.login(driver, "19216900003", "123456xyz")
        # driver.implicitly_wait(20)
        sleep(1)
        driver.get("https://console.2035kids.com/#/baseData/students/info")
        driver.refresh()
        po=Studentinfo_Page(driver)
        message=po.add("9043","学43","18143469043","学43家长")
        # sleep(0.5)
        try:
            self.assertEqual(message,"新增成功!")
            logging.info("新增学生成功")
        except Exception as e:
            logging.info(e)
            Base_Page(driver).save_screenshots("学生信息测试")
            raise

    # @unittest.skip
    # 测试上传头像
    def test2_upload_headimg(self):
        driver = self.driver
        # sleep(3)
        driver.get("https://console.2035kids.com/#/baseData/students/info")
        # sleep(3)
        # Base_Page(driver).by_xpath("//li[text()='11']").click()
        # sleep(3)
        # 获取人脸图片的绝对路径
        file_path = os.path.abspath('./TestData/人脸.jpg')
        po = Studentinfo_Page(driver)
        # sleep(3)
        message=po.upload_headimg("学43",file_path)
        try:
            self.assertEqual(message,"人脸上传成功")
            logging.info("人脸上传成功")
        except Exception as e:
            logging.info(e)
            Base_Page(driver).save_screenshots("学生信息测试")
            raise

    # 测试删除学生
    def test3_delete(self):
        driver=self.driver
        # sleep(3)
        driver.get("https://console.2035kids.com/#/baseData/students/info")
        # sleep(3)
        po=Studentinfo_Page(driver)
        message=po.delete("学43")
        try:
            self.assertEqual(message,"删除成功")
            logging.info("删除学生成功")
        except Exception as e:
            logging.info(e)
            Base_Page(driver).save_screenshots("学生信息测试")
            raise



    # @unittest.skip
    # # 测试下载模板
    # def test_download_muban(self):
    #     driver=self.driver
    #     path = 'C:/Users/靳立民/Downloads'
    #     sleep(3)
    #     driver.get("https://console.2035kids.com/#/baseData/students/info")
    #     file1 = int(len([lists for lists in os.listdir(path) if os.path.isfile(os.path.join(path, lists))]))
    #     sleep(3)
    #     Studentinfo_Page(driver).download_muban()
    #     sleep(20)
    #
    #     file2 = int(len([lists for lists in os.listdir(path) if os.path.isfile(os.path.join(path, lists))]))
    #     self.assertNotEqual(file1,file2)
    #     print(file1,file2)




if __name__ == '__main__':
    unittest.main()

