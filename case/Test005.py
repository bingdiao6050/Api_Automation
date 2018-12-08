from common.excelread import ExcelUtil
import ddt
import unittest
from Library.readexcel import readexcel
import json
import requests
from log_config.logConfig import logger
from Library.operation import operate_method
from config.param import paramters
from Library.oper_mysql import MysqlUtil

# l = readexcel("M:\\PaySvn\\08_AutoTest\\yunbao_api_autotest\\config\\money.xlsx","Sheet1")
op = operate_method()
pa = paramters()
mysql = MysqlUtil()

l = mysql.mysql_getdict("select * FROM test_data")



@ddt.ddt

class Test(unittest.TestCase):
    '''添加配置金额'''
    def setUp(self):
        print("start")

    def tearDown(self):
        print("end!")

    # @ddt.data(*l)
    # def test_ddt1(self, l):
    #     print(l['username'])
    #     # print(l['password'])
    # # @ddt.data(*test_data2)
    # # def test_ddt2(self, data):
    # #     print(data)

    @ddt.data(*l)
    def test01(self, l):
        '''配置金额'''
        self.url = op.url(pa.url() + "api/v1/repository/quota/add")
        self.headers = {"Host":pa.host(),
                        "Connection":"keep-alive",
                        "Origin":pa.origin(),
                        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
                        "A-Authorization":pa.token(),
                        "Content-Type":"application/json; charset=UTF-8",
                        "Referer":pa.referer()
                        }
        self.data = {"price":int(l['price']),
                     "disabled":l['disabled']
                     }

        # self.data = json.dumps(self.data) #转换成json


        r = requests.post(url= self.url, headers = self.headers, data = op.dump(self.data))
        y = r.json()
        print(y)
        self.assertEqual(str(l['status']),str(y["status"]))

    def test02(self):
        '''测试用例2'''
        print("this is test02")


if __name__ == "__main__":
    unittest.main()