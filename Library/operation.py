# !/usr/bin/env python
# -*- coding:utf-8 -*-
# project name: yunbao_api_autotest
# author: "HSF"
# creation time: 2018/11/21  09:41
# Email: bingdiao6050@126.com

from log_config.logConfig import logger
import json


class operate_method(object):
    '''操作方法'''

    #网址
    def url(self,send_url):
        url = send_url
        logger.info("测试地址：" + url)
        return url

    #转换json
    def dump(self,data):
        dump = json.dumps(data)
        logger.info(data)
        print(data)
        return dump



