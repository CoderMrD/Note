Base：dojo的内核，保存于dojo.js
dojo.js包含进页面内，可以自动导入dojo的基本组件。

dojo widget:简单来说，就是一个dom结点
data-dojo-type:用来声明dojo widget类型

lang.hitch()指定一个上下文对象和一个函数

registry.byId 和 dom.byId 经常混淆, 尤其是初次使用者。
registry.byId 应当用于： 当你想直接引用某个部件的JavaScript对象以及访问这个部件的方法时。
dom.byId 应当用于：当你想直接访问一个DOM节点。

区分base和dojo.js???

constructor初始化dojo类的属性

dojo中通过dojo.declare方法定义用于表示一个逻辑实体的声明称为类，因为js中不支持类。
dojo部件（widget）就是由dojo.declare语句创建的function对象

dojo.require的作用就像python中的import，c中的#include,把指定的资源加载到页面以供开发人员使用。另外一个重要的特点就是对工具箱的本地安装执行同步加载，而在跨域加载工具箱时执行一步操作。

dojo.byid("id").innerHTML返回中间的内容，如果有多个这个id的，就返回第一个

dojo.connect
====================================
connect(/*Object|null*/ obj,
        /*String*/ event,
        /*Object|null*/ context,
        /*String|Function*/ method) // Returns a connection handle
    
    
====================================
//连接鼠标事件，鼠标移入s1节点，console.log显示内容
var handle = dojo.connect(
  dojo.byId("s1"), //context
  "onmouseover", //event(鼠标移入事件)
  null, //context
  function(evt) {console.log("mouseover event", evt);} //event
);
//断开连接
dojo.disconnect(handle);
    

	
js 

console.dir()可以显示一个对象所有的属性和方法
console.trace()用来追踪函数的调用轨迹。
console.time()和console.timeEnd()用来显示代码的运行时间,在小括号中加上相同的字符串（名字）即可。

js对象都继承自object类型，并且有一个prototype属性
JavaScript prototype 属性使您有能力向对象添加属性和方法。

闭包本质上是数据与封闭数据的作用域的结合体，js有作用域链。
环境：基于浏览器的js中默认的this环境是全局windows对象。对于Function对象而言，关键字this则多用于其直接环境。
js可以像传递其他数据类型一样传递function对象，虽然在代码中使用匿名函数绝对能减少混乱和提高易维护性，但匿名函数的一个更重要的特性还是作为保护直接环境的闭包使用。
js不支持函数外部的块级作用域，无论是i的值还是在循环过程或者条件逻辑中定义的任何“临时”变量，都会在其所在的块执行后继续存在。

//变量i未定义
for (var i=0; i < 10; i++){
	//对i进行操作
}
console.log(i);//i不是undefine
如果有必要明确的提供一个块级作用域，那么可以把这个块包含在一个Funciton对象中，并在代码中调用该Function对象。
(function(){
	for (var i=0; i<10; i++){
	//对i进行操作
	}
})()
console.log(i);//undefine
这样可以把可能的冲突因素隔离开来，为执行的代码提供了闭包。

appendChild() 方法可向节点的子节点列表的末尾添加新的子节点。
document.getElementById("myList").appendChild(newListItem);

onload事件会在页面或图像加载完成后立即发生
养成使用dojo.addOnLoad的习惯，可以跨域加载

命名空间是为了解决相同作用域下的命名问题。