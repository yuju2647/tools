#!usr/bin/env python
# coding=utf-8

import json
from handlers.base import Base
from commons.router import Route

@Route("/api/v1/str_to_list")
class String2List(Base):

    def post(self):
        text = self.get_argument("text")
        nodes = text.split("\r\n")
        nodes_json = json.dumps(nodes)
        self.finish(nodes_json)
