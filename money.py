import os
import time

class Money():
	def __init__(self,device_x = 1920, device_y = 1080, device_name = None):
		self.device_x = device_x
		self.device_y = device_y
		self.device_name = device_name
		
	def run(self):
		os.system('adb -s {} shell input tap {} {}'.format(self.device_name, 1389/1980*self.device_x, 840/1080*self.device_y))
		time.sleep(0.1)
		os.system('adb -s {} shell input tap {} {}'.format(self.device_name, 1556/1980*self.device_x, 956/1080*self.device_y))
	
if __name__ == "__main__":
	# 输入设备分辨率
	# emulator-5554
	# emulator-5556
	# 127.0.0.1:5555
	# 127.0.0.1:5557
	#test0 = Money(device_x=1280,device_y=720, device_name="emulator-5554")
	test1 = Money(device_x=1280,device_y=720, device_name="emulator-5556")
	#test1 = Money(device_x=1280,device_y=720, device_name="127.0.0.1:5557")
	
	while True:
		#test0.run()
		test1.run()