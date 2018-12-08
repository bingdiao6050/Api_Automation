# !/usr/bin/env python
# -*- coding:utf-8 -*-
# project name: yunbao_api_autotest
# author: "HSF"
# creation time: 2018/11/22  09:41
# Email: bingdiao6050@126.com



class paramters():
    '''全局变量'''

    #token变量
    def token(self):
        token = "Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ0ZXN0NSIsImlkIjo2LCJhY2NvdW50IjoidGVzdDUiLCJ1c2VyTmFtZSI6Iua1i-ivlTUiLCJvbmxpbmUiOiJkMDA2NjEyZS0wNTIwLTQwY2QtYjU0Yy02ZTVhNTIzYzMxOWEiLCJpc3MiOiJjb2xsZWN0aW9ucyIsImlhdCI6MTU0NDI0MDM0NywiZXhwIjoxNTQ0MjUxMTQ3fQ.fgUcP9f4BVzgYfWSJL-mw7LKEEgyzxxn1RHdaI3VQQ8ftK5V2i2xaYJB7rI6lBbjDqGGQyBBsCvZ_YTpMGCwaQ"
        return token

    #url
    def url(self):
        url = "http://***.***.1.***:***/" #测试环境
        return url

    #host
    def host(self):
        host = "192.***.1.***:***" #测试环境
        return host

    #Origin
    def origin(self):
        origin = "http://***.***.1.***:***"
        return origin

    #Referer
    def referer(self):
        referer = "http://***.***.1.***:***/"
        return referer

