#!usr/bin/env python
#coding=utf-8
import sys
import logging
logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filemode='a')

reload(sys)
sys.setdefaultencoding('utf-8')

import config
import tornado.web
import tornado.ioloop
import tornado.options
import tornado.httpserver
from tornado.options import define,options
from commons import router
from handlers import *
from handlers.ui import *
from handlers.api import *


class Application(tornado.web.Application):
    def __init__(self):
        tornado.web.Application.__init__(self,handlers=router.Route.get_routes(),**config.settings)

def main():
    tornado.options.parse_command_line()
    http_server=tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    logging.info('''
                ************                          ****************
                **************** Tools {} is running********************
                ************                          ****************
            '''.format(options.port))
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    define("port", default=config.APP_PORT, type=int)
    main()