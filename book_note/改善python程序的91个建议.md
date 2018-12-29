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
1）避免不必要的计算