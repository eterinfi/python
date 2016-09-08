import time, threading

def loop():
    print '%s is running...' % threading.current_thread().name
    n = 0
    while n < 5:
        n += 1
        print '%s >>> %s' % (threading.current_thread().name, n)
        time.sleep(1)
    print '%s ended.' % threading.current_thread().name

print '%s is running...' % threading.current_thread().name
t = threading.Thread(target = loop, name = 'LoopThread')
t.start()
t.join()
print '%s ended.' % threading.current_thread().name