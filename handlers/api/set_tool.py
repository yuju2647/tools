# coding=utf-8

import json
from handlers.base import Base
from commons.router import Route


@Route("/api/v1/set_tools")
class SetTool(Base):
    @classmethod
    def to_set(cls, text):
        nodes = text.split("\r\n")
        nodes = filter(lambda node: node, nodes)
        nodes = [node.strip() for node in nodes]
        return set(nodes)

    def post(self):
        text1 = self.get_argument("set1")
        text2 = self.get_argument("set2")
        sign = self.get_argument("sign")
        wrapper = self.get_argument("wrapper", False)
        set1 = self.to_set(text1)
        set2 = self.to_set(text2)
        if sign == "&":
            result = list(set1 & set2)
        elif sign == "|":
            result = list(set1 | set2)
        elif sign == "-":
            result = list(set1 - set2)
        if not wrapper:
            self.finish(",".join(result))
            return
        self.finish(json.dumps(result, ensure_ascii=False))