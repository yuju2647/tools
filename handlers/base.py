#!usr/bin/env python
# coding=utf-8

from commons.router import Route
from tornado.web import RequestHandler

@Route("/")
class Base(RequestHandler):

    def get(self):
        self.render("index.html")