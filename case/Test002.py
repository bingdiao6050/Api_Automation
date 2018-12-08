# !/usr/bin/env python
# -*- coding:utf-8 -*-
# project name: yunbao_api_autotest
# author: "HSF"
# creation time: 2018/11/21  09:41
# Email: bingdiao6050@126.com

import unittest
import json
import ddt
import requests
from common.excelread import ExcelUtil
from config.param import paramters


pa = paramters()

# data = ExcelUtil("M:\\PaySvn\\08_AutoTest\\yunbao_api_autotest\\config\\juese.xlsx","Sheet1")
# l = data.dict_data()
# for i in l:
#     name = i['name']
#     code = i['code']
#     ordinal = i['ordinal']



class TestClass(unittest.TestCase):
    '''商户后台-财务管理-提现申请'''
    def setUp(self):
        print("start")
        data = ExcelUtil("M:\\PaySvn\\08_AutoTest\\yunbao_api_autotest\\config\\juese.xlsx","Sheet1")
        l = data.dict_data()
        for i in l:
            self.name = i['name']
            self.code = i['code']
            self.ordinal = i['ordinal']
        return self.name,self.code,self.ordinal



    def tearDown(self):
        print("end")

    def test01(self):
        '''查看钱包信息'''

        #制作协议包
        self.url = "http://192.168.1.203:8082/merchant/wallet/info"
        self.headers = {"Host":"192.168.1.203:8082",
                   "Origin":"http://192.168.1.203:8092",
                   "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
                   "A-Authorization":pa.token(),
                   "Content-Type":"application/json; charset=UTF-8",
                   "Referer":"http://192.168.1.203:8092/"
                   }

        #发送get请求
        r = requests.get(url=self.url,headers=self.headers)
        y = r.json()
        print(y)
        self.assertEqual("200",str(y['code']))
        self.assertEqual("True",str(y['success']))

    def test02(self):
        '''查看商户信息'''

        #制作协议包
        self.url = 'http://192.168.1.203:8082/merchant/user/current'
        self.headers = {"Host":"192.168.1.203:8082",
                   "Origin":"http://192.168.1.203:8092",
                   "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
                   "A-Authorization":pa.token(),
                   "Content-Type":"application/json; charset=UTF-8",
                   "Referer":"http://192.168.1.203:8092/"
                   }

        #发送get请求
        r = requests.get(url= self.url,headers= self.headers)
        y = r.json()
        print(y)
        self.assertEqual("yunbaotest123",str(y['account']))

    def test03(self):
        '''新增角色'''

        #制作协议包
        self.setUp()
        self.url = 'http://192.168.1.203:8082/merchant/role/add'
        self.headers = {"Host":"192.168.1.203:8082",
                   "Origin":"http://192.168.1.203:8092",
                   "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
                   "A-Authorization":pa.token(),
                   "Content-Type":"application/json; charset=UTF-8",
                   "Referer":"http://192.168.1.203:8092/"
                   }
        self.data = {"name":self.name,
             "code":self.code,
             "ordinal":self.ordinal}
        self.data = json.dumps(self.data)
        #发送get请求
        r = requests.post(url= self.url,headers= self.headers,data= self.data)
        y = r.json()
        print(y)
        self.assertEqual("True",str(y['success']))


if __name__ == '__main__':
    unittest.main()