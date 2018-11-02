import threading
import time
 
class Timer():
 
    def __init__(self):
        self.queues = []
        self.timer = None
        self.last_time = time.time()
 
    def start(self):
        item = self.get()
        if item:
            self.timer = threading.Timer(item[0],self.execute)
            self.timer.start()
 
    def add(self,item):
        print('add',item)
        self.flush_time()
        self.queues.append(item)
        self.queues.sort(key=lambda x:x[0])
 
        if self.timer:
            self.timer.cancel()
            self.timer = None
        self.start()
 
    def get(self):
        item = None
        if len(self.queues) > 0:
            item = self.queues[0]
        return item
 
    def pop(self):
        item = None
        if len(self.queues) > 0:
            item = self.queues.pop(0)
        return item
 
    def flush_time(self):
        curr_time = time.time()
        for i in self.queues:
            i[0] = i[0] - (curr_time - self.last_time)
        self.last_time = curr_time
 
    def execute(self):
        # if self.timer:
        #     self.timer.cancel()
        #     self.timer = None
        item = self.pop()
        self.flush_time()
        if item:
            callback = item[1]
            args = item[0]
            callback(args)
        self.start()

if __name__ == '__main__':
    def func():
        while True:
            print(threading.active_count())
            time.sleep(1)
    
    f1 = threading.Thread(target=func)
    f1.start()
    
    import logging
    logging.basicConfig(level=logging.INFO,format="%(asctime)s %(message)s", datefmt="%m/%d/%Y %H:%M:%S [%A]")
    def func1(*args):
        logging.info('func1 %s'%args)
        # time.sleep(5)
    
    def func2(*args):
        logging.info('func2 %s' % args)
        # time.sleep(5)
    def func3(*args):
        logging.info('func3 %s' % args)
        # time.sleep(5)
    
    def func4(*args):
        logging.info('func4 %s' % args)
        # time.sleep(5)
    
    def func5(*args):
        logging.info('func5 %s' % args)
        # time.sleep(5)
    
    
    t1 = Timer()
    logging.info('start')
    t1.add([5,func1])
    time.sleep(0.5)
    t1.add([4,func2])
    time.sleep(0.5)
    t1.add([3,func3])
    time.sleep(0.5)
    t1.add([2,func4])
    time.sleep(0.5)
    t1.add([1,func5])
    time.sleep(5)
    t1.add([1,func1])
    t1.add([2,func2])
    t1.add([3,func3])
    t1.add([4,func4])
    t1.add([5,func5])
    print t1.queues