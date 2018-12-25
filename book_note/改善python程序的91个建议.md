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