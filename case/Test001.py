# !/usr/bin/env python
# -*- coding:utf-8 -*-
# project name: yunbao_api_autotest
# author: "HSF"
# creation time: 2018/11/21  09:41
# Email: bingdiao6050@126.com

import json
import requests
import unittest
from Library.translate_pic import trans_yzm
from Library.verificationCode import code_demo
import os
from common.excelread import ExcelUtil

data = ExcelUtil("M:\\PaySvn\\08_AutoTest\\yunbao_api_autotest\\config\\loginusername.xlsx","Sheet1")
l = data.dict_data()
for i in l:
    username = i['username']
    password = i['password']


class TestClass(unittest.TestCase):
    """商户后台登陆"""

    def test01(self):
        '''打开网页'''
        self.url = 'http://192.168.1.203:8082/captcha'
        self.headers ={"Host":"192.168.1.203:8082",
                       "Origin":"http://192.168.1.203:8092",
                       "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
                       "A-Authorization":"Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJjYzExIiwiaWQiOjQsInNvdXJjZUlkIjozLCJ0ZXN0ZXIiOjAsInBsYXRmb3JtSWQiOjgsIm5hbWUiOiJjYzExIiwicm9sZUlkIjozMjgsInJvbGVDb2RlIjoiMTIzNCIsInJvbGVOYW1lIjoidGVzdCIsIm9ubGluZSI6ImRlMjM4MTkwLTA4MDktNGEzNy05YjEyLTkxNzEzM2U4YzBjMiIsImlwIjoiMTkyLjE2OC4zMC4yNTMiLCJtb2JpbGUiOiIxMzQxMDk2MDA5NCIsImlzcyI6ImFsZWMiLCJpYXQiOjE1NDI3MDUzNTQsImV4cCI6MTU0MjcyNjk1NH0.RNs5USuody6CILU_QQc4FOYkwITXBlGGvkazpYQPiBu5QTvAHWEhx3NGSx2c30gY2ZuZ8mNvNED9Ohe6123s5q",
                       "Content-Type":"application/json; charset=UTF-8",
                       "Referer":"http://192.168.1.203:8092/"
                       }
        r = requests.get(url = self.url,headers = self.headers)

        y = r.json()
        img = y['img']
        self.token = y['token']
        self.assertIn("200",str(y['code']))
        self.assertIn("True",str(y['success']))
        trans_yzm(img)
        path = os.path.realpath(__file__)[:-22]
        self.value = code_demo('15521108558', 'passwd123',path + '\\img\\verificationCode.png', '7100')
        print(self.value)



    def test02(self):
        '''登陆'''
        self.test01()
        self.url = 'http://192.168.1.203:8082/auth/login'
        self.headers ={"Host":"192.168.1.203:8082",
                       "Origin":"http://192.168.1.203:8092",
                       "Captcha-token":self.token,
                       "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
                       "Content-Type":"application/json; charset=UTF-8",
                       "Referer":"http://192.168.1.203:8092/"
                       }
        self.data = {"captcha":self.value,
                     "username":username,
                     "password":password}
        self.data = json.dumps(self.data)

        r = requests.post(url= self.url, headers = self.headers, data = self.data)
        y = r.json()
        # print(y)
        self.assertEqual ("200",str(y['code']))
        self.assertEqual ('True',str(y['success']))

    def test03(self):
        '''发送短信验证码'''
        self.url = 'http://192.168.1.203:8082/auth/code'
        self.headers = {"Host":"192.168.1.203:8082",
                        "Origin":"http://192.168.1.203:8092",
                        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
                        "A-Authorization":"Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ5dW5iYW90ZXN0MTIzIiwiaWQiOjExLCJzb3VyY2VJZCI6NywidGVzdGVyIjowLCJwbGF0Zm9ybUlkIjoxLCJuYW1lIjoi6LaF57qn566h55CG5ZGYIiwicm9sZUlkIjoxLCJyb2xlQ29kZSI6ImFkbWluIiwicm9sZU5hbWUiOiLotoXnuqfnrqHnkIblkZgiLCJvbmxpbmUiOiI1ZDJhYWY1OC00YzhkLTQzOGEtYTczOC00ODQyNWYzM2FkMTkiLCJpcCI6IjE5Mi4xNjguMzAuMjUzIiwibW9iaWxlIjoiMTU1MjExMDg1NTgiLCJpc3MiOiJhbGVjIiwiaWF0IjoxNTQyODY3NTA1LCJleHAiOjE1NDI4ODkxMDV9.I58wIR3X9_gB1-hUreYvg1QAfm8jhSHu2A_l9mdcHoMlLIG4mtie_8Yg7Ev3AX0Q1k-ggA9OGPlEEZDBzswljg",
                        "Content-Type":"application/json; charset=UTF-8",
                        "Referer":"http://192.168.1.203:8092/"
                        }
        r = requests.get(url= self.url,headers= self.headers)
        y = r.json()
        self.assertEqual("200",str(y['code']))
        self.assertEqual("True",str(y['success']))
        print(y)

if __name__ == "__main__":
    unittest.main()

