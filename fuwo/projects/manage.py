#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author magic, create Date: 5/19/17
"""
from settings import *
from urls import Application
import tornado.options
import tornado.ioloop
from tornado.options import options
import tornado.httpserver


def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()

if __name__ == '__main__':
    print " Server is listening at 127.0.0.1:%s ... " % options.port
    main()