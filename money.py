import os
import time
import threading
# adb kill-server
class Money():
    def __init__(self,device_x = 1920, device_y = 1080, device_name = None):
        self.device_x = device_x
        self.device_y = device_y
        self.device_name = device_name
        
    def run(self):
        while True:
            os.system('ld -s {} input tap {} {}'.format(self.device_name, 1389/1920*self.device_x, 840/1080*self.device_y))
            time.sleep(1)
            os.system('ld -s {} input tap {} {}'.format(self.device_name, 1556/1920*self.device_x, 956/1080*self.device_y))
    
if __name__ == "__main__":
    test1 = Money(device_x=960,device_y=540, device_name="1")
    test0 = Money(device_x=960,device_y=540, device_name="0")
    t1 = threading.Thread(target=test0.run,name="number1")
    t2 = threading.Thread(target=test1.run,name="number2")
    t1.start()
    t2.start()