#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2012 Ethan Zhang<http://github.com/Ethan-Zhang> 
# Licensed under the Apache License, Version 2.0 (the "License"); you may 
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0    
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT 
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the 
# License for the specific language governing permissions and limitations
# under the License.
 
import os
import cjson
import logging
import random

from tornado import ioloop
from config.settings import APP_CONFIG

class AutoReloadConfig(object):
    
    _instance = None
    
    _mapping_dict = {
                "pata_modify_range":"106",
                "working_time":"618",
                "av_check_method":"119",
                "pata_check_method":"120",
                "enable_global_config":"111",
                "return_point":"604",
                "return_price":"607",
                "pnr_method":"121",}
    
    @staticmethod
    def get_instance():
        """static method, singleton."""
        return AutoReloadConfig._instance
 
    def __init__(self, path):
        """constructing function."""
        self._filepath = path
        AutoReloadConfig._instance = self
        self._mtime = None
        self._check()
 
    def get_config(self):
        """get config of specified site."""
        return self._config

    def _check(self):
        """check and reload."""
        logger = logging.getLogger("debug")
        logger.debug("preparing to check")
        if self._should_load():
            self._load()
 
    def _should_load(self):
        """check the modification time of the file."""
        if self._mtime != os.path.getmtime(self._filepath):
            return True
        else:
            return False
    
    def _load(self):
        """load config."""
        logger = logging.getLogger("debug")
        try:
            logger.debug("preparing to load config.json. "
                         "path:%s" % (self._filepath, ))
            self._config = cjson.decode(open(self._filepath,"r").read()) 
            self._mtime = os.path.getmtime(self._filepath)
        except Exception, e:
            logger.error("load site config failed. e.meg:%s." % (e.message, ))
            self._config = None              
            self._mtime = None
            
    def start_timer(self, check_interval):
        """start timer."""
        if not hasattr(self, '_reload_timer'):
            self._reload_timer = ioloop.PeriodicCallback(self._check, 
                                    1000 * check_interval + random.uniform(1,5))
        self._reload_timer.start()
