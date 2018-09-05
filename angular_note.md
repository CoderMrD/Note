angular2以前叫做angularjs，以后统称为angular

angular核心特点：方便快捷的编写，高重用的组件，核心就是组件

对比：
	react:速度，适合于其他框架结合用
	vue：简单，灵活，性能，尺寸小

angular下载安装
1、安装nodejs，官网下载，一路下一步（命令行中npm -v可以看到版本号，安装成功）
2、安装angular\cli,命令行npm install -g @angular/cli(需要一会)（ng -v，安装成功）
3、安装webstorm（开发工具），下载，一路下一步。

创建新项目ng new 项目名称，会在当前目录生成一个项目名称的文件夹
一个Angular程序至少需要一个模块和一个组件。
目录结构：
	e2e:自动测试的
	src：我们写的代码
		app:主要代码位置
			app.component.ts:这个便是组件，组件是angular应用的基本构建模块，可以理解为一段带有业务逻辑和数据的html
			app.module.ts:这个表示模块
		envirments
		index.html:整个页面的根HTML，里面有一个app-root标签
		main.ts整个页面的入口点,也是程序的起点
		polyfills.ts：导入一些必要的库
		styles.css：全局的样式写在这里。

	angular-cli.json 可能需要测试
	karma:执行自动化测试的
	package.json模块
组件的必备元素：下面三项

组件元数据装饰器，简称装饰器@component
@component装饰器用来告知angular如何处理一个typescript类，@component装饰器包括多个属性，这些属性的值叫做元数据，会根据元数据的值渲染组件，并执行组件的逻辑。

模板：通过组件自带的模板来定义组件的外观，模板以html的形式存在，看起来像HTML，但是我们可以在模板中使用angular中的数据绑定语法来实现控制器中的数据。

控制器：普通的typescript类，会被component装饰，控制器包含组件所有的属性和方法，绝大多数的逻辑都写在控制器里，控制器通过数据绑定与模板来通讯，模板展现控制器的数据，控制器处理模板上发生的事件。

启动：ng serve

使用第三方库：
1、安装类库：npm install jqery --save (--save：把依赖寄到npm，packege.json文件中)
2、把库引到项目中，添加到style和script中
   在app.component.ts里面使用$符号的时候会报错，因为$是js中的，这里是ts，需要把ts的类型描述文件安装到本地的库中去。要让ts代码认识jquery和bootstrap，命令（npm install @types/bootstrap --save,jquery同前面的）
   
auction组件图
![auction组件图](https://github.com/CoderMrD/Note/blob/master/auction%E7%BB%84%E4%BB%B6.png)
