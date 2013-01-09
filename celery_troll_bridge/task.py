# -*- coding: utf-8 -*-

from celery import Task
from celery import current_app

@current_app.task()
def troll(real_task, args, kwargs):
    kwargs['real'] = True
    real_task.apply_async(args, kwargs)


class GlobalSemaphoredTask(Task):
    """
    All task that extends this task implements a global - all works share the same rate_limit
    """

    abstract = True

    def __init__(self, *args, **kwargs):

        super(GlobalSemaphoredTask, self).__init__(*args, **kwargs)

        current_app.control.rate_limit(troll.name, self.global_rate_limit)


    def __call__(self, *args, **kwargs):

        if 'real' in kwargs:
            real = kwargs.pop('real')
            super(GlobalSemaphoredTask, self).__call__(*args, **kwargs)
        else:
            troll.apply_async((self,args, kwargs), queue='troll',)



