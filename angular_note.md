## angular基础

angular2以前叫做angularjs，以后统称为angular

angular核心特点：方便快捷的编写，高重用的组件，核心就是组件，数据绑定，通过操作后台数据，改变前台页面

对比：
	react:速度，适合于其他框架结合用
	vue：简单，灵活，性能，尺寸小
	jquery：操作页面元素DOM

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

	angular-cli.json Angular命令行工具的配置文件。后期可能会去修改它，引一些其他的第三方的包
	karma:执行自动化测试的
	package.json模块
组件的必备元素：下面三项

组件元数据装饰器，简称装饰器@component
@component装饰器用来告知angular如何处理一个typescript类，@component装饰器包括多个属性，这些属性的值叫做元数据，会根据元数据的值渲染组件，并执行组件的逻辑。

模板：通过组件自带的模板来定义组件的外观，模板以html的形式存在，看起来像HTML，但是我们可以在模板中使用angular中的数据绑定语法来实现控制器中的数据。

控制器：普通的typescript类，会被component装饰，控制器包含组件所有的属性和方法，绝大多数的逻辑都写在控制器里，控制器通过数据绑定与模板来通讯，模板展现控制器的数据，控制器处理模板上发生的事件。

启动：ng serve

使用第三方库：
1、安装类库：npm install jquery --save (--save：把依赖寄到npm，packege.json文件中)，安装指定版本jquery@+版本
2、把库引到项目中，添加到style和script中
   在app.component.ts里面使用$符号的时候会报错，因为$是js中的，这里是ts，需要把ts的类型描述文件安装到本地的库中去。要让ts代码认识jquery和bootstrap，命令（npm install @types/bootstrap --save,jquery同前面的）
   
auction组件图
![auction组件图](https://github.com/CoderMrD/Note/blob/master/auction%E7%BB%84%E4%BB%B6.png)

生成组件:
app组件在创建项目的时候已经被生成，命令创建另外六个组件
ng g component navbar 导航栏组件
ng g component footer 页脚组件
ng g component search 搜索表单组件
ng g component carousel 轮播图组件
ng g component product 商品展示组件
ng g component stars  星级评价组件


调用组件：在app.component.html中添加<app-navbar></app-navbar>,当做标签添加

### bootstrap

#### div
- class="container"生成了一个容器,固定宽度,.container-fluid （100% 宽度）
- class="row"添加行
- class="col-md-3",列，包裹于行内，md为中等屏幕 桌面显示器 (≥992px)
- col-lg-12 大屏幕,>1200px
不管在哪种屏幕上，栅格系统都会自动的每行row分12列col-md-后面跟的参数表示在当前的屏幕中，每个div所占列数，3就是3/12，即1/4

#### nav

- .navbar-header ，负责包裹brand和折叠按钮，控制小屏幕时brand和按钮的位置，控制导航列表的布局。
- .navbar-brand, 负责左边logo区的默认样式
- .nav 负责定义成垂直导航的样式
- navbar-toggle：负责定义按钮的样式，里面用三个盒子绘制三条线。在大屏幕时消失。
- collapse，负责控制显示和隐藏
- .navbar-collapse: 负责被折叠盒子的样式


- 提示：如果文档中有“前后”按钮，则应该把它放到 <nav> 元素中。
以下是class属性
- navbar-default   navbar-inverse 这两个控制颜色的属性，一白一黑。 
- navbar主要功能是设置padding，圆角。
- navbar-fixed-top 导航栏固定到顶部
- <div> 元素添加一个标题 class .navbar-header，内部包含了带有 class navbar-brand 的 <a> 元素。这会让文本看起来更大一号
- 为了向导航栏添加链接，只需要简单地添加带有 class .nav、.navbar-nav 的无序列表即可
nav  nav-navbar属性要一起使用，设置浮动菜单项。

按钮中间加入<span class="icon-bar"></span>会多一道横线，看着比较清晰，一般加三条
ul 是无序列表 。内含列表项 li

- data-toggle(与class同等级别):指以什么事件触发
- data-target:指事件的目标

响应式的导航栏
为了给导航栏添加响应式特性，要折叠的内容必须包裹在带有 class .collapse、.navbar-collapse 的 <div> 中。
折叠起来的导航栏实际上是一个带有 class .navbar-toggle 及两个 data- 元素的按钮。
第一个是 data-toggle，用于告诉 JavaScript 需要对按钮做什么，第二个是 data-target，指示要切换到哪一个元素。三个带有 class .icon-bar 的 <span> 创建所谓的汉堡按钮。
这些会切换为 .nav-collapse <div> 中的元素

!important增加样式权重，如果没有这个，出现的晚的样式权重会更高，更加准确定位的权重更高

@media 条件添加css样式
eg：@media (min-width: 768px)最小宽度为768px的时候

带有大于号的选择器，代表选择标签时仅作用与儿子标签而不作用于孙子标签(只有二级标签起作用,一级都不起作用)
eg:div>span只有在div中的二级标签span才起作用


#### 基本表单结构

基本的表单结构是 Bootstrap 自带的，个别的表单控件自动接收一些全局样式。下面列出了创建基本表单的步骤：
1. 向父 <form> 元素添加 role="form"。
2. 把标签和控件放在一个带有 class .form-group 的 <div> 中。这是获取最佳间距所必需的。（增加块元素的下部留白或下部边界，从而使块元素的间距变大）
3. 向所有的文本元素 <input>、<textarea> 和 <select> 添加 class ="form-control" 。（换行+填充整行 ）

- <input>的placeholder 属性规定可描述输入字段预期值的简短的提示信息

role属性：告知标签的作用

<hr>被水平线分隔的标题和段落


form表单中name属性规定表单的名称。
form 元素的 name 属性提供了一种在脚本中引用表单的方法。

<label> 标签为 input 元素定义标注


#### 按钮
- btn 基本按钮样式
- btn-primary：原始按钮样式
- btn-block:拉伸至父级元素的宽度

#### carousel(轮播图)
仿制。。。。

#### product
1. 在product.component.ts中创建商品的类（export class Product{constructor}），constructor构造
2. 在export class ProductComponent implements OnInit类中声明一个private products: Array<Product>;
3. 在ngOnInit中添加只调用一次的数据
4. div中添加*ngFor, *ngFor根据products数组中的数量来生成相应的代码数量,遍历

#### star
1. 显示实心星星<span class="glyphicon glyphicon-star"></span>，在加上glyphicon-star-empty变成空心的星星，
2. 生成5颗星星在后台添加，ts文件中定义私有变量stars,布尔类型数组，然后在ngoninit中定义数值
3. 将商品组件中的数据传递给星级评价的组件,在子属性加上装饰器@Input,然后在调用这个组建的地方把值传递进去<app-stars [rating]="product.rating"></app-stars>


数据绑定
插值表达式{{}}，直接把对象的属性展示在页面上
属性绑定：将html的标签属性和控制器上的属性做绑定eg：将span的class的glyphicon-star-empty属性和后台的star绑定
<span [class.glyphicon-star-empty]="star"></span>

各个组件都是从顶部开始排的，所以会出现覆盖的情况，可以在style.css中加入样式，body{ padding-top:70px} padding-top是设置上内边距

margin-bottom:下边距

单页Web应用（single page web application，SPA），就是只有一张Web页面的应用，是加载单个HTML 页面并在用户与应用程序交互时动态更新该页面的Web应用程序，是指在浏览器中运行的应用，它们在使用期间不会重新加载页面。

error：
Uncaught TypeError: Cannot read property 'fn' of undefined
在进行前端的开发要注意顺序.将packaage中的jquery和bootstrap引入顺序改一下，先导入jQuery，再导入bootstrap即可
bootstrap中css样式不生效，看一下是不是版本不对


响应式布局：（width=device-width表示当前大小按照设备大小，后一个是缩放，等于1是不缩放）
在head中添加<meta name="viewport" content="width=device-width,initial-scale=1">

## router

