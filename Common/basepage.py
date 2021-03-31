"""
使用pyhton+selenium+po+unittest测试智慧校园控制台
"""
from selenium import webdriver
import logging
import time
import os
import datetime


class Base_Page():

    def __init__(self,driver):
        self.driver=driver


    def open(self,url):
        self.driver.get(url)

    def by_css(self,css):

        try:
            # self.save_screenshots("登录页面_登录测试")
            return self.driver.find_element_by_css_selector(css)

        except Exception as e:
            logging.info(e)
            # now=datetime.datetime.now()


    def by_xpath(self,xpath):
        try:
            return self.driver.find_element_by_xpath(xpath)
        except Exception as e:
            logging.info(e)

    #保存截图
    def save_screenshots(self,doc):

        base_path = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]
        # 截图路径
        screenshot_path = os.path.join(base_path, r'Screenshot')
        # 图片名称：模块名_页面名称_操作名称_年-月-日_时分秒.png
        # filePath = "截图路径" + "{0}".format(time.strftime("%Y%m%d%H%M%S"))
        filePath = screenshot_path + "\{0}_{1}.png".format( doc,time.strftime("%Y-%m-%d %H-%M-%S", time.localtime()))
        try:
            self.driver.save_screenshot(filePath)
            logging.info("截取网页成功，文件路径为：{}".format(filePath))
        except:
            logging.exception('截取网页失败!')


if __name__=="__main__":
    pass
