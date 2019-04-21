# day1

vue采用M，V，VM(ViewModel)的结构

![MVC&MVVM](/images/MVC和MVVM.png)

当导入包之后，在浏览器的内存中就多了一个Vue构造函数，可以使用new Vue()来创建。

- 定义Vue模块
``` javascript
var vm = new Vue({
    el: '#app', // el是element缩写，表示当前new的这个Vue实例，要控制页面上的哪个区域(dom元素)
    data: { // data属性中，存放的是 el 中要用到的数据
        msg: 'welcome to China' // 
vue的特色之一就是不需要去操作dom元素，使用vue提供的指令，将数据渲染到元素上
    }
})
```
- 使用Vue模块中的数据（插值表达式）

```html
<p>{{ msg }}</p>
```

html文件默认是用file协议打开的，使用http协议打开的话在vscode中可以安装express插件，然后ctrl+shift+p调出命令模式，找到Express: Host Current Workspace and Open in Browser,运行在当前目录的server，使用Express:stop server来停止

## html,css,js加载顺序
1. js放在head中会立即执行，阻塞后续的资源下载与执行。因为js有可能会修改dom，如果不阻塞后续的资源下载，dom的操作顺序不可控。
正常的网页加载流程是这样的。
    - 浏览器一边下载HTML网页，一边开始解析
    - 解析过程中，发现< script >标签
    - 暂停解析，网页渲染的控制权转交给JavaScript引擎
    - 如果< script >标签引用了外部脚本，就下载该脚本，否则就直接执行
    - 执行完毕，控制权交还渲染引擎，恢复往下解析HTML网页

如果外部脚本加载时间很长（比如一直无法完成下载），就会造成网页长时间失去响应，浏览器就会呈现“假死”状态，这被称为“阻塞效应”。html需要等head中所有的js和css加载完成后才会开始绘制，但是html不需要等待放在body最后的js下载执行就会开始绘制,因此将js放在body的最后面，可以避免资源阻塞，同时使静态的html页面迅速显示。**将脚本文件都放在网页尾部加载**，还有一个好处,在DOM结构生成之前就调用DOM，JavaScript会报错，如果脚本都在网页尾部加载，就不存在这个问题，因为这时DOM肯定已经生成了，所以js一般都放到body元素的最后

骚操作：
chrome调慢加载,选择slow 3g
![慢动作](/images/SetSlow3g.png)

***
###  指令：v-cloak

由于js放到dom结构的最下面，所以会先出现需要js解析的插值表达式{{msg}}，然后才会出现我们的数据，为了解决这个问题，就出现了v-cloak,v-cloak 这个指令是防止页面加载时出现 vuejs 的变量名而设计的。在需要请求数据的dom接口中加入v-cload属性，在head标签中加上css样式，设置含有vi-cloak的元素不显示。

``` html

<head>
  <style>
        [v-cloak] {
            display:none;
        }
    </style>
</head>

<body>
    <div id="app">
        <p v-cloak>{{ msg }}</p>
    </div>
</body>
```

### 指令：v-text
也是绑定数据的，和插值表达式基本相同，但是由于是添加的属性，所以不会出现变量名的问题。
```html
<h1 v-text='msg'></h1>
```
还有一个区别插值表达式除了渲染里面的内容，也会展示其他的内容，而v-text则开始的时候显示非渲染的数据，当出现msg数据后，原本的数据就会被覆盖

```html
<p>++++{msg}----</p>
<h1 v-text='msg'>++++</h1>
```

### 指令v-html
v-html将要渲染的数据解析成html
``` html
    <script>
        var vm = new Vue({
            el: '#app',
            data: {
                msg: '<h1>test</h1>'
            }
        })
    </script>
```

