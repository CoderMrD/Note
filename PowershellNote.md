@()创建数组
@{}创建哈希表
eg：$target = @{
"CPU"             ="Lenovo.HardwareMgmtPack.IMM2.ManagementModule";
}
$target["CPU"]

在哈希表中存储数组
可以在创建哈希表时就使用数组，因为创建数组和哈希表的的元素关键字不冲突。一个是逗号，一个是分号。
$stu=@{ Name = "小明";Age="12";sex="男";Books="三国演义","围城","哈姆雷特" }

字符串函数
IndexOf()	返回第一次匹配的所索引	(“Hello”).IndexOf(“l”)
匹配到返回0，匹配不到返回-1

Powershell使用-F方法带入数据
封闭在双引号中的字符串能够直接使用变量，这是常用的手法，但是只能获取变量本身而不能获取变量属性
$name = $host.Name
"Your host is called $name."
获取变量属性
'Your host is called {0}.' -f $host.Name
