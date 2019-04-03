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



#### 配置认证user（djjango自带的user表）
AUTH_USER_MODEL='users.UserProfile'

supervisorctl reload
supervisorctl status



