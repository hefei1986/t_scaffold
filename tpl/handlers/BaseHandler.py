#!/usr/bin/env python2.7
#! coding: UTF-8
#! author: hefei@kuxun.com


"""
"""

import re
import time
import urllib
import cjson
import logging
import traceback
import copy

import tornado


class BaseHandler(tornado.web.RequestHandler):
    """Abstract class integrated public property."""

    def on_finish(self):
        """last words."""
        pass
