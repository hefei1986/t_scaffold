#!/usr/bin/env python2.7
#! -*- coding: UTF-8 -*-
#! author: hefei1986@gmail.com

import os
import sys
import logging
from configobj import ConfigObj
from logging.config import dictConfig

# 全局配置
CONF_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = CONF_DIR + "/../"
sys.path.insert(0, ROOT_DIR)

# 确定日志文件目录
LOG_PATH = ROOT_DIR + '/logs/'

MODULE_NAME = "$MODULE_NAME"

# 确定日志级别
LOG_LEVEL = "INFO"

# 程序配置
APP_CONFIG = {}
APP_CONFIG["config_path"] = ROOT_DIR + '/config/config.json'
APP_CONFIG["config_reload_interval"] = 15

# 日志配置
LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[%(levelname)s] %(asctime)s %(module)s %(lineno)d %(process)d %(thread)d %(message)s',
        },
        'simple': {
            'format': '[%(levelname)s] %(asctime)s %(message)s',
        },
    },
    'filters': {
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console':{
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'debug':{
            'level': 'DEBUG',
            'class':'third_party.MultiProcessTimedRotatingFileHandler.MultiProcessTimedRotatingFileHandler',
            'filename': os.path.join(LOG_PATH, MODULE_NAME + 'debug.log'),
            'backupCount': 0,
            'when': 'midnight',
            'formatter':'verbose',
        }, 
        'wf':{
            'level': 'INFO',
            'class':'third_party.MultiProcessTimedRotatingFileHandler.MultiProcessTimedRotatingFileHandler',
            'filename': os.path.join(LOG_PATH, MODULE_NAME + 'wf.log'),
            'backupCount': 0,
            'when': 'midnight',
            'formatter':'verbose',
        }, 
    },
    'loggers': {
        'debug': {
            'handlers': ['debug'],
            'propagate': False,
            'level': LOG_LEVEL,
        },
        'wf': {
            'handlers': ['wf'],
            'propagate': False,
            'level': LOG_LEVEL,
        },
    }
}

## enable the logging config
dictConfig(LOGGING_CONFIG)
