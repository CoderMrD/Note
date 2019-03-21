#### 根据需要判断是否需要创建类，是否执行__init__
class ConfigReader:
    configReader = None

    @staticmethod
    def getConfigReader(cfgfile=None, mkeyfile=None):
        if cfgfile and mkeyfile:
            ConfigReader.configReader = ConfigReader(cfgfile, mkeyfile)
        else:
            ConfigReader.configReader = ConfigReader()
        return ConfigReader.configReader
    
    def __init__(self):
        print "ok"
    
    def eat(self):
    print "eat"

'self表示实例，完整的执行是ConfigReader.eat(con)'
con = ConfigReader()
con.eat()

 "单下划线" 开始的成员变量叫做保护变量，意思是只有类对象(即实例)和子类对象(即继承自基类的类的实例)自己能访问到这些变量；此变量不能通过from XXX import xxx 导入，"双下划线" 开始的是私有成员，意思是只有类本身访问，连子类对象也不能访问到这个数据。(如下列所示)
     以单下划线开头（_foo）的代表不能直接访问的类属性，需通过类提供的接口进行访问，不能用“from xxx import *”而导入；以双下划线开头的（__foo）代表类的私有成员；以双下划线开头和结尾的（__foo__）代表python里特殊方法专用的标识，如 __init__（）代表类的构造函数。目的就是以防子类意外重写基类的方法或者属性,私有变量和保护变量的作用域被设定在本模块内，虽然可以访问但是不建议访问。

命名：类，大驼峰，方法：小驼峰

分页：
s = "0123456789"
pageSize = 3
pageCount = (len(s)-1)/pageSize + 1
if len(s) > pageSize:
    for currentPage in range(1,pageCount+1):
        begin = (currentPage-1)*pageSize
        end = currentPage * pageSize
        print s[begin:end]
        
pip和python绑定，使用python -m pip xxx
