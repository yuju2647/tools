# coding=utf-8

import json
import time
from handlers.base import Base
from commons.router import Route


@Route("/api/v1/time2stamp")
class Time2Stamp(Base):

    def post(self):
        date = self.get_argument("date")
        ms = self.get_argument("ms")
        time_str = date[0:4] + "-" + date[4:6] + "-" + date[6:8] + " " + ms
        timestamp = int(time.mktime(time.strptime(time_str, '%Y-%m-%d %H:%M:%S')))
        self.finish(json.dumps(timestamp))