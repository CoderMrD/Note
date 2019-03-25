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
``` python
# 在INSTALLED_APPS列表中添加
# 自动添加的，如果不自动添加，直接加app名称即可
app名称.apps.app名称Config
```



supervisorctl reload
supervisorctl status



