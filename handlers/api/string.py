# coding=utf-8

import json
from handlers.base import Base
from commons.router import Route


@Route("/api/v1/str2list")
class String2List(Base):

    def post(self):
        text = self.get_argument("text")
        wrapper = self.get_argument("wrapper", False)
        nodes = text.split("\r\n")
        nodes = filter(lambda node: node, nodes)
        nodes = [node.strip() for node in nodes]
        if not wrapper:
            self.finish(",".join(nodes))
            return
        nodes_json = json.dumps(nodes, ensure_ascii=False)
        self.finish(nodes_json)


@Route("/api/v1/str_trim")
class StringTrim(Base):

    def post(self):
        text = self.get_argument("text")
        wrapper = self.get_argument("wrapper", False)
        nodes = text.split("\r\n")
        nodes = filter(lambda node: node, nodes)
        nodes = [node.strip() for node in nodes]
        if not wrapper:
            self.finish(",".join(nodes))
            return
        nodes_json = json.dumps(nodes, ensure_ascii=False)
        self.finish(nodes_json)


@Route("/api/v1/sqlResult2list")
class sqlResult2list(Base):

    def post(self):
        text = self.get_argument("text")
        wrapper = self.get_argument("wrapper", False)
        text = text.replace("|", "")
        text = text.replace("+", "")
        text = text.replace("---", "")
        text.strip()
        nodes = text.split("\r\n")
        clean_nodes = []
        for node in nodes:
            node = node.strip()
            if node != '' and wrapper:
                clean_nodes.append(node)
            elif node != '' and not wrapper:
                node += "<br/>"
                clean_nodes.append(node)
        if not wrapper:
            self.finish("".join(clean_nodes))
            return
        nodes_json = json.dumps(clean_nodes, ensure_ascii=False)
        self.finish(nodes_json)
