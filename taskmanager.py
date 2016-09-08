# taskmanager.py

import random, Queue
from multiprocessing.managers import BaseManager

# The queue that sends tasks:
task_queue = Queue.Queue()
# The queue that receives results:
result_queue = Queue.Queue()

# QueueManager inherits BaseManager:
class QueueManager(BaseManager):
    pass

# Register both queues on the web, argument callable related to Queue object
QueueManager.register('get_task_queue', callable = lambda: task_queue)
QueueManager.register('get_result_queue', callable = lambda: result_queue)
# Bind Port 5000, set password 'abc':
manager = QueueManager(address = ('', 5000), authkey = 'abc')
# Start Queue:
#server = manager.get_server()
#server.serve_forever()
manager.start()
# Get Queue objects accessed through network:
task = manager.get_task_queue()
result = manager.get_result.queue()
# Put some tasks in
for i in range(10):
    n = random.randint(0, 10000)
    print('Put task %d...' % n)
    task.put(n)
# Get results from result queue
print 'Try get results...'
for i in range(10):
    r = result.get(timeout = 10)
    print('Result: %s' % r)
# Shut down
manager.shutdown()
print 'master exit.'