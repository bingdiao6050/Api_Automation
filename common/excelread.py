# !/usr/bin/env python
# -*- coding:utf-8 -*-
# project name: yunbao_api_autotest
# author: "HSF"
# creation time: 2018/11/26  09:41
# Email: bingdiao6050@126.com

import xlrd

class ExcelUtil():

    def __init__(self,excelPath,sheetName):

        self.data = xlrd.open_workbook(excelPath)
        self.table = self.data.sheet_by_name(sheetName)
        #获取第一行作为key值
        self.keys = self.table.row_values(0)
        #获取总行数
        self.rowNum = self.table.nrows
        #获取总列数
        self.colNum = self.table.ncols

    def dict_data(self):

        if self.rowNum <= 1:
            print("总行数小于1")
        else:
            r = []
            j = 1
            for i in range(self.rowNum - 1):
                s = {}
                #从第二行取对应values值
                values = self.table.row_values(j)
                for x in range(self.colNum):
                    s[self.keys[x]] = values[x]
                r.append(s)
                j+=1
            return r



if __name__ == "__main__":
    ExcelUtil("M:\\PaySvn\\08_AutoTest\\yunbao_api_autotest\\config\\loginusername.xlsx","Sheet1")