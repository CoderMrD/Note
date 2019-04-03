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

## 二、新建app

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

## 二、配置
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



supervisorctl reload
supervisorctl status



