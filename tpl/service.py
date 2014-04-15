#!/usr/bin/env python2.7
#! -*- coding: UTF-8  -*-
#! author: hefei1986@gmail.com

import os
import sys
import re
import signal
import logging
import cjson

import tornado
import tornado.web
import tornado.ioloop
import tornado.httpserver
from tornado.options import define, options

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, ROOT_DIR)

from handlers.PingHandler import PingHandler
from utils.AutoReloadConfig import AutoReloadConfig
from config.settings import APP_CONFIG

print "version of tornado now is %s." % (tornado.version, )

define("port", default=46010, help="run on the given port", type=int)
define("proc", default=8, help="the number of process", type=int)
define("magicstring", default="", help="fare_pricecomputing", type=str)

class Application(tornado.web.Application):
    """A collection of request handlers that make up a web application."""

    def __init__(self):
        """construting function."""

        handlers = [
            (r"/ping/", PingHandler),
        ]
        
        settings = {}
        tornado.web.Application.__init__(self, handlers, **settings) 

def handle_sigint(sig, frame):
    """gently exit."""
    tornado.ioloop.IOLoop.instance().add_callback(tornado.ioloop.\
                                                  IOLoop.instance().stop)
def handle_check():
    """check whether its father has died."""
    if os.getppid() == 1:
        logger = logging.getLogger("debug")
        logger.warning("Father died!")
        tornado.ioloop.IOLoop.instance().add_callback(tornado.ioloop.\
                                                  IOLoop.instance().stop)
         
def main():
    """main."""
    signal.signal(signal.SIGINT, handle_sigint)
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.bind(options.port)
    http_server.start(options.proc)
    
    # 注册自检定时器
    tornado.ioloop.PeriodicCallback(handle_check, 1000 * 5).start()
    
    # 注册站点配置的自动更新定时器
    site_config = AutoReloadConfig(APP_CONFIG["config_path"])
    site_config.start_timer(APP_CONFIG["config_reload_interval"])
    
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()

