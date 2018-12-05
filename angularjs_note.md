### angularjs入门
1. ng-app=" "  定义angularJS的使用范围；（在html中定义就作用于整个DOM，如果和其他框架混用，可能会出问题，这时候可以在某个div中使用）

2. ng-init="变量=值;变量='值'"  初始化变量的值，有多个变量时，中间用分号隔开；

3. ng-model="变量"  定义变量名；

4. ng-bind="变量"  绑定变量名，获取该变量的数据。这里的变量就是第3条的变量名。但是一般都用双重花括号来获取变量的值，比如：{{变量}}。

5. ng-include 指令用于包含外部的 HTML 文件，包含的内容将作为指定元素的子节点。

6.  angular.module(name,[]) 函数来创建模块，一个angularjs应用由一个或者多个模块组成
参数：name：模块定义的名称，它应该是一个唯一的必选参数，它会在后边被其他模块注入或者是在ngAPP指令中声明应用程序主模块；
    []：依赖列表，比如依赖的其他模块，也就是可以被注入到模块中的对象列表,可选参数

7. Module_name.controller():控制器定义了用于支持视图的业务逻辑，控制器位于模型和视图之间用于连接它们,
    传递给controller方法的参数是新控制器的名称和一个将会被调用的函数，用于定义控制器的功能。
    由angular.module所返回的Module对象上的controller方法创建,通常命名为<name>Ctrl

- ng-repeat 遍历,属性格式<name> in <collection>
angularjs 弹出框 $modal

$开头的变量名表示angularjs提供的内置特性。