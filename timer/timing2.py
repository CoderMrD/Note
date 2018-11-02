import time
import threading
import logging
 
class NewTimer(threading.Thread):
    def __init__(self):
        super().__init__()
        self.queues = []
        self.timer = None
        self.cond = threading.Condition()
 
    def run(self):
        while True:
            # print('NewTimer',self.queues)
            self.cond.acquire()
            item = self.get()
            callback = None
            if not item:
                logging.info('NewTimer wait')
                self.cond.wait()
            elif item[0] <= time.time():
                new_item = self.pop()
                callback = new_item[1]
            else:
                logging.info('NewTimer start sys timer and wait')
                self.timer = threading.Timer(item[0]-time.time(),self.execute)
                self.timer.start()
                self.cond.wait()
            self.cond.release()
 
            if callback:
                callback(item[0])
 
    def add(self, item):
        # print('add', item)
        self.cond.acquire()
        item[0] = item[0] + time.time()
        self.queues.append(item)
        self.queues.sort(key=lambda x: x[0])
        logging.info('NewTimer add notify')
        if self.timer:
            self.timer.cancel()
            self.timer = None
        self.cond.notify()
        self.cond.release()
 
    def pop(self):
        item = None
        if len(self.queues) > 0:
            item = self.queues.pop(0)
        return item
 
    def get(self):
        item = None
        if len(self.queues) > 0:
            item = self.queues[0]
        return item
 
    def execute(self):
        logging.info('NewTimer execute notify')
        self.cond.acquire()
        self.cond.notify()
        self.cond.release()

        
if __name__ == '__main__':
    def func():
        while True:
            print(threading.active_count())
            time.sleep(1)

    f1 = threading.Thread(target=func)
    f1.start()
    logging.basicConfig(level=logging.INFO,format="%(asctime)s %(message)s", datefmt="%m/%d/%Y %H:%M:%S [%A]")

    newtimer = NewTimer()
    newtimer.start()

    def func1(*args):
        logging.info('func1 %s'%args)
        time.sleep(5)

    def func2(*args):
        logging.info('func2 %s' % args)
        time.sleep(5)
    def func3(*args):
        logging.info('func3 %s' % args)
        time.sleep(5)

    def func4(*args):
        logging.info('func4 %s' % args)
        time.sleep(5)

    def func5(*args):
        logging.info('func5 %s' % args)
        time.sleep(5)

    newtimer.add([5,func1])
    newtimer.add([4,func2])
    newtimer.add([3,func3])
    newtimer.add([2,func4])
    newtimer.add([1,func5])
    time.sleep(1)
    newtimer.add([1,func1])
    newtimer.add([2,func2])
    newtimer.add([3,func3])
    newtimer.add([4,func4])
    newtimer.add([5,func5])