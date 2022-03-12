# **Linux上整体迁移Anaconda环境并授权所有子用户访问**

原文：[传送门](https://blog.csdn.net/weixin_41010198/article/details/106833121)

# 1 问题描述

由于一开始把anaconda安装到了：`/HDD/anaconda3`路径下，但是后面由于/HDD空间不足，所有就需要把anaconda整体迁移，这样就可以保住以前安装的库包，虚拟环境等，否则一切都要重头再来，太麻烦了！！！

把anaconda整体从`/HDD/anaconda3/`移动到`/home/`路径下

# 2 Linux上整体迁移Anaconda过程

## 2.1 移动anaconda文件到新的路径

移动anaconda文件到新的路径下`mv /home/anaconda3 /home`

```powershell
(base) [root@localhost /home]$ ls
anaconda3  project  shl  tools  xcd  zhangq
```

## 2.2 修改Anaconda的环境变量

- 打开`.bashrc`配置文件，`vi root/.bashrc` 或 `vi ~/.bashrc`
    - 修改前：
        
        ```python
        # >>> conda initialize >>>
        # !! Contents within this block are managed by 'conda init' !!
        __conda_setup="$('/HDD/anaconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
        if [ $? -eq 0 ]; then
            eval "$__conda_setup"
        else
            if [ -f "/HDD/anaconda3/etc/profile.d/conda.sh" ]; then
                . "/HDD/anaconda3/etc/profile.d/conda.sh"
            else
                export PATH="/HDD/anaconda3/bin:/usr/local/gcc/bin$PATH"
            fi
        fi
        unset __conda_setup
        # <<< conda initialize <<<
        ```
        
    - 修改后：
        
        一共修改四处，主要修改就是有关anaconda的一些环境变量的路径
        
        ```python
        # >>> conda initialize >>>
        # !! Contents within this block are managed by 'conda init' !!
        __conda_setup="$('/home/anaconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
        if [ $? -eq 0 ]; then
            eval "$__conda_setup"
        else
            if [ -f "/home/anaconda3/etc/profile.d/conda.sh" ]; then
                . "/home/anaconda3/etc/profile.d/conda.sh"
            else
                export PATH="/home/anaconda3/bin:/usr/local/gcc/bin$PATH"
            fi
        fi
        unset __conda_setup
        # <<< conda initialize <<<
        ```
        
- 让修改后的环境变量生效`source ~/.bashrc`

## 2.3 修改可执行文件conda

1. 打开conda配置文件
    
    ```powershell
    vi /home/anaconda3/bin/conda
    ```
    
2. 修改conda文件
    
    把conda第一行的路径修改成如下：
    
    - 修改前：`#!/HDD/anaconda3/bin/python`
    - 修改后：`#!/home/anaconda3/bin/python`
    
    此时在命令行中输入conda，就会显示一些命令参数的！
    
    注意：如果输入conda显示没有该命令，则重新打开一个终端再试一下
    

## 2.4 修改可执行文件pip

修改可执行文件pip之后，pip和python才可用。没有修改前，如果使用pip会报如下错误：

```powershell
(base) [root@localhost /home/anaconda3/envs/mmdetection/bin]$ pip -V
-bash: /home/anaconda3/bin/pip: /HDD/anaconda3/bin/python: 坏的解释器: 没有那个文件或目录
```

1. 打开pip配置文件 `vi /home/anaconda3/bin/pip`
2. 修改pip文件
    
    把pip第一行的路径修改成如下：
    
    - 修改前：`#!/HDD/anaconda3/bin/python`
    - 修改后：`#!/home/anaconda3/bin/python`

## 2.5 修改虚拟环境中的可执行文件pip

修改虚拟环境下的可执行文件pip之后，进入虚拟环境后pip和python才可用。没有修改前，如果在虚拟环境中使用pip会报如下错误（我的虚拟环境是`mmdetection`）：

```powershell
(mmdetection) [root@localhost /home/project/mmdetection_hat]$ pip -V
-bash: /home/anaconda3/envs/mmdetection/bin/pip: /HDD/anaconda3/envs/mmdetection/bin/python: 坏的解释器: 没有那个文件或 目录
```

1. 打开pip配置文件`vi //home/anaconda3/envs/mmdetection/bin/pip`
2. 修改pip文件
    
    把pip第一行的路径修改成如下：
    
    - 修改前：`/HDD/anaconda3/envs/mmdetection/bin/python`
    - 修改后：`/home/anaconda3/envs/mmdetection/bin/python`

# 3 让Linux的子用户共享root用户的Anaconda环境

上面我们已经知道root用户下，anaconda的很多环境变量都是在`root/.bashrc`（或`~/.bashrc` 是同一个文件）配置文件中定义的，如果要让子用户能够共享到root用户下的anaconda所有环境（包括虚拟环境），就必须让子用户能够访问到`/root/.bashrc`中定义的anaconda的环境变量，所以我们把`/root/.bashrc`拷贝到子用户的home目录下，覆盖子用户的`.bashrc`配置文件。

## 3.1 拷贝root用户的`.bashrc`配置文件，并覆盖子用户`/home/子用户名/.bashrc`配置文件

例如，我想要子用户shl可以使用root用户下的anaconda环境：

1、拷贝root用户的`.bashrc`配置文件，并覆盖子用户`/home/子用户名/.bashrc`配置文件

`cp /root/.bashrc /home/shl/.bashrc`

## 3.2 让子用户可以在root用户的anaconda下新建虚拟环境

如果要让子用户可以在root用户的anaconda下新建虚拟环境，就必须让子用户对anaconda的安装路径`/home/anaconda3`有读写执行的权利，因此只要赋予子用户对`/home/anaconda3`权利即可。

例如：赋予用户shl对`/home/anaconda3` 读写执行权利：`chown -R shl:shl /home/anaconda3`

**注意：**以上操作都是在root用户下操作的，否则你没有权限