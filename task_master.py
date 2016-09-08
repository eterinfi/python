# task_master.py
# -*- coding: utf-8 -*-
# server，往任务队列中放任务后， 从结果队列中获取结果


import random, time, Queue
from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support

#发送任务的队列
task_queue = Queue.Queue()
#接收结果的队列
result_queue = Queue.Queue()

class QueueManager(BaseManager):
    pass

def return_task_queue():
    global task_queue
    return task_queue

def return_result_queue():
    global result_queue
    return result_queue



#注册到网络
def start_server():
    QueueManager.register('get_task_queue', callable = return_task_queue)
    QueueManager.register('get_result_queue', callable = return_result_queue)
    manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'abc')

    manager.start()

    task = manager.get_task_queue()
    result = manager.get_result_queue()

    for i in range(1000):
        n = random.randint(0, 10000)
        print ('Put task %d...' % n)
        task.put(n)

    #print ('Try get results...')
    for i in range(1000):
        r = result.get(timeout = 5)
        print ('Result: %s' % r)

    manager.shutdown()
    print ('master exit.')


if __name__ == '__main__':
    freeze_support()
    start_server()