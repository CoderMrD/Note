@()创建数组
@{}创建哈希表
单双引号可以用@''@引用。
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
获取变量属性，{}中的数字表示第几个，可以传递多个
'Your host is called {0}.' -f $host.Name

Get-Content读取文本文件

Remove-Item 删除一个或多个项。由于许多提供程序都支持它，因此它可以删除多种不同类型的项，其中包括文件、目录、注册表项、变量、别名和函数。可以删除文件

Foreach 语句（也称为 Foreach 循环）是一种用于逐一遍历（循环访问）项集合中一系列值的语言
foreach ($<item> in $<collection>){<statement list>}

分割
-Split <String>
<String> -Split <Delimiter>[,<Max-substrings>[,"<Options>"]]
<String> -Split {<ScriptBlock>} [,<Max-substrings>]

-replace
    说明：替换运算符。更改值的指定元素。
    示例：
        C:\PS> "Get-Process" -replace "Get", "Stop"
        Stop-Process

Write-Output：将指定对象发送到管道中的下一个命令。如果该命令是管道中的最后一个命令，则在控制台上显示这些对象。

out-file:cmdlet 将输出发送到文件。如果需要使用它的参数，可以使用此 cmdlet 而不是重定向运算符 (>)。

Out-File [-FilePath] <string> [[-Encoding] <string>] [-Append] [-Force] [-InputObject <psobject>] [-NoClobber] [-Width <int>] [-Confirm] [-WhatIf] [<CommonParameters>]

-Append 
将输出添加到现有文件的末尾，而不替换文件内容。

-Encoding <string>
指定在文件中使用的字符编码的类型。有效值是“Unicode”、“UTF7”、“UTF8”、“UTF32”、“ASCII”、“BigEndianUnicode”、“Default”和“OEM”。默认值为“Unicode”。

“Default”使用系统当前 ANSI 代码页的编码。

“OEM”使用操作系统的当前原始设备制造商代码页标识符。


Split-Path Split-Path cmdlet 仅返回路径的指定部分，如父目录、子目录或文件名。它还显示拆分路径所引用的项，并指示该路径是相对路径还是绝对路径。
使用此 cmdlet 可以只显示或只提交路径的选定部分。

-Parent 
只返回路径所指定的项或容器的父容器。例如，在路径“C:\Test\Logs\Pass1.log”中，该命令返回“C:\Test\Logs”。Parent 参数是默认的拆分位置参数。

et-ExecutionPolicy 可更改 Windows PowerShell 执行策略的用户首选项。
参数：
Unrestricted：加载所有配置文件并运行所有脚本





