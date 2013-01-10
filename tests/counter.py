# -*- coding: utf-8 -*-

import os
import pickle

TMP_DATA_PATH = os.path.join(os.path.dirname(__file__), 'tmp_data')


class Counter(object):

    def __init__(self):
        self.file = open("%s/counter.pic" % TMP_DATA_PATH, 'w')


    def add(self):
        pickle.dump(self.read() + 1, self.file)


    def read(self):
        return pickle.load(self.file)
