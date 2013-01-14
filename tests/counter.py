# -*- coding: utf-8 -*-

import os
import pylibmc


class Counter(object):

    KEY = 'celery-troll-bridge-test-key'

    def __init__(self):
        self.mc = pylibmc.Client(["127.0.0.1"], binary=True, behaviors={"tcp_nodelay": True, "ketama": True})

    def add(self):
        try:
            return self.mc.incr(self.KEY)
        except pylibmc.NotFound:
            self.mc.set(self.KEY, 1, time=3600)
            return 1

    def read(self):
        return self.mc.get(self.KEY) or 0

    def reset(self):
        self.mc.flush_all()
        self.mc.set(self.KEY, 0, time=3600)

