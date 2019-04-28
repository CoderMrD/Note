有需要细看：建议九
待看
## 第一章 引论
### 建议一：pythonic风格的概念

1. 可读性， 接近伪代码的风格。【用reversed()代替[::-1]来进行逆序列表】
2. 具体python特征的代码。
    ```python
    # 交换
    a,b = b,a
    # 遍历
    for i in l :
    # 安全关闭
    with open(path, "r") as f:
    ```
3. 标准库
    ```python
    # 格式化输出,提升可读性
    str.format()
    print '{greet} from {language}'.format(greet = 'Hello word', language = 'python')
    ```
4. pythonic风格的框架
    - Flask
    - gevent
    - requests
### 建议二： 编写pythonic风格的代码
- PEP8
    ```python
    pip install -U pep8
    # 检测代码是否符合pep8
    pep8 --first optparse.py
    # 更加细致的显示pep8的每一个错误和警告对应的代码
    pep8 --show-source --show-pep8 testsuite/E40.py
    ```
### 建议三： 理解python与C语言的不同之处
### 建议四： 在代码中适当添加注释
- 行注释，块注释，文档注释(docstring)
1. 注释和代码隔开一定距离
    ```python
    x = x + 1        # increace x by 1
    ```
2. 给外部可访问的函数和方法（无论是否简单）添加文档注释。注释要清楚地描述方法的功能，并对参数、返回值已经可能发生的异常进行说明。使外部调用的人员仅仅看docstring就能使用，较为复杂的内部也需要注释
    ```python
    def FuncName(parameter1 , parameter2):
        """Describe what this function does.
            #such as "Find whether the special string is in ths queue or not"
            Args:
                parameter1: parameter type, what is this parameter used for.
                # such as strqueue:string,string queue list for search
                parameter2: parameter type, what is this parameter userd for.
                # such as str: string,string to find
        Returns:
            return type, return value.
            # such as boolean,special string    found return Ture,else return False
        """
        function body
        ...
        ...
    ```
3. 推荐在头文件中包含copyright申明、模块描述等，如有必要，可以考虑加入作者信息以及变更记录
### 建议五： 通过适当添加空行使代码布局更为优雅、合理
1. 一组代码表达完一个完整的思路后，应该使用空白行进行间隔。如没个函数之间，导入声明，变量赋值等。推荐在函数定义或者类定义之间空两行，在类定义与第一个方法之间，或者需要语义分割的地方空一行。
2. 尽量保持上下文语义的以理解性，如当一个函数需要调用另一个函数的时候，尽量将他们放在一起，最好调用者在上，被调用者在下。
3. 避免过长代码行，不要超过80个字符。
4. 空格的使用能够在需要强调的时候警示读者，而在具有紧密关系的时候不要使用空格。
    - 逗号，分号前不要使用空格
### 建议六： 编写函数的四个原则
1. 不要过长。不用拉动滚动条就能查看，循环判断语句不要过深，尽量控制在三层以内。
2. 参数设计不应过多
3. 考虑向下兼容。可以加入默认参数，传入则使用，不传入使用默认。
4. 一个函数只做一件事，尽量保证函数语句粒度的一致性。
- 其余好习惯,不要在函数中定义可变对象（列表list、集合set、字典dict）为默认值，使用异常替换错误，以便通过单元测试。

`
1、构造操作:  这类操作主要是基于一些已知信息，产生这个类的实例对象。类似银行进行开通账户  
 
2、解析操作：这类操作是获取对象的一些有用信息，其结果反应了对象的一些特征，但返回的不是对象本身。类似银行查询账户余额   

3、变化操作 ：这类操作是修改对象内部的信息和状态。比如一个银行账户进行转账操作

如果一个类型，具只具有1和2两种操作，也就说只具有构造和解析操作，那么这个类型就是不可变类型，这个类型的对象就是不可变对象
如果一个类型，具有1、2、3三种操作，这个类型就是可变类型，这个类型的对象就是可变对象。
`
### 建议七：将常量集中在一个文件,易于维护
python没有提供定义常量的直接方式（如C中的define）。

python中一般使用常量方式：
1. 通过命名风格，如常量名所有字母大写，用下划线连接各个单词。（只是约定俗成的风格）
2. 通过自动以类实现。要求符合“命名全部大写”和“值一旦绑定便不可以再修改”这两个条件。
```python
class _const:
    class ConstError(TypeError): pass
    class ConstCaseError(ConstError): pass

    def __setattr__(self, name, value):
        if self.__dict__.has_key(name):
            raise self.ConstError, "can't change const.%s" % name
        if not name.isupper():
            raise self.ConstCaseError, 'const name "%s" is not all uppercase' % name
        self.__dict__[name] = value

import sys
sys.modules[__name__]=_const()
```
如果上面的代码对应的模块名为const, 使用的时候只需要import const，便可以直接定常量了
```python
import const
const.COMPANY = "IBM"
```
采用第二种方式可以把存放敞亮的文件命名为constant.py，并在其中定义一系列的常量。

## 第二章 编程惯用法
### 建议8：利用assert语句来发现问题
- 基本语法
```python
# 如果expression1的值为False时会引发AssertionError,expression2用来传递异常信息
assert expression1 ["," expression2]
```
- 禁用断言可以在运行脚本的时候加上-O标志。

断言是被设计用来捕获用户所定义的约束的，而不是用来捕获程序本身错误的。
1. 不要滥用。断言应该使用在正常逻辑不可达到的地方或者正常情况下总为真的场合。
2. 如果Python本身的异常能够处理就不要再使用断言。
3. 不要使用断言来检查用户的输入。
4. 在函数调用后，当需要确认返回值是否合理时使用断言。
5. 当条件是业务逻辑继续下去的先决条件时可以使用断言（如a和b必须相当业务逻辑才能继续，可以使用断言来判断二者关系）
### 建议9：数据交换值的时候不推荐使用中间变量
这种方式性能更好，因为python表达式的计算顺序是从左到右，但碰到表达式赋值的表达式右边的操作数先于左边的操作数计算
x,y = y,x在内存中执行顺序如下：

- dis，分析函数字节码。eg：dis.dis(add)
```
 2            0 LOAD_FAST                0 (a)
              2 LOAD_FAST                1 (b)
              4 BINARY_ADD
              6 RETURN_VALUE
# 第一列数字代表源代码中的行数，第二列数字是字节码的索引，第三列是指令本身对应的人可读的名字，第四列是指令的参数，第五列是计算后的实际参数
```

### 建议10：充分利用Lazy evaluation（延迟计算、惰性计算）的特性
1）避免不必要的计算，带来性能上的提升。如if x and y，如果x为false，则y就不再计算，变成中应充分利用这个特性。
2）节省空间，使得无限循环的数据结构成为可能。Python中最经典使用的例子就是生成器表达式了，每次许要计算的时候才通过yield产生所需要的元素。如斐波那契数列
```python
def fib():
	a, b = 0, 1
	while True:
		yield a
		a, b = b, a+b
from itertools import islice
print list(islice(fib(),5))
[0,1,2,3]
```

###  建议11：理解枚举替代实现的缺陷
- 枚举型是一个集合，集合中的元素(枚举成员)是一些命名的整型常量
1）使用类属性
```python
class Season:
    Spring, Summer, Autumn, Winter=range(4)
```
2) 借助函数

缺陷：
- 允许枚举值重复
- 支持无意义的操作，如对季节的加减

python2.7以后可以使用第三方模块flufl.enum,包含两种枚举类型：一种是Enum，只要保证枚举值唯一即可，另一种是IntEnum，其枚举值为int型。
```python
from flufl.enum imort Enum
class Seasons(Enum):        # 继承自Enum定义枚举
    Spring = "Spring"
    Summer = 2
    Autumn = 3
    Winner = 4
Seasons = Enum('Seasons','Spring Sumter Autumn Winter')
```
可以使用__members__属性对枚举名称进行遍历，也可以直接使用value属性获取枚举元素的值，不支持元素比较（无意义的操作）
python3.4中加入了枚举Enum

### 建议12：不推荐使用type来进行类型检查
按照python理念，充分利用变量的动态性特征，不推荐类型检查。
不可以进行类型检查，而在出错的时候通过抛出异常来进行处理。
一定要使用的话可以用types
```python
import types
if type(a) is types.ListType:
```
缺陷：
1)继承自int基类的类，不被type认为是int类型
2)python2.7中，古典类(不由任意内置类型派生出的类)的实例返回的都是<type'instance'>

### 建议13：尽量转换为浮点类型后再做除法
python当除法运算中两个操作数都为整数的时候，其返回值也是整数，运算结果将直接截断（非四舍五入）
如果对计算精度要求比较高，可以使用Decimal来进行处理或者将浮点数尽量扩大为整数，计算完毕后再转换回去。

### 建议14：警惕eval()安全漏洞
eval()将字符串str当成有效的表达式来求值并返回计算结果。
eval(expression[, globals[, locals]])
可能会被黑客输入命令直接处理。

### 建议15：使用enumerate()获取序列迭代的索引和值
字典除外，字典适合用for key, value in dict.iteritems()

### 建议16：分清==与is
==是判断值，is是判断id

### 建议17：考虑兼容性，尽可能使用Unicode（限于python2）
python2 Unicode(字符串加上u)对应于python3 str
python2 str 对应于python3 byte
utf8在windows系统中被映射为GBK编码，所以当控制台上直接显示utf8时，两种编码不兼容，以UTF8形式表示的编码在GBK编码中被解释为其他的符号而产生乱码。要解决乱码问题可以使用Unicode作为中间介质来完成转换。首先对读入的字符用UTF-8解码（decode），然后用GBK进行编码。如str.decode("utf-8").encode("gbk")
python中默认编码是ASCII，可以在首行对指定源文件进行编码声明
```python
# -*- coding: <encoding name> -*-
```
某些情况下可能会出现异常，如'gbk' codec can't encode character u'\uufeff' in position 0;
因为某些软件在保存UFT8编码时，会在文件最开始的地方插入不可见的字符BOM（0xEF 0xBB 0xBF）,这些不可见字符无法被正确的解析，可以用codecs模块处理
import codecs
content[:3] == codecs.BOM_UTF8
content = content[3:]
content.decode("utf-8")

### 建议18：构建合理的包层次来管理module
简单地说包就是目录，除了包含模块(python文件)外，还包含一个__init__.py
Package/ __init__.py
    Module1.py
    Module2.py
    subpackage/__init__.py
        Module1.py
        Module2.py
包中的模块可以通过 . 访问符进行访问，即包名.模块名
__init__ 主要作用是区分开普通目录和包，其次可以声明模块级别的import语句从而使其变成包级别可见
如上目录，__init__为空，导入Module1中的Test类则需要from Package.Module1 import Test,
如果在__init__中写入from Module1 import Test,则外部再导入的时候就可以直接from Package import Test
__init__.py还能在该文件中定义__all__ 变量，控制需要导入的子包和模块，如__all__ = ['Module1', 'Module2', 'Subpackage']
包的便利：
1. 合理组织代码，便于维护和使用（关系密切的模块组成一个包）
2. 能够有效地避免名称空间冲突

## 第三章 基础语法
### 建议19：有节制的使用from...import..语句
- 一般尽量优先使用import a形式，如访问B可以使用a.B的形式
- 有节制的使用from a import B ，可以直接访问B
- 尽量避免使用from a import *，这样会污染命名空间

##### python的import机制
Python初始化环境会预先加载一批内建模块到内存中，这些模块相关信息存放在sys.modules（一个字典）中。
加载一个模块的时候解析器要做以下动作：
1. 在sys.modules中搜索查看是否已经存在，存在则导入到当前局部命名空间
2. 找不到则为导入的模块创建一个字典对象，并将信息插入sys.modules中
3. 加载前确认是否需要对模块中的文件进行编译，如果需要则先编译
4. 执行动态加载，当前模块的命名空间中执行编译后的字节码，并将所有的对象放入模块对应的字典中
警惕循环嵌套导入的问题，可以直接使用import语句，不使用from

### 建议20：优先使用absolute import来导入模块
pass

### 建议21：i+=1不等于++i
python会将++i操作解释为+(+i)，  其中+表示正数符号

### 建议22：使用with来自动关闭资源
python上下文管理器，即在对象中定义__enter__()和__exit__方法

### 建议23：使用else简化循环(异常处理)
```python
# 如果for循环中的内容一次都没有执行，那么会执行一次else中的内容
for xxx:
    xxx
else:
    xxx
```
```python
# 如果try中的内容没有被执行，那么会执行一次else中的内容，而finally则是无论上面的是否执行，都会执行finally中的内容
try:
    xxx
except EXception as e:
    xxx
else:
    xxx
finally:
    xxx
```

### 建议24：异常处理的几点原则
try，except，finally，else等可以灵活组合
- 注意异常的粒度，不要过大
- 谨慎使用单独的except捕获所有异常， 比如Exception(常规错误的基类)或者StandardError(所有的内建标准异常的基类)
- 注意捕获异常的顺序，在合适的层次处理异常。
用户也可以继承自建异常构建自己的异常类。

### 建议25：避免finally中可能出现的陷阱
- 如果try中出现了异常，但是在except中没有被捕获，那么这个异常会被临时保存起来，当finally中执行完毕的时候，临时保存的异常会被再次抛出，但是如果finally语句中产生了新的异常或者执行了return或者break语句的时候，临时保存的异常会被丢失，从而导致异常屏蔽。
- 由于finally是必须会执行的语句，如果执行try中的语句时，发现return语句，那么会先执行finally中的语句之后再执行try中的return，但是如果finally中也有return语句，那么会直接执行return中的语句，而不执行try中的语句，所以并不建议在finally中执行return语句

### 建议26：深入理解None，正确判断对象是否为空
所有赋值为None的变量都相等，None与任何其他非None的对象比较结果都为False，包过空字符串，0等等。

python内建对象都有一个_nonzero_()方法，对于自身对象进行空置检测，返回0/1或True/False，如果一个对象中没有定义该方法，那么会调用__len__()方法来判断，如果都没有定义，那么该类的实例用if判断的结果都为True。

### 建议27：连接字符日优先用join，而不是+
Python中的字符串是不可变对象，一旦创建不能改变，这个特性直接影响到Python中字符串连接的效率
```python
''.join('a','b')
```
使用join方法效率要高于+操作符，特别是字符串规模较大的时候(连接数为100000时，时间差上百倍)。
原理：使用+的时候，由于字符串不可变，每加一次就会在内存中申请一块新的内存空间，将上一次的操作结果和本次操作的右操作数复制到新的内存空间，因此，N个字符串相连会产生N-1个中间结果，没产生一个申请一次内存，影响了效率。
而join()方法会先计算需要申请的总的内存空间，然后一次性将所需内存并将字符串序列中的每一个元素复制到内存中去，所以join的时间复杂度为O(n)

### 建议28：格式化字符尽量使用.format
1. 更灵活
2. 方便作为参数传递
```python
# 使用位置
'The number is {0}'.format(123)
# 使用名称
'The number is {num}'.format(num=123)
```

### 建议29：区别可变对象和不可变对象
不可变对象：数值型(int,float),字符串，元组
可变对象：list，dict，set
- 字符串为不可变对象，任何对字符串某个字符的修改都会抛出异常
修改某个字符可以先转换成列表，修改后再用join拼接起来
```python
a = "test"
l = list(a)
l[2]="t"
"".join(l)
```
- 警惕可变对象作为默认参数传递，对可变对象的更改会直接影响到原对象，最好的方法是传入None作为默认参数，在创建对象的时候动态生成列表
```python
def __init__(self,name,course=None):
    self.name=name
    if course is None:course=[]
    self.course=course
```
- 切片相当于浅拷贝，只复制值，所以切片操作不会影响原对象

### 建议30：[],(),{}一致的容器初始化形式
```python
#列表解析,迭代iterable中每一个元素，当条件满足的时候根据表达式expr计算的内容生成一个新的元素放入新的列表中，条件表达式不是必须的，expr甚至可以是函数
[expr for iter_item in iterable if cond_expr]
# eg:获取1到10中大于4的数的平方
L = [ i**2 for i in range(1,11) if i >= 4 ]
```
- 列表解析更加直观，代码更简洁
- 效率更高
- 元祖，集合，字典等都有解析
```python
# 字典解析
{expr1,expr2 for iter_item in iterable if cond_expr}
```

### 建议31：函数传参既不是传值也不是传引用
总结：传的是对象，或者说传对象的引用。将整个对象传入，对可变对象的修改在函数外部以及内部都可见，调用者和被调用者之间共享这个对象，而对于不可变对象，由于不能真正的修改，所以修改往往通过生成一鞥新对象然后来赋值实现。(如果是重新赋值，则会改变可变对象的id，如果是修改，则不会改变id)

### 建议32：警惕默认参数潜在的问题
类似于建议29，可变对象作为默认参数时建议使用None，然后函数内再判断None后再赋值于空列表。

### 建议33：慎用变长参数
*args,**kwargs
1. 使用过于灵活。在混合普通参数或者默认参数的情况下，变长参数意味着这鞥函数的签名不够清晰，存在多种调用方式，调用者需要花费过多时间研究这个方法如何调用。
2. 如果一个函数的参数列表很长，虽然可以通过变长参数简化函数定义，但通常意味着这个函数有更好的实现方式，应该被重构。
3. 适合在以下情况使用
- 为函数添加一个装饰器
- 如果参数的数目不确定，可以考虑变长参数(比如读取一些配置文件)
- 用来实现函数的多态或者继承情况下子类需要调用父类某些方法的时候


### 建议34：深入理解str()和repr()
二者都可以将python中的对象转换成字符串。
总结：
1) 二者目标不同：str()主要面对用户，目的是可读性，而repr()是面对Python解释器或者开发人员，目的是准确性，其返回值表示Python解释器内部的含义，常作为编程人员debug用途
2) 在解释器中直接输入对象时默认调用repr()，而print(object)则调用str()
3) repr()返回值**一般**可以用eval()来还原对象
4) 这两个方法分别调用内建的__str__()和__repr__()方法，一般来说类中都应该定义__repr__()方法。而__str__()方法则为可选，当可读性比准确性更重要的时候应考虑定义__str__()方法，则默认使用__repr__()方法的结果来返回对象的字符串表达式。

### 建议35：分清staticmethod和classmethod的使用场景
两个方法都依赖于装饰器实现。
类方法在调用的时候没有显示声明cls(类本身,self实例本身)，但实际上类本身是作为隐含参数传入的。
- 类方法是将类本身作为对象操作，适用于逻辑上采用类本身作为对象来调用更为合理。
- 静态方法是类中的函数，不需要实例，逻辑上属于类，但是和类本身没有关系，就是在静态方法中不会设计到类中的属性和方法的操作。

# 第四章：库
### 建议36：掌握字符串的基本用法
python遇到为闭合的小括号时会自动将多行代码拼接为一行和把相邻的两个字符串拼接在一起，这种方式更加符合用户思维习惯，如
```python
s = ('SELECT * '
    'FROM atable '
    'WHERE afield="value"'
)
print(s)
# 输出： 'SELECT * FROM atable WHERE afield="value"'
```
python2中要注意判断字符串是str还是unicode。
判断一个变量s是不是字符串应使用isinstance(s,basestring)。
basestring是str和unicode的基类。
is*()形式的函数，进行判断是否是数字、字母等。
- 查找和替换
count(),find(),index(),rfind等方法都可以接受start，end参数，可以优化性能。
判断是否包含子串的判定推荐使用in和not in操作符
待看

### 建议37：按需选择sort()和sorted()
待看
### 建议38：使用copy模块深拷贝对象
待看
### 建议39：使用counter进行计数统计
待看
### 建议40：深入掌握ConfigParser
待看
### 建议41：使用argparse处理命令行参数
待看
### 建议42：使用pandas处理大型CSV文件
暂时不看
### 建议43：使用ElementTree解析XML
暂时不看
### 建议44：理解模块pickle优劣
序列化模块
待看
### 建议45：序列化操作--JSON
json在序列化datetime的时候会抛出TypeError异常，因为json模块不支持datetime的序列化，因此需要对json本身的JSONEncoder进行扩展，多种方法可以实现。
json模块提供了编码(JSONEncoder)和解码类(JSONDecoder)，以便用户对其魔人不支持的序列化类型进行扩展
```python
import datetime
from time import mktime
try: import simplejson as json
except ImportError: import json

class DateTimeEncoder(json.JSONEncoder):  # 对JSONEncoder进行扩展
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        return json.JSONEncoder.default(self, obj)

d = datetime.datetime.now()
print(json.dumps(d,cls=DateTimeEncoder)) # 使用cls指定编码器名称

```
python中的json模块性能比pickle与cPickle稍逊，如果对序列化性能要求非常高的场景，可以选择cPick模块。

### 建议46：使用traceback获取栈信息
traceback可以输出完整的栈信息，包括调用顺序，异常发生的语句、错误类型等。
待看
### 建议47：使用logging记录日志信息
待看
关于logging的使用，有几点建议
1) 尽量为logging取一个名字而不是默认，这样当在不同模块中使用的时候，其他模块只需要使用以下代码就能方便地使用同一个logger，因为他本质上符合单例模式。
```python
import logging
logging.basicConig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
```
### 建议48：使用threading模块编写多线程程序
GIL存在于python解释器中，用来确保当前只有一个线程被执行,当一个线程获得GIL后，这个线程将被执行，退出时释放GIL，由下一个获得GIL的线程执行,这导致了纯Python代码使用多线程并不能提高运行速率，只是在遇到需要等待操作的时候，使用多线程会提升效率。
python多线程有两个模块，threading和thread，一般情况下使用threading，特殊情况才使用thread，下面是原因：
1. threading模块对同步原语的支持更为完善和丰富。
2. threading模块在主线程和子线程交互上更为友好。
3. thread模块不支持守护线程。
    thread模块中主线程退出的时候。所有的子线程不论是否还在工作，都会被强制结束。
4. python3中已经不存在thread模块。

### 建议49：使用Queue使多线程编程更安全

# 第五章 设计模式

### 建议50： 利用模块实现单例模式

### 建议51：用mixin模式让程序更灵活

### 建议52：用发布订阅模式实现松耦合

### 建议53：用状态模式美化代码


# 第六章 内部机制

### 建议54：

### 建议55：

### 建议56：