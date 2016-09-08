# task_worker.py
# -*- coding: utf-8 -*-
# 客户端，从服务器的任务队列中获取任务，进行计算并放入结果队列

import time, sys, Queue
from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support


class QueueManager(BaseManager):
    pass


def start_cal():

    QueueManager.register('get_task_queue')
    QueueManager.register('get_result_queue')

    server_addr = '127.0.0.1'
    #print ('Connect to server %s ...' % server_addr)

    m = QueueManager(address = (server_addr, 5000), authkey = b'abc')
    m.connect()

    task = m.get_task_queue()
    result = m.get_result_queue()

    for i in range(1000):
        try:
            n = task.get(timeout = 1)
            print ('Run task %d * %d' % (n, n))
            r = '%d * %d = %d' % (n, n, n * n)
            #time.sleep(1)
            result.put(r)
        except Queue.Empty:
            print ('task queue is empty.')
    m.close()
    print ('worker exit.')

if __name__ == '__main__':
    freeze_support()
    start_cal()