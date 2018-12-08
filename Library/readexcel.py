# !/usr/bin/env python
# -*- coding:utf-8 -*-
# project name: yunbao_api_autotest
# author: "HSF"
# creation time: 2018/11/21  09:41
# Email: bingdiao6050@126.com

from common.excelread import ExcelUtil

def readexcel(filepath,sheetNum):
    '''读取excel数据'''
    data = ExcelUtil(filepath,sheetNum)
    readexcel = data.dict_data()
    # print(readexcel)
    return readexcel



if __name__=="__main__":
    readexcel("M:\\PaySvn\\08_AutoTest\\yunbao_api_autotest\\config\\loginusername.xlsx","Sheet1")
