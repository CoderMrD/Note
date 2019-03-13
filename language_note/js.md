	
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