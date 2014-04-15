#!/usr/bin/env python2.7
#! coding: utf-8
#! author: hefei@kuxun.com

"""
    PingHandler,测试用。
"""

import tornado

from BaseHandler import BaseHandler


class PingHandler(BaseHandler):
    """ping! pong!. [测试用]"""
    @tornado.web.asynchronous
    def get(self):
        """handle get request."""
        self.write("pong")
        self.finish()

