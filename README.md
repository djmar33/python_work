# Python编程从入门到实践

本笔记记录《Python编程从入门到实践》书籍的相关笔记，因为本书会使用python3.7进行讲解，所以入手了本书，已经放弃了一本《笨方法学习python》，但是该书是使用python2.7语法讲解，导致很多命令都无法实现，卡在习题41《类》下，所以看本章节，学习python3.7看看是否从坑里爬出来。

## 第一部分 基础知识

### 1.起步

#### 1.1搭建环境

### 2.变量和简单数据类型

#### 2.1变量

```
message = "Hello Python world!"
print(message)
```

message为一个变量，每个变量都存储了一个值，在这里，存储的值为Hello Python world!。

```
message = "Hello Python World!"
print(message)

message = "Hello Python Crash Course world!"
print(message)
```

以上将会输出两行文字，程序中可以随时修改变量的值，而python将始终记录变量的最新值。

#### 2.2变量的命名和使用

1. 变量名职能包含字母、数字和下划线。可以用字母或下划线开头，但是不能使用数字开头。例如message_1，但不能为1_message。
2. 变量名不能包含空格，可以使用下划线代替。greeting_message。
3. 不要将python关键字和函数名用作变量名。例如不能使用print作为变量。
4. 变量名应简短又具有描述性。例如name，student_name。
5. 慎用小写字母l和大写字母O，因为它们可能被人错看成数字1和0。
6. 小写python变量名。

#### 2.3 使用变量时避免命名错误

程序存在错误时，解释器会提供一个traceback。traceback是一条记录，指出解释器运行代码时，在哪里遇到问题。

#### 练习

```python
feichou = "张文雅是废抽！"
print(feichou)

feichou = "废抽就是张文雅！"
print(feichou)
```



#### 2.4字符串

字符串就是一系列字符。在python中，用引号括起来的都是字符串，其中的引号可以是单引号或双引号。

```
name = "ada lovelace"
#首字母大写
print(name.title())
#全部大写
print(name.upper())
#全部小写
print(name.lower())
```

以上实例中，将ada lovelace赋值给name变量。python可对数据执行的操作，在name.title()中，name后面的句点（.）让python对变量name执行方法title（）指定操作。每个方法后面都跟着一对括号，这是因为方法通常需要额外的信息来完成其工作，如果没有额外的信息，它后面的括号是空。

title（）会以首字母大写显示变量中的值。

upper（）会以全部大写显示变量中的值。

lower（）会以全部小写显示变量中的值。

建议：无法依靠用户来提供正确的大小写，因此需要将字符串先转换为小写，在存储它们。以后需要显示这些信息时，再将它转换为最合适的大小写方式。