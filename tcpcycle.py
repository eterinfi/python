from multiprocessing import Pool
import os
def task(name):
    print 'Running task %s...' % name
    os.system("python tcp_client.py")

i = 0
while True:
    i+=1
    task(str(i))
