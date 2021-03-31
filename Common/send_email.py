import os
import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from email.header import Header
import time

# 自动发送邮件
class Send_Email():
    def send_email(self, new_report_addre):
        # 读取测试报告中的内容作为邮件的内容
        with open(new_report_addre, 'r', encoding='utf-8') as f:
            mail_body = f.read()
        # 发件人地址
        send_addr = '984925335@qq.com'
        # 收件人地址
        reciver_addr = '984925335@qq.com'
        # 发送邮箱的服务器地址 qq邮箱是'smtp.qq.com', 163邮箱是'smtp.163.com'
        mail_server = 'smtp.qq.com'
        now = time.strftime("%Y-%m-%d %H:%M:%S")
        # 邮件标题
        subject = '智慧校园控制台自动化测试报告' + now
        # 发件人的邮箱及邮箱授权码
        username = '984925335@qq.com'
        password = 'oevppwgbkswmbbhb'  # 注意这里是邮箱的授权码而不是邮箱密码
        # 声明全局变量the_last_report
        global the_last_report
        htmlApart = MIMEApplication(open(new_report_addre, 'rb').read())
        htmlApart.add_header('Content-Disposition', 'attachment',filename=the_last_report)
        msg_file = MIMEMultipart()
        msg_file["From"]=Header(send_addr)
        msg_file["To"]=Header(reciver_addr)
        msg_file["Subject"] = subject
        # 邮箱的内容和标题
        message = MIMEText(mail_body, 'html', 'utf-8')  # MIMEText(邮箱主体内容,内容类型,字符集）

        message["Content Type"] = "application/octet-stream"
        msg_file.attach(message)
        msg_file.attach(htmlApart)

        # 发送邮件，使用的smtp协议
        smtp = smtplib.SMTP()
        smtp.connect(mail_server)
        smtp.login(username, password)
        smtp.sendmail(send_addr, reciver_addr.split(','), msg_file.as_string())
        smtp.quit()




    # 获取最新的测试报告地址
    def acquire_report_address(self, reports_address):
        # 测试报告文件夹中的所有文件加入到列表
        test_reports_list = os.listdir(reports_address)
        # 按照升序排序生成新的列表
        new_test_reports_list = sorted(test_reports_list)
        # 获取最新的测试报告
        global the_last_report
        the_last_report = new_test_reports_list[-2]
        # 最新的测试报告地址
        the_last_report_address = os.path.join(reports_address, the_last_report)
        return the_last_report_address




if __name__ == '__main__':
    # 测试报告存放位置
    reports_address = '../Report'
    # 查找最新生成的测试报告地址
    new_report_addre = Send_Email().acquire_report_address(reports_address)
    # print(new_report_addr)
    # 自动发送邮件
    Send_Email().send_email(new_report_addre)
