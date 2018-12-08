# !/usr/bin/env python
# -*- coding:utf-8 -*-
# project name: yunbao_api_autotest
# author: "HSF"
# creation time: 2018/11/21  09:41
# Email: bingdiao6050@126.com

import unittest
import os
import time
from Library.email import *



def all_case():
    '''执行用例'''

    #待执行用力的目录
    cur_path = os.path.dirname(os.path.realpath(__file__))

    case_path = os.path.join(cur_path, "case") #测试用例的路径

    testcase =unittest.TestSuite()


    discover = unittest.defaultTestLoader.discover(case_path, "Test005.py")

    #discover方法筛选出来的用例，循环添加到测试套件中
    # for test_suite in discover:
    #     for test_case in test_suite:
    #         #添加用例到testcase
    #         testcase.addTests(test_case)
    # print(testcase)
    # return testcase
    testcase.addTests(discover) # 直接加载 discover
    print(testcase)
    return testcase




if __name__ =="__main__":
    #返回实例
    runner = unittest.TextTestRunner()
    import HTMLTestRunner
    # cur_path = os.path.dirname(os.path.realpath(__file__))
    # path = "Report\\"
    timeStr = time.strftime('%Y-%m-%d-%H', time.localtime(time.time()))
    report_path = "Report\\TestReport%s.html" % timeStr


    fp = open(report_path, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(
                stream=open(report_path, "wb"),
                title='支付接口自动化测试报告',
                tester='胡世方',
                description='This demonstrates the report output by HTMLTestRunner.'
                )

    # run 所有用例
    runner.run(all_case())
    fp.close()
    mail("bingdiao6050@qq.com")





