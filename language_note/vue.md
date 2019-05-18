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

### 指令v-bind
属性绑定
v-bind:可以缩写为:

### 指令v-on
监听DOM事件
v-on:可以缩写为@
应该支持js中的事件
``` bash
@click = "counter++"
```
click 和 tap 事件比较
二者都会在点击时触发，但是在手机WEB端，click会有200~300ms延迟。

### 样式绑定
使用v-bind:class设置一个对象，从而动态的切换class
下面的例子通过动态改变isActive和hasError的属性来动态改变div的样式，引号里面也可以是各种表达式
``` html
<div class="static"
     v-bind:class="{ active: isActive, 'text-danger': hasError }">
</div>
<script>
new Vue({
  el: '#app',
  data: {
    isActive: true,
	hasError: true
  }
})
</script>
```

#### 指令v-for
<div v-for="(items key index) in list" :key="key"></div>