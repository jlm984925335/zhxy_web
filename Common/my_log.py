import logging
import os
from datetime import datetime

class My_Log(object):
    def __init__(self):
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.INFO)

        # 2.将log信息输出到log文件中
        # 2.1 先定位看将log文件输出到哪里去
        # current_dir = os.path.dirname(os.path.abspath(__file__))
        # print(current_dir)  # D:\MySpace\Python\WebTesting\util
        log_dir = os.path.join('./Log')
        # 日志名称构建
        log_file_name = datetime.now().strftime("%Y-%m-%d") + '日志.log'
        log_file_path = log_dir + '/' + log_file_name
        # print(log_file_path)

        # 2.2 好的，将日志写进log文件中
        self.file_handle = logging.FileHandler(log_file_path, 'a', encoding='utf-8')
        formatter = logging.Formatter(
            '\n %(asctime)s %(filename)s %(funcName)s %(levelno)s: [%(levelname)s] ---> %(message)s \n')
        self.file_handle.setFormatter(formatter)
        self.logger.addHandler(self.file_handle)

    def get_log(self):
        return self.logger

    def close_handle(self):
        self.logger.removeHandler(self.file_handle)
        self.file_handle.close()

if __name__ == "__main__":
    log = My_Log()
    logging = log.get_log()
    logging.info('输出到文件中去')
    log.close_handle()