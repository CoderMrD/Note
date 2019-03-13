Base：dojo的内核，保存于dojo.js
dojo.js包含进页面内，可以自动导入dojo的基本组件。
core: 基于base构建，对base的扩展。
dijit：依赖于core，提供了大量组件
dojox：对dojo等的扩展

dojo widget（部件，组件）:dojo.declare创建的Function对象，简单来说，就是一个dom结点
data-dojo-type:用来声明dojo widget类型

lang.hitch()指定一个上下文对象和一个函数

registry.byId 和 dom.byId 经常混淆, 尤其是初次使用者。
registry.byId 应当用于： 当你想直接引用某个部件的JavaScript对象以及访问这个部件的方法时。
dom.byId 应当用于：当你想直接访问一个DOM节点。

区分base和dojo.js???

constructor初始化dojo类的属性

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
    
dojo.addOnLoad
dojo中通过dojo.declare方法定义用于表示一个逻辑实体的声明称为类，因为js中不支持类。
dojo.require的作用就像python中的import，c中的#include,把指定的资源加载到页面以供开发人员使用。另外一个重要的特点就是对工具箱的本地安装执行同步加载，而在跨域加载工具箱时执行一步操作。