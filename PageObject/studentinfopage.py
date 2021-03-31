from Common.basepage import Base_Page
from selenium import webdriver
from TestCase.logintest import Login_Test
from time import sleep
import os

class Studentinfo_Page(Base_Page):
    def __init__(self,driver):
        self.driver=driver
    def seek(self):
        pass
    def select_grade(self):
        pass
    def select_name(self):
        pass

    #新增
    def add(self,id,stuname,phone,parentname):
        self.driver.implicitly_wait(10)
        sleep(2)
        self.by_css(".el-icon-plus").click()
        self.by_xpath("/html/body/div[1]/div/section/section/div/div/div[4]/div/div[2]/form/div[1]/div/div/div/input").click()
        self.by_xpath("/html/body/div[3]/div[1]/div[1]/div[1]/ul/li[3]/span").click()
        self.by_xpath("/html/body/div[3]/div[1]/div[2]/div[1]/ul/li[3]/span").click()
        self.by_css("input[placeholder='请输入学号']").send_keys(id)
        self.by_css("input[placeholder='请输入学生姓名']").send_keys(stuname)
        self.by_css("input[placeholder='请输入家长手机号']").send_keys(phone)
        self.by_css("input[placeholder='请输入家长姓名']").send_keys(parentname)
        self.by_xpath("/html/body/div[1]/div/section/section/div/div/div[4]/div/div[3]/div/button[2]/span").click()
        # sleep(3)
        # driver.switch_to.alert
        # 获取新增成功提示语内容
        message = self.by_xpath("//div[@class='el-message el-message--success']/p").text
        # print(message)
        return message


    # 上传头像
    def upload_headimg(self,name,file_path):
        # self.driver.implicitly_wait(20)
        sleep(1)
        self.by_css("input[placeholder='请输入姓名/学号']").send_keys(name)
        self.by_xpath("//*[@id='app']/div/section/section/div/div/div[1]/div/div[1]/div/div[3]/div/div/button[1]").click()
        self.by_xpath("//*[@id='app']/div/section/section/div/div/div[2]/div[3]/table/tbody/tr/td[6]/div/span/i").click()

        self.by_css("input[name='file']").send_keys(file_path)
        sleep(3)
        # self.driver.switch_to.alert
        # 获取人脸上传后的提示语内容
        # message = self.by_xpath("//p[text()='人脸上传成功']").text
        message=self.by_css("p[class='el-message__content']").text
        return message




    # 删除学生
    def delete(self,name):
        # self.driver.implicitly_wait(20)
        sleep(1)
        self.by_css("input[placeholder='请输入姓名/学号']").send_keys(name)

        self.by_xpath("//*[@id='app']/div/section/section/div/div/div[1]/div/div[1]/div/div[3]/div/div/button[1]").click()

        self.by_xpath("//*[@id='app']/div/section/section/div/div/div[2]/div[4]/div[2]/table/tbody/tr/td[14]/div/div/button[3]").click()

        # sleep(3)
        # self.driver.accept()
        self.by_xpath("/ html / body / div[2] / div / div[3] / button[2] / span").click()

        # 获取删除成功提示语内容
        message = self.by_xpath("//div[@class='el-message el-message--success']/p").text
        # print(message)
        return message

    def export(self):
        pass

    def download_muban(self):
        self.by_xpath("//span[text()='下载模板']").click()



if __name__ == '__main__':
    driver=webdriver.Chrome()
    driver.get("https://console.2035kids.com/#/login?redirect=%2F")
    driver.maximize_window()
    driver.implicitly_wait(10)
    Login_Test().login(driver,"19216900003","123456xyz")

    sleep(3)

    driver.get("https://console.2035kids.com/#/baseData/students/info")
    driver.refresh()
    sleep(5)
    # Studentinfo_Page(driver).add("9043","学43","18143469043","学43家长")
    # sleep(3)
    # Base_Page(driver).by_xpath("//li[text()='11']").click()
    # sleep(3)
    # # 定义上传的文件路径
    # file_path = os.path.abspath('C:/Users/靳立民/Pictures/人脸.jpg')
    # a=Studentinfo_Page(driver).upload_headimg(file_path)
    # print(a)
    # Studentinfo_Page(driver).download_muban()
    Studentinfo_Page(driver).delete("学43")

