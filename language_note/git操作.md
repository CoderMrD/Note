创建ssh
ssh-keygen -t rsa -C "youremail@example.com"
把主页面生成的公匙粘贴到git

git init 用 Git 来对现有的项目进行管理
git clone https://github.com/xxx  克隆现有的仓库

- git add .   //全部上传
- git status  //查看文件是否添加到暂存区，掌握仓库的当前状态
- git commit -m "批注"  //添加注释，提交到仓库
- git push    //推送到远程仓库
- git diff "文件名" //比较的是工作目录中当前文件和暂存区域快照之间的差异，也就是修改之后还没有暂存起来的变化内容。
- git diff --cached  暂存起来的文件和上次提交时的快照之间的差异
- git pull：取回远程主机某个分支的更新，再与本地的指定分支合并

- git remote add origin https://xxx    关联到远程仓库

- git branch  //查看当前分支,当前分支前面会标一个*号
- git checkout -b dev // 创建dev分支，并切换到dev分支（加上-b表示创建并切换）

- git branch dev //创建分支
- git branch -d dev //删除dev分支
- git checkout dev //切换分支

- git branch -vv  // 查看本地分支对应的远程分支

- git push origin master推送到远程分支，如果没有则创建
- git log dev ^master 查看dev中有，master中没有的（暂时不会用）
- Git diff branch1 branch2 --stat   //显示出所有有差异的文件列表
- Git diff branch1 branch2 文件名(带路径)   //显示指定文件的详细差异
- Git diff branch1 branch2  //显示出所有有差异的文件的详细差异

- git branch --set-upstream-to=origin/test 当前分支关联到远程test分支


- git log //显示从最近到更远的提交日志，太多的话可以加上--pretty=oneline参数，不看详细信息
回退
- HEAD表示当前版本，HEAD^表示上一个版本，HEAD^^表示上上一个版本，HEAD~100往上100个版本
- git reset --hard commit_id返回到某个版本
- git reset --hard HEAD^ 回退到上一个版本 
向前（命令窗口还没被关掉）
- git reset --hard 1094a //版本号没必要写全，写前几位git就会自动去找
- git reflog 记录每一条命令

工作区：电脑里面能看到的目录
.git不算工作区，而是git的版本库，里面有暂存区和分支
git添加文件需要两步，git add把文件添加进去，实际上就是把文件修改添加到暂存区
git commit  提交更改，实际上就是把暂存区的所有内容提交到当前分支。
暂存区（Stage）在版本库里面

提交code流程:
	1、发起merge
	2、please熟悉的人review
	3、accept merge Request
	
合并冲突：
1. 用代码库中的文件完全覆盖本地工作版本. 
git reset --hard
git pull

本地分支关联远程分支（切换到想关联的本地分支）
git branch --set-upstream debug origin/test

merge操作，合并分支
- git merge dev 将dev分支的更改合并到当前分支（只是当前分支，并没有同步到远程分支，所以再push一下）

原始分支----目标分支（需要更新的分支)

- 删除远程仓库文件，本地保留（删除文件夹要使用-r参数）
1、git rm --cached -r 文件夹
2、git commit -m "说明"
3、git push


git fetch   运行 git fetch，可以将远程分支信息获取到本地
git checkout -b local-branchname origin/remote_branchname   将远程分支remote_branchname映射到本地命名为local-branchname 的一分支。 

在使用git命令的时候，后面可能会带有参数，有些参数前面是单横杠有些是双横杠。
下面就简单介绍一下两种横杠的使用场景。
一.单横杠短选项命令（UNIX风格）：
（1）.一个短选项命令，由横杠（-）紧跟单个短选项字符。
（2）.多个短选项命令，由横杠（-）紧跟每个短选项字符。
（3）.命令和参数之间用空格分隔。
（4）.仅作为连字符。
 eg:git commit -m "蚂蚁部落第一次提交"

二.双横杠长选项命令（GNU风格）：
（1）.长选项命令，有两个（--）紧跟长选项单词（单词不能简写）。
（2）.长选项后面跟参数，用空格或等号分隔。
eg:git log --pretty=oneline

取消暂存看提示
eg:git reset HEAD benchmarks.rb

添加中文：
使用git add添加要提交的文件的时候，如果文件名是中文，会显示形如 274\232\350\256\256\346\200\273\347\273\223.png 的乱码。 
解决方案：在bash提示符下输入： git config --global core.quotepath false

