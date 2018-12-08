# -*- coding:utf-8 -*-
# project name: yunbao v4.0.5
# author: "HSF"
# creation time: 2018/7/4 18:11
# Email: bingdiao6050@126.com

import os
import logging.config
path = os.path.dirname(os.path.realpath(__file__))
print(path)



logging.config.fileConfig("%s/logger.conf" % path)
logger = logging.getLogger("root")


if __name__ == "__main__":
    # logger = logs()
    logger.error('错误咯')
    logger.info('运行日志')
    logger.debug('调试日志')
    logger.warning('不知道')
    logger.critical('不懂')
