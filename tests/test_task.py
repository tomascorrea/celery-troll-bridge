# -*- coding: utf-8 -*-

import unittest
import subprocess
import time

from .tasks import dummy_task
from counter import Counter

class GlobalSemaphoredTaskTestCase(unittest.TestCase):

    def setUp(self):
        super(GlobalSemaphoredTaskTestCase, self).setUp()
        self.counter = Counter()
        self.counter.reset()
        self.process_defaults = []
        self.process_trolls = []

    def tearDown(self):

        for process in self.process_defaults:
            process.kill()

        for process in self.process_trolls:
            process.kill()

    def test_dummy(self):

        self.process_defaults.append(subprocess.Popen(['celery', 'worker', '--app', 'tests.tasks', '-l', 'info', '-Q', 'celery']))

        self.process_trolls.append(subprocess.Popen(['celery', 'worker', '--app', 'tests.tasks', '-l', 'info', '-Q', 'troll']))


        for a in range(50):
            response = dummy_task.apply_async(('hello',))

        # The global max rate is 50/s, for 50 task we need to wait for a second

        for a in range(20):
            time.sleep(0.1)
            if self.counter.read() > 49:
                break

        self.assertEqual(50, self.counter.read())

















