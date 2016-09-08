# -*- coding : utf-8 -*-
import os, time, subprocess
from multiprocessing import Process

def master():
	r = subprocess.call(['python', 'task_master.py'])
	if r != 0: print('Task Master ERROR!')

def client():
	r = subprocess.call(['python', 'task_worker.py'])
	if r != 0: print('Task Client ERROR!')

if __name__=='__main__':
	tesp = 0
	for i in range(10):
	    start=time.time()
	    ps=Process(target=master,args=())
	    pc=Process(target=client,args=())
	    ps.start()
	    pc.start()
	    ps.join()
	    pc.join()
	    end=time.time()
	    te=end-start
	    tesp+=te
	print 'Average Time elapsed: %.2fs' % (tesp/10)
