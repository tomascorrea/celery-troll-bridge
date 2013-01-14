# -*- coding: utf-8 -*-

import unittest

from counter import Counter

class CounterTestCase(unittest.TestCase):

    def setUp(self):
        super(CounterTestCase, self).setUp()
        self.counter = Counter()
        self.counter.reset()


    def test_add_read(self):
        self.counter.add()
        self.assertEquals(1, self.counter.read())