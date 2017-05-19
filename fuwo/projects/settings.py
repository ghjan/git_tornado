#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author magic, create Date: 5/19/17
"""
import os
from tornado.options import define
import sys


PROJECT_ROOT = os.path.normpath(os.path.dirname(os.path.dirname(__file__)))
PROJECT_PATH = os.path.join(PROJECT_ROOT, 'projects')
sys.path.insert(1, PROJECT_PATH)
LIB_PATH = os.path.join(PROJECT_ROOT, 'libs')
sys.path.insert(1, LIB_PATH)
APP_PATH = os.path.join(PROJECT_ROOT, 'apps')
sys.path.insert(1, APP_PATH)

config = {
            'template_path': os.path.join(APP_PATH, 'farm/templates'),
            'static_path': os.path.join(APP_PATH, 'farm/static'),
            'debug': True
        }


# server run port
define('port', default=7888, help='run on the given port', type=int)

# database configure
# define('mysql_host', default='127.0.0.1', help='farm database host')
# define('mysql_database', default='farm_tornado', help='farm database name')
# define('mysql_user', default='user', help='farm database user')
# define('mysql_password', default='AzMNTOk%', help='farm database password')

