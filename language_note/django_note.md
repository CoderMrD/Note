syncdb老版本django用的迁移命令，现在已经移除。执行这个命令django会查找INSTALLED-APPS里的每一个models.py文件，并为找到的每一个model都创建一张数据库表，但是如果只是修改字段，是不会同步的。
makemigrations 用于执行迁移动作，具有syncdb的功能
migrate 基于当前的model创建新的迁移策略文件
数据库常用字段:
越芽说项目总结
后端django + xadmin
前端
web页面
小程序页面


# 项目搭建

## 一、新建项目
1. 建立project

``` python
django-admin startproject 项目名称
```

生成目录

    项目名称/

        manage.py

        项目名称/

            __init__.py

            settings.py

            urls.py

            wsgi.py
2. 建立app

``` python
python manage.py startapp app名称
```

生成目录

    项目名称/

        manage.py

        项目名称/

            __init__.py

            settings.py

            urls.py

            wsgi.py
    

        app名称/

            __init__.py

            models.py

            views.py

- 可以看出多了一个app名称的文件夹,里面有models，views
    - model:模型，数据库模型。

    - views:视图，处理业务逻辑，通过创建项目生成的urls.py将url请求映射到views中来处理.
    - template:模板，这个文件夹不存在，是可以自己在app目录下创建template目录，然后将前台的html等内容放置在这个目录下以实现MTV的结构

- 可以看出app是一个相对独立的MTV结构，使得不同的app可以在不同的项目中使用，体现出了django的设计理念:不要做重复的事情。

3. 简单设置
- 在setting.py中注册app
子应用的配置信息文件apps.py中的Config类添加到INSTALLED_APPS列表中。
例如，将刚创建的users子应用添加到工程中，可在INSTALLED_APPS列表中添加**'users.apps.UsersConfig'**。（app名称.apps.app名称Config）

- 配置数据库
对DATABASE进行修改
默认是sqlite
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR,'sqlite.db'),
        }
os.path拼接的是sqlite的文件名，在自己开发的时候可以使用sqlite，比较简单，不需要安装
配置mysql
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'database名字',
        'USER':'root',
        'PASSWORD':'MySQL数据库密码',
        'HOST':'127.0.0.1',
    }
}

python3连接mysql需要安装pymysql

```shell
pip install PyMYSQL
```
在项目文件夹中的__init__(和setting.py在同一文件夹)中添加以下代码
```python
import pymysql
pymysql.install_as_MySQLdb()
```
接下来就可以连接mysql了

- 配置ALLOWED_HOST 
ALLOWED_HOSTS是为了限定请求中的host值，以防止黑客构造包来发送请求。只有在列表中的host才能访问，里面是字符串列表，
这个字符串列表值表示当下这个Django站点可以提供的host/domain(主机/域名），不建议使用'*' 来配置，不安全
可以使用绝对匹配，也可以使用正则中的一些通配符来匹配

ALLOWED_HOSTS = []
当DEBUG设置为flase的时候，必须设定ALLOWED_HOSTS的值，否则会抛出异常
当DEBUG设置为True，且ALLOWED_HOSTS设置为空，主机将针对['localhost'，'127.0.0.1'，'[:: 1]']进行验证
django默认工作在调式Debug模式下，如果增加、修改、删除文件，服务器会自动重启


4. 创建视图

视图应定义在子应用的views.py中
### 1. 创建

打开刚创建的users模块(app)，在views.py中编写视图代码。

```python
from django.http import HttpResponse

def index(request):
    """
    index视图
    :param request: 包含了请求信息的请求对象
    :return: 响应对象
    """
    return HttpResponse("hello the world!")
```

说明：

* 视图函数的第一个传入参数必须定义，用于接收Django构造的包含了请求数据的**HttpReqeust**对象，通常名为**request**。
* 视图函数的返回值必须为一个响应对象，不能像Flask一样直接返回一个字符串，可以将要返回的字符串数据放到一个**HTTPResponse**对象中。

### 2. 定义路由URL

#### 1) 在子应用中新建一个urls.py文件用于保存该应用的路由。

![新建urls.py文件](/images/new_urls_file.png)

#### 2) 在users/urls.py文件中定义路由信息。

```python
from django.conf.urls import url

from . import views

# urlpatterns是被django自动识别的路由列表变量
urlpatterns = [
    # 每个路由信息都需要使用url函数来构造
    # url(路径, 视图)
    url(r'^index/$', views.index),
]
```

#### 3)  在工程总路由demo/urls.py中添加子应用的路由数据。

```python
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),  # django默认包含的
    
    # 添加
    url(r'^users/', include('users.urls')), 
]
```

* 使用include来将子应用users里的全部路由包含进工程路由中；
* **r'^users/'** 决定了users子应用的所有路由都已**/users/**开头，如我们刚定义的视图index，其最终的完整访问路径为**/users/index/**。

**include**函数除了可以传递字符串之外，也可以直接传递应用的urls模块，如

```python
from django.conf.urls import url, include
from django.contrib import admin
import users.urls  # 先导入应用的urls模块

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^users/', include('users.urls')),
    url(r'^users/', include(users.urls)),  # 添加应用的路由
]
```

#### 4) 启动运行

重新启动django程序

```shell
python manage.py runserver
```

在浏览器中输入网址**127.0.0.1:8000/users/index/** 可看到返回的信息

![返回结果](/images/hello_the_world.png)

# 二、 配置、静态文件与路由

# 配置文件(settings.py文件)

## 1. BASE_DIR

```python
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
```

当前工程的根目录（manage.py文件所在目录），Django会依此来定位工程内的相关文件，我们也可以使用该参数来构造文件路径。

## 2. DEBUG

调试模式，创建工程后初始值为**True**，即默认工作在调试模式下。

作用：

* 修改代码文件，程序自动重启

* Django程序出现异常时，向前端显示详细的错误追踪信息，例如

  ![错误追踪](/images/error_trackback.png)

  而非调试模式下，仅返回Server Error (500)

**注意：部署线上运行的Django不要运行在调式模式下，记得修改DEBUG=False。**

## 3. 本地语言与时区

Django支持本地化处理，即显示语言与时区支持本地化。

本地化是将显示的语言、时间等使用本地的习惯，这里的本地化就是进行中国化，中国大陆地区使用**简体中文**，时区使用**亚洲/上海**时区，注意这里不使用北京时区表示。

初始化的工程默认语言和时区为英语和UTC标准时区

```python
LANGUAGE_CODE = 'en-us'  # 语言
TIME_ZONE = 'UTC'  # 时区
```

将语言和时区修改为中国大陆信息

```python
LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'
```

![中文默认页面](/images/chinese_index_page.png)


# 静态文件

项目中的CSS、图片、js都是静态文件。一般会将静态文件放到一个单独的目录中，以方便管理。在html页面中调用时，也需要指定静态文件的路径，Django中提供了一种解析的方式配置静态文件路径。静态文件可以放在项目根目录下，也可以放在应用的目录下，由于有些静态文件在项目中是通用的，所以推荐放在项目的根目录下，方便管理。

为了提供静态文件，需要配置两个参数：

* **STATICFILES_DIRS** 存放查找静态文件的目录
* **STATIC_URL** 访问静态文件的URL前缀


## 示例

1） 在项目根目录下创建static_files目录来保存静态文件。

2） 在demo/settings.py中修改静态文件的两个参数为

```python
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static_files'),
]
```

3）此时在static_files添加的任何静态文件都可以使用网址 **/static/文件在static_files中的路径** 来访问了。

例如，我们向static_files目录中添加一个index.html文件，在浏览器中就可以使用127.0.0.1:8000/static/index.html来访问。

或者我们在static_files目录中添加了一个子目录和文件goods/detail.html，在浏览器中就可以使用127.0.0.1:8000/static/goods/detail.html来访问。

### 注意

Django 仅在调试模式下（DEBUG=True）能对外提供静态文件。

当DEBUG=False工作在生产模式时，Django不再对外提供静态文件，需要是用collectstatic命令来收集静态文件并交由其他静态文件服务器来提供。（详细在部署时会讲）

# 路由说明

![视图处理流程](/images/view_process.png)

## 1. 路由定义位置

Django的主要路由信息定义在工程同名目录下的urls.py文件中，该文件是Django解析路由的入口。

每个子应用为了保持相对独立，可以在各个子应用中定义属于自己的urls.py来保存该应用的路由。然后用主路由文件包含各应用的子路由数据。

除了上述方式外，也可将工程的全部路由信息都定义在主路由文件中，子应用不再设置urls.py。如：

```
from django.conf.urls import url
from django.contrib import admin
import users.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^users/index/$', users.views.index)
]
```

## 2. 路由解析顺序

Django在接收到一个请求时，从主路由文件中的urlpatterns列表中以由上至下的顺序查找对应路由规则，如果发现规则为include包含，则再进入被包含的urls中的urlpatterns列表由上至下进行查询。

值得关注的**由上至下**的顺序，有可能会使上面的路由屏蔽掉下面的路由，带来非预期结果。例如：

```python
urlpatterns = [
    url(r'^say', views.say),
    url(r'^sayhello', views.sayhello),
]
```

即使访问sayhello/路径，预期应该进入sayhello视图执行，但实际优先查找到了say路由规则也与sayhello/路径匹配，实际进入了say视图执行。

#### 提示：

**需要注意定义路由的顺序，避免出现屏蔽效应。**

## 3. 路由命名与reverse反解析（逆向）

### 3.1 路由命名

在定义路由的时候，可以为路由命名，方便查找特定视图的具体路径信息。

1) 在使用include函数定义路由时，可以使用namespace参数定义路由的命名空间，如

```python
url(r'^users/', include('users.urls', namespace='users')),
```

命名空间表示，凡是users.urls中定义的路由，均属于namespace指明的users名下。

**命名空间的作用：避免不同应用中的路由使用了相同的名字发生冲突，使用命名空间区别开。**

2) 在定义普通路由时，可以使用name参数指明路由的名字，如

```python
urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^say', views.say, name='say'),
]
```

### 3.2 reverse反解析

使用reverse函数，可以根据路由名称，返回具体的路径，如：

```python
from django.urls import reverse  # 注意导包路径

def index(request):
    return HttpResponse("hello the world!")

def say(request):
    url = reverse('users:index')  # 返回 /users/index/
    print(url)
    return HttpResponse('say')
```

* 对于未指明namespace的，reverse(路由name)
* 对于指明namespace的，reverse(命名空间namespace:路由name)

Django中提供了一个关于URL的映射的解决方案，你可以做两个方向的使用：

1.有客户端的浏览器发起一个url请求，Django根据URL解析，把url中的参数捕获，调用相应的试图，

    获取相应的数据，然后返回给客户端显示

2.通过一个视图的名字，再加上一些参数和值，逆向获取相应的URL

第一个就是平常的请求有URLconf来解析的过程，第二个叫做，url的逆向解析，url逆向匹配，url的逆向查阅，等

## 4. 路径结尾斜线/的说明

Django中定义路由时，通常以斜线/结尾，其好处是用户访问不以斜线/结尾的相同路径时，Django会把用户重定向到以斜线/结尾的路径上，而不会返回404不存在。如

```python
urlpatterns = [
    url(r'^index/$', views.index, name='index'),
]
```

用户访问 index 或者 index/ 网址，均能访问到index视图。

**说明：**

虽然路由结尾带/能带来上述好处，但是却违背了HTTP中URL表示资源位置路径的设计理念。

是否结尾带/以所属公司定义风格为准。

# 三、请求与响应
request
response
cookie
session

# 请求

回想一下，利用HTTP协议向服务器传参有几种途径？

+ 提取URL的特定部分，如/weather/beijing/2018，可以在服务器端的路由中用正则表达式截取；
+ 查询字符串（query string)，形如key1=value1&key2=value2；
+ 请求体（body）中发送的数据，比如表单数据、json、xml；
+ 在http报文的头（header）中。

## 1 URL路径参数

在定义路由URL时，可以使用正则表达式提取参数的方法从URL中获取请求参数，Django会将提取的参数直接传递到视图的传入参数中。

* 未命名参数按定义顺序传递， 如

  ```python
  url(r'^weather/([a-z]+)/(\d{4})/$', views.weather),

  def weather(request, city, year):
      print('city=%s' % city)
      print('year=%s' % year)
      return HttpResponse('OK')
  ```

* 命名参数按名字传递，如

  ```python
  url(r'^weather/(?P<city>[a-z]+)/(?P<year>\d{4})/$', views.weather),

  def weather(request, year, city):
      print('city=%s' % city)
      print('year=%s' % year)
      return HttpResponse('OK')
  ```

## 2 Django中的QueryDict对象

定义在django.http.QueryDict

HttpRequest对象的属性GET、POST都是QueryDict类型的对象

与python字典不同，QueryDict类型的对象用来处理同一个键带有多个值的情况

- 方法get()：根据键获取值

  如果一个键同时拥有多个值将获取最后一个值

  如果键不存在则返回None值，可以设置默认值进行后续处理
  
  ```python
  dict.get('键',默认值)
  可简写为
  dict['键']
  ```

- 方法getlist()：根据键获取值，值以列表返回，可以获取指定键的所有值

  如果键不存在则返回空列表[]，可以设置默认值进行后续处理

  ```python
  dict.getlist('键',默认值)
  ```

## 3. 查询字符串Query String

获取请求路径中的查询字符串参数（形如?k1=v1&k2=v2），可以通过request.GET属性获取，返回QueryDict对象。

```python
# /qs/?a=1&b=2&a=3

def qs(request):
    a = request.GET.get('a')
    b = request.GET.get('b')
    alist = request.GET.getlist('a')
    print(a)  # 3
    print(b)  # 2
    print(alist)  # ['1', '3']
    return HttpResponse('OK')
```

**重要：查询字符串不区分请求方式，即假使客户端进行POST方式的请求，依然可以通过request.GET获取请求中的查询字符串数据。**

## 4 请求体

请求体数据格式不固定，可以是表单类型字符串，可以是JSON字符串，可以是XML字符串，应区别对待。

可以发送请求体数据的请求方式有**POST**、**PUT**、**PATCH**、**DELETE**。

**Django默认开启了CSRF防护**，会对上述请求方式进行CSRF防护验证，在测试时可以关闭CSRF防护机制，方法为在settings.py文件中注释掉CSRF中间件，如：

![注释CSRF中间件](/images/csrf_middleware.png)

### 4.1 表单类型 Form Data

前端发送的表单类型的请求体数据，可以通过request.POST属性获取，返回QueryDict对象。

```python
def get_body(request):
    a = request.POST.get('a')
    b = request.POST.get('b')
    alist = request.POST.getlist('a')
    print(a)
    print(b)
    print(alist)
    return HttpResponse('OK')
```

**重要：request.POST只能用来获取POST方式的请求体表单数据。**

## 4.2 非表单类型 Non-Form Data

非表单类型的请求体数据，Django无法自动解析，可以通过**request.body**属性获取最原始的请求体数据，自己按照请求体格式（JSON、XML等）进行解析。**request.body返回bytes类型。**

例如要获取请求体中的如下JSON数据

```json
{"a": 1, "b": 2}
```

可以进行如下方法操作：

```python
import json

def get_body_json(request):
    json_str = request.body
    json_str = json_str.decode()  # python3.6 无需执行此步
    req_data = json.loads(json_str)
    print(req_data['a'])
    print(req_data['b'])
    return HttpResponse('OK')
```

## 5 请求头

可以通过**request.META**属性获取请求头headers中的数据，**request.META为字典类型**。

常见的请求头如：

- `CONTENT_LENGTH` – The length of the request body (as a string).
- `CONTENT_TYPE` – The MIME type of the request body.
- `HTTP_ACCEPT` – Acceptable content types for the response.
- `HTTP_ACCEPT_ENCODING` – Acceptable encodings for the response.
- `HTTP_ACCEPT_LANGUAGE` – Acceptable languages for the response.
- `HTTP_HOST` – The HTTP Host header sent by the client.
- `HTTP_REFERER` – The referring page, if any.
- `HTTP_USER_AGENT` – The client’s user-agent string.
- `QUERY_STRING` – The query string, as a single (unparsed) string.
- `REMOTE_ADDR` – The IP address of the client.
- `REMOTE_HOST` – The hostname of the client.
- `REMOTE_USER` – The user authenticated by the Web server, if any.
- `REQUEST_METHOD` – A string such as `"GET"` or `"POST"`.
- `SERVER_NAME` – The hostname of the server.
- `SERVER_PORT` – The port of the server (as a string).

具体使用如:

```python
def get_headers(request):
    print(request.META['CONTENT_TYPE'])
    return HttpResponse('OK')
```

## 6 其他常用HttpRequest对象属性

- **method**：一个字符串，表示请求使用的HTTP方法，常用值包括：'GET'、'POST'。
- **user：请求的用户对象。**
- path：一个字符串，表示请求的页面的完整路径，不包含域名和参数部分。
- encoding：一个字符串，表示提交的数据的编码方式。
  - 如果为None则表示使用浏览器的默认设置，一般为utf-8。
  - 这个属性是可写的，可以通过修改它来修改访问表单数据使用的编码，接下来对属性的任何访问将使用新的encoding值。


- FILES：一个类似于字典的对象，包含所有的上传文件。

# 响应

视图在接收请求并处理后，必须返回HttpResponse对象或子对象。HttpRequest对象由Django创建，HttpResponse对象由开发人员创建。

## 1 HttpResponse

可以使用**django.http.HttpResponse**来构造响应对象。

```python
HttpResponse(content=响应体, content_type=响应体数据类型, status=状态码)
```

也可通过HttpResponse对象属性来设置响应体、状态码：

- content：表示返回的内容。
- status_code：返回的HTTP响应状态码。

响应头可以直接将HttpResponse对象当做字典进行响应头键值对的设置：

```python
response = HttpResponse()
response['Itcast'] = 'Python'  # 自定义响应头Itcast, 值为Python
```

示例：

```python
from django.http import HttpResponse

def demo_view(request):
    return HttpResponse('itcast python', status=400)
    或者
    response = HttpResponse('itcast python')
    response.status_code = 400
    response['Itcast'] = 'Python'
    return response
```

## 2 HttpResponse子类

Django提供了一系列HttpResponse的子类，可以快速设置状态码

* HttpResponseRedirect  301
* HttpResponsePermanentRedirect  302
* HttpResponseNotModified  304
* HttpResponseBadRequest  400
* HttpResponseNotFound  404
* HttpResponseForbidden  403
* HttpResponseNotAllowed  405
* HttpResponseGone  410
* HttpResponseServerError  500

## 3 JsonResponse

若要返回json数据，可以使用JsonResponse来构造响应对象，作用：

* 帮助我们将数据转换为json字符串
* 设置响应头**Content-Type**为 **application/json**

```python
from django.http import JsonResponse

def demo_view(request):
    return JsonResponse({'city': 'beijing', 'subject': 'python'})
```

## 4 redirect重定向

```python
from django.shortcuts import redirect

def demo_view(request):
    return redirect('/index.html')
```

# Cookie

Cookie，有时也用其复数形式Cookies，指某些网站为了辨别用户身份、进行session跟踪而储存在用户本地终端上的数据（通常经过加密）。Cookie最早是网景公司的前雇员Lou Montulli在1993年3月的发明。Cookie是由服务器端生成，发送给User-Agent（一般是浏览器），浏览器会将Cookie的key/value保存到某个目录下的文本文件内，下次请求同一网站时就发送该Cookie给服务器（前提是浏览器设置为启用cookie）。Cookie名称和值可以由服务器端开发自己定义，这样服务器可以知道该用户是否是合法用户以及是否需要重新登录等。服务器可以利用Cookies包含信息的任意性来筛选并经常性维护这些信息，以判断在HTTP传输中的状态。Cookies最典型记住用户名。

Cookie是存储在浏览器中的一段纯文本信息，建议不要存储敏感信息如密码，因为电脑上的浏览器可能被其它人使用。

#### Cookie的特点

- Cookie以键值对的格式进行信息的存储。
- Cookie基于域名安全，不同域名的Cookie是不能互相访问的，如访问itcast.cn时向浏览器中写了Cookie信息，使用同一浏览器访问baidu.com时，无法访问到itcast.cn写的Cookie信息。
- 当浏览器请求某网站时，会将浏览器存储的跟网站相关的所有Cookie信息提交给网站服务器。

## 1 设置Cookie

可以通过**HttpResponse**对象中的**set_cookie**方法来设置cookie。

```python
HttpResponse.set_cookie(cookie名, value=cookie值, max_age=cookie有效期)
```

* **max_age**  单位为秒，默认为**None**。如果是临时cookie，可将max_age设置为None。

示例：

```python
def demo_view(request):
    response = HttpResponse('ok')
    response.set_cookie('itcast1', 'python1')  # 临时cookie
    response.set_cookie('itcast2', 'python2', max_age=3600)  # 有效期一小时
    return response
```

## 2 读取Cookie

可以通过**HttpRequest**对象的**COOKIES**属性来读取本次请求携带的cookie值。**request.COOKIES为字典类型**。

```python
def demo_view(request):
    cookie1 = request.COOKIES.get('itcast1')
    print(cookie1)
    return HttpResponse('OK')
```

# Session

## 1 启用Session

**Django项目默认启用Session。**

可以在settings.py文件中查看，如图所示

![session中间件](/images/session_middleware.png)

如需禁用session，将上图中的session中间件注释掉即可。

## 2 存储方式

在settings.py文件中，可以设置session数据的存储方式，可以保存在数据库、本地缓存等。

### 2.1 数据库

存储在数据库中，如下设置可以写，也可以不写，**这是默认存储方式**。

```python
SESSION_ENGINE='django.contrib.sessions.backends.db'
```

如果存储在数据库中，需要在项INSTALLED_APPS中安装Session应用。

![session_app](/images/session_app.png)

数据库中的表如图所示

![session数据库](/images/session_database.png)

表结构如下

![session表结构](/images/session_table.png)

由表结构可知，操作Session包括三个数据：键，值，过期时间。

### 2.2 本地缓存

存储在本机内存中，如果丢失则不能找回，比数据库的方式读写更快。

```python
SESSION_ENGINE='django.contrib.sessions.backends.cache'
```

### 2.3 混合存储

优先从本机内存中存取，如果没有则从数据库中存取。

```python
SESSION_ENGINE='django.contrib.sessions.backends.cached_db'
```

### 2.4 Redis

在redis中保存session，需要引入第三方扩展，我们可以使用**django-redis**来解决。

1） 安装扩展

```python
pip install django-redis
```

2）配置

在settings.py文件中做如下设置

```python
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://127.0.0.1:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"
```

#### 注意

 如果redis的ip地址不是本地回环127.0.0.1，而是其他地址，访问Django时，可能出现Redis连接错误，如下：

![redis连接错误](/images/redis_connect_error.png)

解决方法：

修改redis的配置文件，添加特定ip地址。

打开redis的配置文件

```shell
sudo vim /etc/redis/redis.conf
```

在如下配置项进行修改（如要添加10.211.55.5地址）

![修改redis配置文件](/images/modify_redis_config.png)

重新启动redis服务

```shell
sudo service redis-server restart
```

## 3 Session操作

通过HttpRequest对象的session属性进行会话的读写操作。

1） 以键值对的格式写session。

```
request.session['键']=值
```

2）根据键读取值。

```
request.session.get('键',默认值)
```

3）清除所有session，在存储中删除值部分。

```
request.session.clear()
```

4）清除session数据，在存储中删除session的整条数据。

```
request.session.flush()
```

5）删除session中的指定键及值，在存储中只删除某个键及对应的值。

```
del request.session['键']
```

6）设置session的有效期

```
request.session.set_expiry(value)
```

- 如果value是一个整数，session将在value秒没有活动后过期。
- 如果value为0，那么用户session的Cookie将在用户的浏览器关闭时过期。
- 如果value为None，那么session有效期将采用系统默认值，**默认为两周**，可以通过在settings.py中设置**SESSION_COOKIE_AGE**来设置全局默认值。







#### 配置认证user（djjango自带的user表）
AUTH_USER_MODEL='users.UserProfile'

supervisorctl reload
supervisorctl status



