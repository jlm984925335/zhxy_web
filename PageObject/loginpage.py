from Common.basepage import Base_Page
from selenium import webdriver
from time import sleep
from Common.my_log import My_Log
import logging

class Login_Page(Base_Page):

    # url="https://console.2035kids.com/#/login?redirect=%2F"
    def __init__(self,driver):
        self.driver=driver

        # self.driver.get(url)
    def user_input(self,username):
        self.by_css("input[name='username']").send_keys(username)



    def pass_input(self,password):
        self.by_css("input[name='password']").send_keys(password)

    def school(self):
        self.by_css("input[placeholder='请选择学校']").click()

    def select_school(self):
        self.by_css("[text()='杭州书僮实验学校']").click()
        # self.find_element_by_xpath("/html/body/div[2]/div[1]/div[1]/ul/li[1]/span").click()
    def login_button(self):
        self.by_css("button[style='width: 100%;']").click()
    # 获取弹出消息
    def get_message(self):
        message=self.by_xpath("//p[text()='账号或密码错误']").text
        # message=self.by_css("p[text='账号或密码错误']")
        # sleep(3)
        return message
    # 获取提示语
    def get_prompts1(self):


        prompts1=self.by_xpath("/html/body/div/div/form/div[1]/div[2]/div/div[2]").text
        return prompts1

    def get_prompts2(self):
        prompts2 = self.by_xpath("/html/body/div/div/form/div[1]/div[3]/div/div[2]").text
        return prompts2


if __name__=="__main__":
    driver=webdriver.Chrome()
    url="https://console.2035kids.com/#/login?redirect=%2F"
    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(10)
    po=Login_Page(driver)
    po.user_input("19216900003")
    po.pass_input("123456xyz")
    # # sleep(3)
    po.login_button()
    # driver.get("https://console.2035kids.com/#/baseData/schoolDataForOne")
    sleep(3)
    driver.get("https://console.2035kids.com/#/baseData/students/info")
    driver.refresh()

    # driver.find_element_by_xpath("//span[text()='新增']").click()
    driver.find_element_by_css_selector(".el-icon-plus").click()
    # driver.switch_to_alert()
    # print(po.get_prompts1())
    # po.school()
    # sleep(5)
    # po.select_school()
    # po.login_button()
    sleep(3)
    driver.quit()
