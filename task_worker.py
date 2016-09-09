# filename: task_worker.py
# -*- coding: utf-8 -*-
# 客户端：从服务器的任务队列中获取任务，进行计算并放入结果队列

import time, sys, Queue
from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support

# 创建从BaseManager继承的QueueManager
class QueueManager(BaseManager):
    pass

def start_cal():
    # 由于这个QueueManager只从网络上获取Queue，所以注册时只提供名字:
    QueueManager.register('get_task_queue')
    QueueManager.register('get_result_queue')
    # 连接到服务器，也就是运行task_master.py的机器:
    server_addr = '127.0.0.1'
    #print ('Connect to server %s ...' % server_addr)
    # 端口和验证码注意保持与task_master.py设置的完全一致:
    m = QueueManager(address = (server_addr, 5000), authkey = b'abc')
    # 从网络连接:
    m.connect()
    # 获取Queue的对象:
    task = m.get_task_queue()
    result = m.get_result_queue()
    # 从task队列取任务,并把结果写入result队列:
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
    # 处理结束:
    print ('worker exit.')
    
if __name__ == '__main__':
    freeze_support()
    start_cal()