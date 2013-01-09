# -*- coding: utf-8 -*-

import unittest
from celery import Celery, current_task

from .tasks import dummy_task

class GlobalSemaphoredTaskTestCase(unittest.TestCase):

    def test_dummy(self):

        for a in range(50):
            response = dummy_task.apply_async(('hello',))

