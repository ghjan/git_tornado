#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author magic, create Date: 5/19/17
"""


import tornado.web
from settings import config
from farm import urls as fm_urls


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", fm_urls.HomeHandler),
            (r"/other", fm_urls.OtherHandler),
            (r"/task", fm_urls.AsyncTaskHandler),
            (r"/future", fm_urls.FutureHandler),
            (r"/future/response", fm_urls.FutureResponseHandler)
        ]

        # import pdb        # use pdb to debug is usefully
        # pdb.set_trace()

        super(Application, self).__init__(handlers, **config)

        # database connect and create