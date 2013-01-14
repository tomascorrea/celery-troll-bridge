# -*- coding: utf-8 -*-

from celery import Celery, current_task

celery = Celery()

class Config:
    CELERY_ENABLE_UTC = True
    BROKER_URL = 'amqp://guest:guest@localhost:5672//'

celery.config_from_object(Config)

#from celery_troll_bridge.task import GlobalSemaphoredTask


#@celery.task(name='test.dummy_task', base=GlobalSemaphoredTask, global_rate_limit="50/s")
@celery.task(name='tests.dummy_task')
def dummy_task(text):
    from .counter import Counter
    counter = Counter()
    print counter.add()
    #print counter.read()