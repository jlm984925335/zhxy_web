from HTMLTestRunnerCN import HTMLTestReportCN
# from  Common.file_path import *
import time
import unittest
from Common.send_email import Send_Email


def Run_All():
        # 使用discover找到一个目录下所有测试用例
        discover=unittest.defaultTestLoader.discover("./TestCase",pattern="*test.py")
        now_time=time.strftime("%Y_%m_%d_%H_%M_%S")
        fp = open("./Report/"+now_time+'.html','wb')
        runner = HTMLTestReportCN(
                stream=fp,
                title="智慧校园控制台自动化测试报告",
                description="智慧校园控制台自动化测试报告",
                tester="靳立民"

        )
        runner.run(discover)
        fp.close()
        # 测试报告存放位置
        reports_address = './Report'
        # 查找最新生成的测试报告地址
        new_report_addre = Send_Email().acquire_report_address(reports_address)
        # print(new_report_addr)
        # 自动发送邮件
        Send_Email().send_email(new_report_addre)

if __name__ == '__main__':
    Run_All()