import threading
import time
from threading import Thread
from logger.Logger import logger
import common.Utility

class Task:
    """Task contains a function that will be executed, a parameter list and return value"""    
    def __init__(self, name, function, paras, callback=None, callbackParas=None,group=None):
        self.paras = paras
        self.function = function
        self.group = group
        self.callback = callback
        self.callbackParas = callbackParas
        self.name = name


class  Tasks:
    def  __init__(self,  numThreads=None, tasksCallback=None, tasksCallbackParas=None,maxRunningTasks=None, timeout=None):
        """Initialize  the  thread  pool  with  numThreads  workers."""  
        self.__threads  =  []
        self.__startedThreads = []
        self.__resizeLock  =  threading.Condition(threading.Lock())
        self.__taskLock  =  threading.Condition(threading.Lock())
        self.__tasks  =  []
        self.__isJoining  =  False
        self.__numberThreads = 0
        if maxRunningTasks != None:
            self.__maxRunningTasks = maxRunningTasks
        else:
            self.__maxRunningTasks = 10
        self.tasksNum = 0
        self.tasksCallback = tasksCallback
        self.tasksCallbackParas = tasksCallbackParas
        self.tasksResult = []
        self.tasksCallbackResult = []
        self.timeout = timeout
    def appendTask(self, task):
        """ Append new tasks into tasks list."""         
        self.__tasks.append(task)
        self.tasksNum = self.tasksNum + 1
    def __startThread(self, maxRunningTasks=None):
    # start all available threads simultaneously
        
        try:
            if maxRunningTasks!=None:
                self.__maxRunningTasks = maxRunningTasks
#             print "self.__threads length is " + self.__threads.__len__().__str__()
            numRunningThread = 0
            start = time.time()
            numStartedThread = 0
            for thr in self.__threads:
                thr.daemon = True
                thr.start()
                numStartedThread = numStartedThread +1
                self.__startedThreads.append(thr)
                numRunningThread = numRunningThread + 1
                while numRunningThread >= self.__maxRunningTasks:
                    for startedThr in self.__startedThreads:
                        if startedThr.is_alive() == False:                            
                            self.__startedThreads.remove(startedThr)
                            numRunningThread = numRunningThread - 1
                    time.sleep(0.1)
                    #if the total consumed time expend the time, break
                    if self.timeout is None :
                        continue
                    if start + numStartedThread * self.timeout > time.time():
                        break
                                         
        except:
            pass
#             print "Error occurred in starting tasks"       
            
        
        try:
            self.__isJoining = True
            for thr in self.__startedThreads:
                thr.join(self.timeout)
                if thr.is_alive():
                    logger.debug("%s is time out." % str(thr))
                    try:
                        thr._Thread__stop()
                    except:
                        pass                 
                    for task in self.__tasks:                        
                        if task.name == thr.name:
                            task.callback(task.callbackParas) 
                     
            #execute call back function of each 
                     
            self.__isJoining = False
            if self.tasksCallback != None:
                self.tasksCallback(self.tasksCallbackParas)
            self.__tasks  =  []
            self.tasksNum = 0
            self.__threads = []
            self.__startedThreads = []
            self.__numberThreads = 0
            self.tasksResult = []
        except Exception, e:
            logger.error("Error occurred in running tasks" + str(e))
            common.Utility.recordException(e)

    def run(self, group=None, maxRunningTasks=None):
        """ execute all available tasks simultaneously. 
        If the number of tasks is larger than the thread number, then the threadpool will be resized """
        if self.__tasks.__len__() > self.__numberThreads:
            self.__numberThreads = self.__tasks.__len__()
        numCreatedThread = 0
        if group == None:
            while numCreatedThread < self.__numberThreads:
                self.__threads.append(threading.Thread(target=self.__tasks[numCreatedThread].function, name=self.__tasks[numCreatedThread].name, args=self.__tasks[numCreatedThread].paras))
                numCreatedThread = numCreatedThread + 1
        else:
            #execute the tasks, of which group are specified.
            for tsk in self.__tasks:
                if tsk.group == group:
                    self.__threads.append(threading.Thread(target=tsk.function,name=tsk.name, args=tsk.paras))
                    numCreatedThread = numCreatedThread + 1
        if maxRunningTasks != None:
            self.__startThread(maxRunningTasks)
        else:
            self.__startThread()
            
# just for unit testing purpose.       
class TestClass:
    def __init__(self, paras):
        self.paras = paras
        
    def testfuncion(self, *paras):
        self.paras = paras
        result1 = "aaa"
        result2 = "bbb"
        result3 = "ccc"
        result = self.paras[0], result1,result2,result3        
        tasks.tasksResult.append(result)
        time.sleep(10)
        #print "running test function, with paras is " + self.retResult
        #= result1, result2, result3
        return result1, result2, result3
    def testcallback(self, *paras):
        result1 = "ddd"
        result2 = "eee"
        result3 = "fff"
        result = self.paras[0], result1,result2,result3
        tasks.tasksCallbackResult.append(result)
    def cleanUp(self):
        print "cleaning up"

if __name__ == "__main__":
    retResult = None
    tasks = Tasks()
    testclass1 = TestClass([1,2])
    testclass2 = TestClass([2])
    testclass3 = TestClass([3])
    testclass4 = TestClass([4])    
    task1 = Task("task1", testclass1.testfuncion, testclass1.paras, testclass1.testcallback, testclass1.paras, group=1)
    task2 = Task("task2", testclass2.testfuncion, testclass2.paras, testclass2.testcallback, testclass2.paras, group=1)
    task3 = Task("task3", testclass3.testfuncion, testclass3.paras, testclass3.testcallback, testclass3.paras, group=1)
    task4 = Task("task4", testclass4.testfuncion, testclass4.paras, None, None, group=1)
    #tasks = Tasks(4, testclass1.cleanUp)
    print "aaa" + task1.name    
    tasks.appendTask(task1)
    tasks.appendTask(task2)
    tasks.appendTask(task3)
    tasks.appendTask(task4)
    #tasks.run(group=1,maxRunningTasks=2)
    tasks.run(group=1,maxRunningTasks=2)
    print tasks.tasksResult
    print tasks.tasksCallbackResult
    