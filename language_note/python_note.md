## note
- Python中的字符串有两种数据类型：str类型和unicode类型。str类型采用的ASCII编码，也就是说它无法表示中文。unicode类型采用unicode编码，能够表示任意字符，包括中文及其它语言。

- 类的私有变量和私有方法
在Python中可以通过在属性变量名前加上双下划线定义属性为私有属性
特殊变量命名

    - 1、 _xx 以单下划线开头的表示的是protected类型的变量。即保护类型只能允许其本身与子类进行访问。若内部变量标示，如： 当使用“from M import”时，不会将以一个下划线开头的对象引入 。

    - 2、 __xx 双下划线的表示的是私有类型的变量。只能允许这个类本身进行访问了，连子类也不可以用于命名一个类属性（类变量），调用时名字被改变（在类FooBar内部，__boo变成_FooBar__boo,如self._FooBar__boo）

    - 3、 __xx__定义的是特列方法。用户控制的命名空间内的变量或是属性，如init , __import__或是file 。只有当文档有说明时使用，不要自己定义这类变量。 （就是说这些是python内部定义的变量名）
 
- callable()

```
1. 方法用来检测对象是否可被调用，可被调用指的是对象能否使用()括号的方法调用。
2. 可调用对象，在实际调用也可能调用失败；但是不可调用对象，调用肯定不成功。
3. 类对象都是可被调用对象，类的实例对象是否可调用对象，取决于类是否定义了__call__方法。
```

- map(function,iterable, ...)

`
map() 会根据提供的函数对指定序列做映射。
第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。
`

## 内置函数

- dict

```
has_key(k)
D.has_key(k) --> True if D has a key k, else False 
```

- getattr

```python
# getattr() 函数用于返回一个对象属性值。
# 也可以用于对象里面找方法
```

- callable(object)

```
1. 方法用来检测对象是否可被调用，可被调用指的是对象能否使用()括号的方法调用。
2. 可调用对象，在实际调用也可能调用失败；但是不可调用对象，调用肯定不成功。
3. 类对象都是可被调用对象，类的实例对象是否可调用对象，取决于类是否定义了__call__方法。
```

- islice
from itertools import islice
islice(seq[, start], stop[, step]);返回序列seq的从start开始到stop结束的步长为step的元素的迭代器islice(seq[, start], stop[, step])

### subrocess

- subprocess.Pope(args,stdin=None, stdout=None, stderr=None,shell=False)

```
产生子进程,并连接到子进程的标准输入/输出/错误中去，还可以得到子进程的返回值
```

- subprocess.PIPE

```
一个可以被用于Popen的stdin、stdout 和stderr 3个参数的特输值，表示需要创建一个新的管道
```

- Pope.communicate()

```
参数是标准输入，返回标准输出和标准错误：stdout, stderr = Pope.communicate()
```

- is

```
is 比较的是两个实例对象是不是完全相同，它们是不是同一个对象，占用的内存地址是否相同
```

- string.atoi(s[, base]) 字符串转换成整型,base是进制，默认是10

- string.atof(s)将字符串转为浮点型数字

- extend()

`
append()拼接的时候是将拼接内容看做一个对象，extend()拼接的时候是将拼接内容看成一个序列,如果是一个列表就把列表中的元素一个一个拼接上去，而append则会把这个列表当成一个元素。
`

- lower()

`
字符串中的大写字母转换成小写字母
`

- upper()

`
字符串中的小写字母转为大写字母。
`

## 正则
- re.compile

`
compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 match() 和 search() 这两个函数使用
`

`
re.compile(pattern[, flags])
参数：

pattern : 一个字符串形式的正则表达式

flags : 可选，表示匹配模式，比如忽略大小写，多行模式等，具体参数为：

re.I 忽略大小写
re.L 表示特殊字符集 \w, \W, \b, \B, \s, \S 依赖于当前环境
re.M 多行模式
re.S 即为 . 并且包括换行符在内的任意字符（. 不包括换行符）
re.U 表示特殊字符集 \w, \W, \b, \B, \d, \D, \s, \S 依赖于 Unicode 字符属性数据库
re.X 为了增加可读性，忽略空格和 # 后面的注释
`

- re.match

`
re.match 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。
`

`
re.match(pattern, string, flags=0)
参数	描述
pattern	匹配的正则表达式
string	要匹配的字符串。
flags	标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。
`

- re.search

`
re.search 扫描整个字符串并返回第一个成功的匹配。
`

`
re.search(pattern, string, flags=0)
参数	描述
pattern	匹配的正则表达式
string	要匹配的字符串。
flags	标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。
匹配成功re.search方法返回一个匹配的对象，否则返回None。

我们可以使用group(num) 或 groups() 匹配对象函数来获取匹配表达式。
`

`
re.match与re.search的区别
re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，函数返回None；而re.search匹配整个字符串，直到找到一个匹配。
`

- IP判断

`
'^(([01]?\d\d?|2[0-4]\d|25[0-5])\.){3}([01]?\d\d?|2[0-4]\d|25[0-4])$'
`

## os
- os.chdir()

`
改变当前工作目录到指定的路径。
`
- os.getcwd()

`
获取当前工作目录
`

- os.path.abspath()

`os.path.abspath取决于os.getcwd,如果是一个绝对路径，就返回，如果不是绝对路径，根据编码执行getcwd/getcwdu. 
然后把path和当前工作路径连接起来
`

- os.path.split(path) 

`
将path分割成目录和文件名二元组返回。 
`

- os.path.dirname(path) 

`
返回path的目录。其实就是os.path.split(path)的第一个元素。 
`

- os.getenv()

`
os.getenv()获取一个环境变量，如果没有返回none
`
- os.pardir()

```
获取当前目录的父目录字符串名：('..')
```

## sys
- sys.argv

`
返回一个列表，第一个元素是此py文件位置，第二个往后是运行的时候输入的参数
`

## time
- ctime
`
将时间戳转化成友好的时间格式，如果没有参数，则默认参数为time.time，即当前时间
`

## threading
- threading.Thread(self, group=None, target=None, name=None,
                 args=(), kwargs=None, verbose=None))
`
target： 指定线程由 run () 方法调用的可调用对象。默认为 None, 意味着不调用任何内容。

name： 指定该线程的名称。 在默认情况下，创建一个唯一的名称。

args： target调用的实参，元组格式。默认为 ()，即不传参。

daemon： 为False表示父线程在运行结束时需要等待子线程结束才能结束程序，为True则表示父线程在运行结束时，子线程无论是否还有任务未完成都会跟随父进程退出，结束程序。（python2和3可能有区别）
`

- start方法和run方法

`
start() 方法是启动一个子线程，线程名就是我们定义的name
run() 方法并不启动一个新线程，就是在主线程中调用了一个普通函数而已。
想启动多线程，就必须使用start()方法。
`

- threading.Timer(interval, function, args=[], kwargs={})

`
threading的派生类，可以用来定时任务，如果要重复执行某个任务，可以在function中再定义一个threading.time()
`

- threading.current_thread().name  （或者threading.current_thread().getName()）

`
线程名，只是一个标识符，可以使用getName()、setName()获取和运行时重命名。
`

- threading.current_thread().ident       
  
`
线程ID，非0整数。线程启动后才会有ID，否则为None。线程退出，此ID依旧可以访问。此ID可以重复使用
`

- threading.current_thread().is_alive()  

`
返回线程是否存活，布尔值，True或False。
`

- threading.active_count()

`
返回当前活跃的Thread对象数量。返回值和通过enumerate()返回的列表长度是相等的。
`

- join([timeout])方法

`threading.Thread.join。主线程A中，创建了子线程B，并且在主线程A中调用了B.join()，那么，主线程A会在调用的地方等待，直到子线程B完成操作后，才可以接着往下执行，那么在调用这个线程时可以使用被调用线程的join方法。
里面的参数时可选的，代表线程运行的最大时间，即如果超过这个时间，不管这个此线程有没有执行完毕都会被回收，然后主线程或函数都会接着执行的。
join（）的作用是，在子线程完成运行之前，这个子线程的父线程将一直被阻塞,设置为None则等待子进程执行完毕

`

- setDaemon()方法

`
主线程A中，创建了子线程B，并且在主线程A中调用了B.setDaemon(),这个的意思是，把主线程A设置为守护线程，这时候，要是主线程A执行结束了，就不管子线程B是否完成,一并和主线程A退出.这就是setDaemon方法的含义，这基本和join是相反的。此外，还有个要特别注意的：必须在start() 方法调用之前设置，如果不设置为守护线程，程序会被无限挂起。
`
## 浮点数比较大小

- math.isclose(a,b,abs_tol=0.0001)
求差然后求绝对值，如果小于误差那么判断相等

## 文件读写
- write:写入单个变量，如果要换行，加入\n
- writelines：写入多个变量，用[]表示
二者都只能写字符串，如果要传入其他的，必须转成字符串
with open as f:
    f.write()
a为追加方式写

## json
- json.dumps()

`
将 Python 对象编码成 JSON 字符串
`

- json.loads()

`
将已编码的 JSON 字符串解码为 Python 对象
`

- 如果要处理的是文件而不是字符串，可以使用 json.dump() 和 json.load() 来编码和解码JSON数据。

## 数据库

### 原始操作
要操作关系数据库，首先需要连接到数据库，一个数据库连接称为Connection；
连接到数据库后，需要打开游标，称之为Cursor，通过Cursor执行SQL语句，然后，获得执行结果。

### SQLAlchemy
orm
- engine = create_engine()用来初始化数据库连接。SQLAlchemy用一个字符串表示连接信息：
'数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名'
eg:   'mysql+mysqlconnector://root:password@localhost:3306/test'
- 创建DBSession类型:
DBSession = sessionmaker(bind=engine)
# 创建Session:
session = DBSession()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
user = session.query(User).filter(User.id=='5').one()
# 删除操作
delete中添加synchronize_session = False参数，表示删除时不进行同步，只删除内存中的，不commit不同步到硬盘里面的数据库

## javascript

- var关键字影响了变量的作用域。

`
函数外部：变量不管是否用了var申明，都是全局变量。

函数内部：变量如果没有使用var关键字申明，那它就是全局变量，只有用var关键字申明了，才是局部变量。
`

- prompt("")

`
t=prompt("enter"); //出现一个弹框，标题为enter，将输入的值赋给t
`

- 鼠标事件

`
①按下时：onclick=”执行的语句”;

②鼠标移动到上面时：onMouseOver=”执行的语句”;

③鼠标离开：onMouseOut=”执行的语句”;

④点击后生效：onClick=”执行的语句”;（仅限鼠标左键）

⑤鼠标按下后生效：onMouseDown=”执行的语句”;（左右键都有用）

⑧判断路径中，文件名是否有某个关键词；
png=document.getElementById("01png");//获取id为01png的元素
if(png.src.match("01.png")) //如果路径中有关键词01，
`

- 大小写

`
js对大小写敏感，css对大小写不敏感，但如果名称涉及HTML等，则需要注意大小写
`


- push

`
push() 方法可向数组的末尾添加一个或多个元素，并返回新的长度，返回新的长度。

- call

`
在特定的作用域中调用函数，等于设置函数体内this对象的值，以扩充函数赖以运行的作用域。
一般来说，this总是指向调用某个方法的对象，但是使用call()和apply()方法时，就会改变this的指向。
`

`
## JQuary

`
$ (selector).action()

其中$是必须的，表示使用jQuery语法；

selector表示你要对哪个进行操作；

action()表示进行的操作；
`

`
$(this) 表示对当前HTML元素进行操作

$(“#abc”) 表示对id为abc的元素进行操作

$(“.abc”) 表示对class=”abc”的进行操作
`

`
$(document).ready

这个存在的意义在于，只有当文档加载完毕（不确定是指所有文档，还是指使用的文档的那一部分），才能运行jQuery代码
`

- 选择器

`
（4）选择器

①$(“p”) 选择元素为<p>的

②$(“p.abc”) 选择class=”abc”的<p>元素

③$(“p#abc”) 选择id=”abc”的<p>元素

④$(“[href]”) 选择所有带有href属性的元素

⑤$(“[href=’#’]”) 选择所有带href值等于“#”的元素

⑥$(“[href!=’#’]”) 选择所有带href值不等于“#”的元素

⑦$(“[href$=’.jpg’]”) 选择所有带href，末尾以.jpg结尾的元素
`

- 事件触发条件

`
①ready是完成后触发，一般用于文档。$(document).ready(执行的命令)

②click是点击后触发，一般用于按钮，也可以用于点击文档某区域。$(selector).click(执行的命令)

③dclick是双击后触发。$(selector).dclick(执行的命令);

④focus是元素获得焦点时触发的事件；

⑤mouseover是鼠标悬停后触发的事件；
`

## dojo

- 加载插件

`
<script>
require([ //这行表示要加载东西了，用哪个加载哪个||这些直接映射到文件名，如果你下载的Dojo源分布 ，并期待在dojo目录，你会看到dom.js和dom-construct.js文件，这些文件定义这些模块。

    'dojo/dom', //加载dojo文件夹下的dom插件（应该）

    'dojo/fx', //加载fx插件，这个插件包括一个滑动动画（slideTo），还有其他

    'dojo/domReady!' //这个插件大概作用是，保证加载完毕后才执行，以免执行一个没加载好的。

], //这行已经加载结束了

function (dom,fx) { //这是一个回调函数（即加载完才执行的），参数有dom和fx（这个应该指的是插件）

    var greeting = dom.byId('greeting');//得到id为greeting的元素，赋值给greeting这个变量

    greeting.innerHTML += ' from Dojo!';//这个元素加入文本（+=）

} //这行是函数完

); //到这部分是require完

</script>
关于插件的加载：

回调函数中的顺序，是按照插件的顺序填写的。否则就很可能会插件加载出错！！
`

- AJAX异步加载

`
插件：dojo/request

参数：request

语法（get）：

request.get(URL).then(成功回调函数,失败回调函数);

第一个回调函数是成功的，参数用response；（也可以用其他的）

第二个回调函数是失败的，参数用error；（也可以用其他的）
`

- dojo.declare 定义类

`
dojo.declare 方法的 API 如下，它有如下三个参数：

dojo.declare 参数定义
dojo.declare(/*String*/  className, 
/*Function | Function[]*/ superclass, 
/*Object*/ props )

className: 是要要申明的类的类名，也就是创建的构造函数的名称。

superclass：所要继承的父类，此参数可为 null，表示没有父类，或者为一个父类，或为多个父类的数组。

props：散列体，由名、值（key, value）对组成，这个散列体将被添加到定义的类的原型对象中，也即为定义的类被其所有实例共享的属性及方法。其中，key ：constructor 为保留字，此函数用来初始化新对象。
`

- Define

`
先看define。作用是定义一个模块（module）。这个模块可以被require引用，引用了之后就可以使用define里面的东西。一个模块想当然，里面干什么事情，不一定全部自己实现。就像人要coding，除了脑子，也不能没有电脑、键盘。因此，define的第一个参数就是将要用到的其他模块引进来。第二个参数描述这个模块具体干什么，并且给第一个参数中的模块分别起一个朗朗上口的名字。就像下面这段代码描述的样子。
`

`
define([ "dojo/dom"], function(dom) {
	return {
		setRed: function(id){
			dom.byId(id).style.color = "red";
		}
	};
`

- declare

`
如果想定义“类”一样的东西，有状态，可以创建多个对象，就需要在define里用declare。最典型的例子就是dijit下面的诸多UI小控件。

举个很简单的例子，我希望基于dijit.Dialog，创建一个有特殊功能的dialog，每次打开后能把上面的一段text标记为红色。
 `

## MD5加密算法

- 取模（就是取余数）

`
对于整型数a，b来说，取模运算的方法都是：
1.求 整数商： c = a/b;
2.计算模： r = a - c*b.
`

- 计算

`
1、数据填充

对消息进行数据填充，使消息的长度对512取模得448，设消息长度为X，即满足X mod 512=448。根据此公式得出需要填充的数据长度。(最小为448，其余的是448+512的倍数,一个ASCII码就是一个字节)

填充方法：在消息后面进行填充，填充第一位为1，其余为0。

2、添加消息长度

在第一步结果之后再填充上原消息的长度，可用来进行的存储长度为64位(占位64位，由低位往高位写)。如果消息长度大于264，则只使用其低64位的值，即（消息长度 对 264取模）。
记录信息长度：用64位来存储填充前信息长度。这64位加在第一步结果的后面，这样信息长度就变为N*512+448+64=(N+1)*512位
在此步骤进行完毕后，最终消息长度就是512的整数倍。

3、数据处理

准备需要用到的数据：

4个常数： A = 0x67452301, B = 0x0EFCDAB89, C = 0x98BADCFE, D = 0x10325476;
4个函数：F(X,Y,Z)=(X & Y) | ((~X) & Z); G(X,Y,Z)=(X & Z) | (Y & (~Z));  H(X,Y,Z)=X ^ Y ^ Z; I(X,Y,Z)=Y ^ (X | (~Z));
`


# win32gui

- FindWindow(lpClassName=None, lpWindowName=None):
    - 描述：自顶层窗口（也就是桌面）开始搜索条件匹配的窗体，并返回这个窗体的句柄。不搜索子窗口、不区分大小写。找不到就返回0
    - 参数：
        - lpClassName：字符型，是窗体的类名，这个可以在Spy++里找到。
        - lpWindowName：字符型，是窗口名，也就是标题栏上你能看见的那个标题。
    - 说明：这个函数我们仅能用来找主窗口。

- FindWindowEx(hwndParent=0, hwndChildAfter=0, lpszClass=None,lpszWindow=None);
    - 描述：搜索类名和窗体名匹配的窗体，并返回这个窗体的句柄。不区分大小写，找不到就返回0。
    - 参数：
        - hwndParent：若不为0，则搜索句柄为hwndParent窗体的子窗体。
        - hwndChildAfter：若不为0，则按照z-index的顺序从hwndChildAfter向后开始搜索子窗体，否则从第一个子窗体开始搜索。
        - lpClassName：字符型，是窗体的类名，这个可以在Spy++里找到。
        - lpWindowName：字符型，是窗口名，也就是标题栏上你能看见的那个标题。
    - 说明：找到了主窗口以后就靠它来定位子窗体啦。