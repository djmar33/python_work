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

##### 程序存在错误时，解释器会提供一个traceback。traceback是一条记录，指出解释器运行代码时，在哪里遇到问题。

##### 练习

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

**建议**：无法依靠用户来提供正确的大小写，因此需要将字符串先转换为小写，在存储它们。以后需要显示这些信息时，再将它转换为最合适的大小写方式。

##### 合并字符串

python使用（+）来合并字符串

```
first_name = "ada"
last_name = "loveace"
full_name = first_name + " " + last_name
print(full_name)
```

##### 制表符和换行操作

```python3
fater_name = "tom"
mother_name = "kirs"
baby_name = "jerry"
print("Hello, My family members have\n\t" + fater_name.title() + ","
      + mother_name.title() + "," + baby_name.title())
```

`\n为换行`

`\t制表符`

##### 删除空白

```
fater_name = "     tom"
mother_name = "kirs "
baby_name = " jerry "

#删除左边空格
print(fater_name.lstrip())
#删除右边空格
print(mother_name.rstrip())
#删除前后空格
print(baby_name.strip())

```

lstrip()：删除左边空格

rstrip（）：删除右边空格

strip（）：删除左右空格

##### 练习

```
#2-3个性化消息
name = "Eric"
print("Hello " + name + ",would you like to learn some Python today?")


#2-4调整名字大小写
name = "zhang wen ya shi fei chou"
print(name.title())

#2-5名言
name = "废抽"
say = "东西我来洗"
print(name + ":" + "\"" + say + "\"")

#2-6名言2
famous_person = "废抽"
say = "帮我拿毛巾我就去洗澡"
print(name + ":" + "\"" + say + "\"")

#2-7剔除人名中的空白
famous_person = " 废抽 "

print(famous_person.lstrip())
print(famous_person.rstrip())
print(famous_person.strip())
```

#### 2.5数字

##### 整数

整数运算加减乘除，乘方运算。python支持运算次序，也可以使用括号改变运算次序。

```
2 + 3
3 - 2
2 * 3
10 / 2
2 ** 3
（2 + 3）* 4
```

##### 浮点数

带小数点的数字都称为浮点数。

```
0.2 + 0.1
```

##### str()函数避免错误

```
age = 23
message = " Happy " + str(age) + "rd Birthday!"
print(message)
```

因age为int整数类型，而赋值给message时候，包含""，python无法判断该值为int还是str，所以如果不加str将age改为字符串，python将会报错。

##### 练习

```
#练习2-8
#加减乘除，乘方；
print(5 + 3)
print(18 - 10)
print(2 * 4)
print(32 / 4)
print(2 **3 )


#练习2-9
number = 4
message = "我最喜欢的数字为" + str(number) + "啊！"
print(message)

```

#### 2.6注释

python中，注释用井号（#）标识。井号后面的内容都会被python解释器忽略。

```
#2-10添加注释练习
#程序编程要养成习惯，有思路解决方法，就立刻在代码中填写注释；

#创建一个浩哥
haoge = "Jerry"
#输出浩哥
print(haoge)
```

#### Python之禅

在python解释器里运行import this，将会输出python之禅。

The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!

------

Python之禅 by Tim Peters

优美胜于丑陋（Python 以编写优美的代码为目标）
明了胜于晦涩（优美的代码应当是明了的，命名规范，风格相似）
简洁胜于复杂（优美的代码应当是简洁的，不要有复杂的内部实现）
复杂胜于凌乱（如果复杂不可避免，那代码间也不能有难懂的关系，要保持接口简洁）
扁平胜于嵌套（优美的代码应当是扁平的，不能有太多的嵌套）
间隔胜于紧凑（优美的代码有适当的间隔，不要奢望一行代码解决问题）
可读性很重要（优美的代码是可读的）
即便假借特例的实用性之名，也不可违背这些规则（这些规则至高无上）

不要包容所有错误，除非你确定需要这样做（精准地捕获异常，不写 except:pass 风格的代码）

当存在多种可能，不要尝试去猜测
而是尽量找一种，最好是唯一一种明显的解决方案（如果不确定，就用穷举法）
虽然这并不容易，因为你不是 Python 之父（这里的 Dutch 是指 Guido ）

做也许好过不做，但不假思索就动手还不如不做（动手之前要细思量）

如果你无法向人描述你的方案，那肯定不是一个好方案；反之亦然（方案测评标准）

命名空间是一种绝妙的理念，我们应当多加利用（倡导与号召）

#### 小结

1. 如何使用变量；
2. 如何创建描述性变量以及如何消除名称错误的语法错误；
3. 字符串是什么；
4. 如何使用小写、大写和首字母大写方式显示字符串；
5. 使用空白来显示整洁的输出，以及如何剔除字符串多余的空白；
6. 如何使用整数和浮点数；
7. 如何编写说明性注释，让代码更容易理解；
8. 了解了让代码尽可能简单的概念；



### 3.列表

列表由一系列按特定顺序排列的元素组成。可以创建包含字母、数字的列表。元素之间可以没有任何关系。

python中，用方括号（[]）来表示列表，并用逗号分隔其中的元素。

```
#3.1 列表用[]括号，如果直接使用print输出列表，或将[]也输出；
family = ['爸爸','浩哥','妈妈']
print(family)
```

#### 访问列表元素

```
#在列表增加索引，索引是从0开始，如果要访问的元素位置减一，就是当前元素的索引位置；
print(family[0])
#返回倒数最后一个元素；
print(family[-1])
```

#### 使用列表中的各个值

```
message = "My first bicycle was a " + family[0].title() + "."
print(message)
```

##### 练习

```
#3-1姓名：
#创建一个列表
names = ['tom','jerry','kirs']
#输出列表第一个元素；
print(names[0].title())
#输出列表第二个元素；
print(names[1].title())
#输出列表第三个元素；
print(names[2].title())


#3-2问候语
print("Hello," + names[0].title() + "!")
print("Hello," + names[1].title() + "!")
print("Hello," + names[2].title() + "!")


#3-3自己的列表
motorcycle = ['本田','丰田','奔驰']
message = "I would like to own a " + motorcycle[0].title() + "motorcycle."
print(message)
```

#### 修改、添加和删除元素

创建的大多数列表都将是动态的，这意味着列表创建后，将随着程序的运行增删元素。

##### 修改元素列表

```
#修改列表元素
family = ['baba','haohao','chouchou']
print(family)

family[0] = 'tom'
print(family)
```

##### 添加元素

使用append（）函数，可以在列表末尾添加元素。一般会创建一个空列表，然后进行添加相关元素。

```
#append()会在列表末尾添加元素
family.append('mama')
print(family)
```

##### 列表中插入元素

```
#列表中插入元素,insert（）
#在列表中第二个元素添加yeye这个元素；
family.insert(1,'yeye')
print(family)
```

##### 列表中删除元素

```
#列表中删除元素,使用del语句
#删除列表中第二个元素；
#del语句可以删除任何位置处的列表元素，但前提条件是知道索引位置；
del family[1]
```

##### 使用pop（）删除元素

```
#使用pop()删除元素
#pop()删除列表末尾的元素，并让你能够接着使用该元素。
#列表就像一个栈，而删除列表末尾的元素相当于弹出栈顶元素。
popend_family = family.pop()
print(family)
print(popend_family)
```

##### 弹出列表中任何位置处的元素

```
#弹出列表中任何位置处的元素
first_popend = family.pop(0)
print(first_popend)
```

如果要从列表中删除一个元素，且不再以任何方式使用它，就是用del语句；

如果要在删除元素后还能继续使用它，就是用方法pop（）；

##### 根据值删除元素

如果不知道需要删除元素的索引位置，只知道删除元素的值，可以使用remove()；remove从列表删除的元素，也可以像pop（）一样接着使用，一般用来提示列表元素删除原因；

```
#根据值删除元素,remove()
family.remove('chouchou')
print(family)


#remove()删除值接着使用，一般用来提示删除信息
del_family = 'tom'
family.remove(del_family)
print(family)
print("这个元素" + del_family.title() + "已被删除！")
```

remove()只删除第一个指定的值，如果列表中该值重复多次，需要循环来判断是否删除所有这样的值。

##### 练习

```
#练习3-4
#邀约嘉宾名单

danner_names = ['爸爸','妈妈','爷爷','奶奶','婆婆','公公']

print(danner_names[0] + "," + "明天一起吃饭咯！")
print(danner_names[1] + "," + "明天一起吃饭咯！")
print(danner_names[2] + "," + "明天一起吃饭咯！")
print(danner_names[3] + "," + "明天一起吃饭咯！")
print(danner_names[4] + "," + "明天一起吃饭咯！")
print(danner_names[5] + "," + "明天一起吃饭咯！\n\n\n\n")

#修改嘉宾名单

busy_names = danner_names[0]
print(busy_names + "明天没空来不了啊，你们吃吧！\n")
danner_names[0] = "三姑奶"
print(danner_names[0] + "," + "明天一起吃饭咯！")
print(danner_names[1] + "," + "明天一起吃饭咯！")
print(danner_names[2] + "," + "明天一起吃饭咯！")
print(danner_names[3] + "," + "明天一起吃饭咯！")
print(danner_names[4] + "," + "明天一起吃饭咯！")
print(danner_names[5] + "," + "明天一起吃饭咯！\n\n\n\n")


#添加嘉宾
print("我买了张大圆桌，大家都过来吃饭吧！\n")
danner_names.insert(0,"姨仔")
danner_names.insert(3,"妹妹")
danner_names.append("洪梓峰")
print(danner_names[0] + "," + "明天一起吃饭咯！")
print(danner_names[1] + "," + "明天一起吃饭咯！")
print(danner_names[2] + "," + "明天一起吃饭咯！")
print(danner_names[3] + "," + "明天一起吃饭咯！")
print(danner_names[4] + "," + "明天一起吃饭咯！")
print(danner_names[5] + "," + "明天一起吃饭咯！")
print(danner_names[6] + "," + "明天一起吃饭咯！")
print(danner_names[7] + "," + "明天一起吃饭咯！")
print(danner_names[8] + "," + "明天一起吃饭咯！\n\n\n\n")


#缩减名单
print("不好意思，剧情需求，餐桌无法到达，只能两个人参与盛宴！\n")
lower_names = danner_names.pop()
print(lower_names + "不好意思啊，不能一起吃饭啦。")
lower_names = danner_names.pop()
print(lower_names + "不好意思啊，不能一起吃饭啦。")
lower_names = danner_names.pop()
print(lower_names + "不好意思啊，不能一起吃饭啦。")
lower_names = danner_names.pop()
print(lower_names + "不好意思啊，不能一起吃饭啦。")
lower_names = danner_names.pop()
print(lower_names + "不好意思啊，不能一起吃饭啦。")
lower_names = danner_names.pop()
print(lower_names + "不好意思啊，不能一起吃饭啦。")
lower_names = danner_names.pop()
print(lower_names + "不好意思啊，不能一起吃饭啦。")
print(danner_names[0] + "," + "你还是受邀约任务，一起吃饭！")
print(danner_names[1] + "," + "你还是受邀约任务，一起吃饭！")
del danner_names[0]
del danner_names[0]
print(danner_names)
```

#### 3.3组织列表

##### sort()排序

对列表按字母顺序排序的，在也无法恢复原来的排列顺序，但是前提是都是英文小写才能实现。

```
#sort()排序
cars = ['bmw','audi','toyota','subaru']
cars.sort()
print(cars)
```

sort()反向排序，只需要向sort()方法传递参数reverse=True。同样排序也是永久性的，无法恢复原来的排列顺序。

```
#sort()反向排序，传递参数reverse=True

cars = ['bmw','audi','toyota','subaru']
cars.sort(reverse=True)
print(cars)

```

##### sorted()排序

sorted()会保留列表元素原来的排列顺序，同时以特定顺序呈现它们。

```
#sorted()临时排序，并不影响原列表顺序；
cars = ['bmw','audi','toyota','subaru']
print("这是没排序前的列表：\n",cars)
print("这是排序后的列表：\n",sorted(cars))
```

sorted()也可以反向排序，和sort()一样，传递reverse=True即可。

```
#sorted()临时反向排序，传递参数reverse=True
cars = ['bmw','audi','toyota','subaru']
print("这是没排序前的列表：\n",cars)
print("这是排序后的列表：\n",sorted(cars,reverse=True))
```

##### reverse()排序

reverse()可反转列表元素的排列顺序。和sort(reverse=True)区别在于，reverse()是反转列表元素排列，而不是按字母反向排序。方法reverse()也是永久性地修改列表排序，如果想恢复排列顺序，再执行多次reverse()排序即可。

```
#reverse()反向排序
cars = ['bmw','audi','toyota','subaru']
print("这是没排序前的列表：\n",cars)
cars.reverse()
print("这是使用reverse()排序后的列表\n",cars)
```

##### len()列表长度

len()函数快速获悉列表的长度。计算列表元素是从1开始，这里不像索引需要从0开始，切记！

```
#len()列表长度
cars = ['bmw','audi','toyota','subaru']
print("列表长度为：",len(cars))
```

##### 练习

```
#3-8放眼看世界

world = ['japan','laos','hongkong','thailand','malaysia']
print("这是我想去的5个国家：\n",world)

#使用sorted()按字母排序
print("使用sorted()函数按字母排序：\n",sorted(world))
print("使用sorted()函数只会临时排序，不影响原始列表元素：\n",world)

#使用sorted()反向排序
print("使用sorted()反向排序：\n",sorted(world,reverse=True))
print("同样也不会影响原来列表顺序：\n",world)

#使用reverse()反向排序
world.reverse()
print("使用reverse()反向排序：\n",world)

#再次使用reverse()反向排序，将恢复默认列表顺序
world.reverse()
print("再次使用reverse()，恢复默认顺序：\n",world)

#使用sort()排序
world.sort()
print("使用sort()函数排序：\n",world)

#使用sort()反向排序
world.sort(reverse=True)
print("使用sort()反向函数排序：\n",world)

#3-9晚餐使用len()长度函数
danner_names = ['废抽','浩哥','爸爸']
print("总共" + str(len(danner_names)) + "人吃晚餐")

#3-10练习本章函数排序
english = ['z','s','e','x','b','o']
print("默认排序：\n",english)

#sortend()
print("sorted()：\n",sorted(english))

#sorted()反向
print("sorted()：\n",sorted(english,reverse=True))

#reverse()
english.reverse()
print("revers()：\n",english)

#reverse()恢复
english.reverse()
print("再次revers(),恢复顺序：\n",english)

#sort()
english.sort()
print("sort()：\n",english)

#sort()反向
english.sort(reverse=True)
print("sort()反向：\n",english)
```

##### 避免列表错误

发生索引错误却找不到解决办法，可以使用len（）显示列表长度，因为列表可能与你以为的截然不同；

列表最后一个值建议使用[-1]，除非列表为空才会出现报错；

#### 小结

1. 列表是什么？family = ['爸爸','妈妈','粉肠']
2. 如果使用列表？ family[0]
3. 如何增删元素？append（），insert()，del 、pop（）
4. 如何对列表永久性排序？sort(),reverse()
5. 如何对列表临时排序？sorted()
6. 如何确定列表长度？len()

### 4.操作列表

#### for语句

可以遍历列表的所有元素，对每个元素执行相同的操作。

for语句注意事项：

1. for语句后面有冒号结尾；
2. for语句里代码需要缩进，一般是4个空格；
3. 不在循环范围内的代码不需要缩进；

```
#4-1披萨
pizzas = ['奥尔良','牛肉','榴莲']
for pizza in pizzas:
    print("我喜欢吃的" + pizza + "披萨.\n")

print("我就是喜欢吃pizza!")


#4-2动物
aniamls = ['dog','cat','cow']
for aniaml in aniamls:
    print("A " + aniaml.title() + " would make a great pet.")
print("Any of these animals would make a great pet!")

```

#### range()函数

range（）能够轻松地生成一系列的数字。

```
#4.3.1 range()函数使用

#打印一系列数字，range函数里1,5，表示生成1-4范围的数字，并不会打印数字5；
for value in range(1,5):
    print(value)
```

##### 创建数字列表

使用list（）将range（）的结果直接转为列表。

```
#4.3.2 创建数字列表
number = list(range(1,5))
print(number)
```

##### 指定步长

range（2,11,2），range（）函数从2开始，然后不断增加2，直到达到或超过最终值11。后面数字2是递增数。

```
#指定步长,生成10以下的偶数列表
number = list(range(2,11,2))
print(number)
```

使用range计算1~10平方数

```
#创建1~10的平方
#创建一个空列表，便于等下存储平方数结果；
squares = []
#使用for循环，遍历1-11（就是1-10）
for value in range(1,11):
    #求value的平方值，并且赋值给square
    square = value ** 2
    #将每个计算平方的值square，添加到squares列表中
    squares.append(square)
#输出列表
print(squares)
```

更简洁方法计算1~10平方数

```
squares = []
for value in range(1,11):
    squares.append(value ** 2)
print(squares)
```

##### 列表统计计算

```
#4.3.3列表统计

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
#列表中最小的数
print(min(digits))
#列表中最大的数
print(max(digits))
#列表中所有数之和
print(sum(digits))
#列表长度
print(len(digits))
```

##### 列表解析  

```
#4.3.4列表解析

squares = [value ** 2 for value in range(1,11)]
print(squares)
```

讲解顺序：

1. 指定一个描述性的列表名，squares；
2. 定义一个表达式，value ** 2；
3. 编写一个for循环，用于给表达式提供值；
4. for value in range(1,11)，它将1~10的值提供给表达式value**2；
5. 这里的for循环是没有冒号的；
6. 可以节约三四行代码来生成列表；

##### 练习

```
#4-3数到20
for value in range(1,21):
    print(value)

#4-4一百万，数太大了，无法运行改成100；
number = list(range(1,101))
print(number)
#4-5计算1~100最大的数，最小的数，1~100求和
number = list(range(1,101))
print(max(number))
print(min(number))
print(sum(number))

#4-6奇数
odd_number = []
for value in range(1,21,2):
    odd_number.append(value)
print(odd_number)

#4-7 3的倍数
number = []
for value in range(3,31,3):
    number.append(value)
print(number)

#4-8 立方
squares = []
for value in range(1,11):
    squares.append(value ** 3)
print(squares)

#4-9 立方解析
squares = [ value ** 3 for value in range(1,11)]
print(squares)
```

#### 切片

处理列表部分元素或所有元素，python称为切片。

```
#4.4.1切片使用

players = ['charles','martina','michael','florence','eli']
#players[0:3]，表示从索引0开始，分别输出0,1,2三个元素。
#若要使用最后一个元素，索引需要加1；与range()一样。但是切片索引还是从0开始；
print(players[0:3])

#索引从头开始,可以不需要指定第一个索引
print(players[:3])

#索引直到最后，可以不需要指定最后一个索引
print(players[2:])

#导出列表倒数第三个元素，无论列表怎么变化，都只会导出倒数第三个数；
print(players[-3:])
```

##### 遍历切片

```
#4.4.2遍历切片
#使用遍历，输出列表前三名球员；
players = ['charles','martina','michael','florence','eli']
print("Here are the fist three players on my team:")
for player in players[0:4]:
    print(player.title())

```

##### 复制列表

```
#4.4.3复制列表
my_foods = ['叉烧','烧鸭','排骨','鸡翅']
#使用切片，将列表复制给firend_foods
firend_foods = my_foods[:]
print("这是我喜欢的食物：\n",my_foods)
print("这是我朋友喜欢的食物：\n",firend_foods)


#与变量赋值不一样
#我们修改一下两个列表，然后输出相关的值，发现他们互不影响
my_foods.append('汉堡')
firend_foods.append('榴莲')
print("这是我喜欢的食物：\n",my_foods)
print("这是我朋友喜欢的食物：\n",firend_foods)


#若使用变量赋值
firend_foods = my_foods
my_foods.append('西瓜')
firend_foods.append('苹果')
#发现输出的值都会一样。
print("这是我喜欢的食物：\n",my_foods)
print("这是我朋友喜欢的食物：\n",firend_foods)
```

##### 练习

```
#练习2
#4-10切片
my_foods = ['叉烧','烧鸭','排骨','鸡翅']
print("The first three items in the list are:\n")
print(my_foods[0:3])

print("Three items from the middle of the list are:\n")
print(my_foods[1:3])

print("The last three items in the list are:\n")
print(my_foods[-3:])


#4-11你的比萨和我的比萨
my_pizzas = ['榴莲','奥尔良','海鲜','牛肉','香菇']
firend_pizzas = my_pizzas[:]
my_pizzas.append('青菜')
firend_pizzas.append('木耳')
print("我喜欢的pizza:\n",my_pizzas)
print("我朋友喜欢的pizza:\n",firend_pizzas)

#4-12使用两个for导出pizza
for my_pizza in my_pizzas[:]:
    print("我喜欢的pizza有",my_pizza)
for firend_pizza in firend_pizzas[:]:
    print("我朋友喜欢的pizza有",firend_pizza)

```

#### 元组

python将不能修改的值称为不可变的，而不不可变的列表称为元组。

##### 定义元组

元组看起来犹如列表，但使用的是圆括号而不是方括号。定义元组后，可以使用索引来访问其元素，像访问列表一样。

##### 遍历元组的所有值

元组也可以像列表一样使用for循环遍历每个元素。

```
foods = ('烧鸡','咸鱼肉饼','酱油鸭','白切鸡','鳄鱼汤')

#使用for遍历元组

for food in foods:
    print(food)
```



##### 修改元组元素的值

元组定以后就无法修改，除非重新赋值。

```
foods = ('烧鸡','咸鱼肉饼','酱油鸭','白切鸡','鳄鱼汤')
#可重新赋值
foods = ('米饭')
```



##### 练习

```
#练习3
#4-13自助餐

foods = ('烧鸡','咸鱼肉饼','酱油鸭','白切鸡','鳄鱼汤')

#使用for遍历元组

for food in foods:
    print("旧食物：\n",food)
print(foods)

#修改元组元素，重新赋值

foods = ('叉烧','烧鹅','小炒肉','粉肠','粿条')

for food in foods[:]:
    print("新食物：\n",food)
print(foods)
```

##### 设置代码格式

1. 格式指南；PEP8(python enhancement proposal)
2. 缩进；使用4个空格缩进。
3. 行长；每行不超过80字符。
4. 空行；增加代码可读性，适当使用空行来区分代码块。执行代码不会考虑空行。

##### 小结

1. 如何高效处理列表中的元素；
2. 如何使用for循环遍历列表；
3. 如何使用缩进来确定程序结构；
4. 如何创建简单数字列表；
5. 如何通过切片使用列表和复制列表；
6. 元组操作和使用；
7. 代码格式指南；

### 5 .if语句

if语句让你能够检查程序当前状态，并据此采取相应措施。

#### 简单示例

```
#5.1 if语句实例，判断列表中bmw如果是小写，就执行首字母大写输出；

cars = ['audi','bmw','subaru','toyota']

for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())
```

if语句核心都是一个值True或False。如果条件为True时，将输出if语句里的代码，否则忽略if里的代码。

##### 检查符号

1. 比较两个值是否相同；==
2. 比较两个值是否不相同；！=
3. 检查多个条件，但是两个都必须满足才为True；and
4. 检查多个条件，但是其中一个条件满足就为True；or
5. 检查元素是否包含在列表里；in   例： `'bmw' in cars `
6. 检查元素是否不包含在列表里； not in 例：`'plane' not in cars`

##### 布尔表达式

条件测试的别名，与条件表达式一样，结果要么是True或False。

##### 练习

```
#5-2更多条件测试
#检查两个字符串相等和不等
#False
print("feichou" == "feichou2")
#True
print("feichou" == "feichou")

#lower测试
a = "FEICHOU"
print(a.lower() == "feichou")

#and，只要一个为False就是False

print("结果：",True and False )
print("结果：",True and True ,"\n")

#or,只要一个为True就是True
print("结果：",True or False )
print("结果：",False or False,"\n")

#in语句判断
mama = "废抽"
print("废在妈妈名字里:\n",'废' in mama)

#not in 语句判断
mama = "废抽"
print("废在妈妈名字里:\n",'废' not in mama)
```

#### if-else语句

判断条件测试通过执行一个操作，若没有通过，将执行另外一个操作。

##### 简单示例

```
#5.3.2 if-else语句
age = 17
if age >= 18:
	print("你年龄满足投票。")
	print("你登记投票了吗？")
else:
	print("你年龄未满足投票资格啊，小弟弟！")

```

#### if-elif-else语句

依次检查每个条件，否则将执行else操作。

##### 简单示例

```
#5.3.3 if-elif-else语句
age = 12

if age < 4:
	price = 0
elif age < 18:
	price = 5
else:
	price = 10
print("Your admission cost is $" + str(price) + "元.")
```

#### 多个elif语句

##### 简单示例

```
#5.3.4 多个elif语句
age = 70

if age < 4:
	price = 0
elif age < 18:
	price = 5
elif age < 64:
	price = 10
else:
	price = 0
print("Your admission cost is $" + str(price) + "元.")
```

#### 省略else

python并不要求if-elif语句里一定要包含else，有时候去掉else，判断语句将会更清晰。

##### 简单示例

```
#5.3.5 省略else语句
age = 64

if age < 4:
	price = 0
elif age < 18:
	price = 5
elif age < 64:
	price = 10
elif age >= 64:
	price = 0
print("Your admission cost is $" + str(price) + "元.")
```

#### 测试多个条件

一般if-elif语句，都只能满足一个条件，然后执行对应的代码。但是如果需要判断每一个元素的时候，就需要使用多个if语句结构来判断。

#### 练习

```
#练习
#5-3外星人颜色
alien_color = 'green'
if alien_color == 'green':
	print("获得5个点。")

alien_color = 'yellow'
if alien_color == 'green':
	print("获得5个点。")

alien_color = 'red'
if alien_color == 'green':
	print("获得5个点。")

#5-4外星人颜色2
alien_color = 'green'
if alien_color == 'green':
	print("获得5个点。")
else:
	print("获得10个点。")

#5-5外星人颜色3
alien_color = input("""
	input Color green,red,yellow\n>""")
if alien_color.lower() == 'green':
	print("获得5个点。")
elif alien_color.lower() == 'yellow':
	print("获得10个点。")
else:
	print("获得15个点。")

#5-6人生的不同阶段
age = input("请输入你的年龄：\n")
if int(age) < 2:
	print("你是个小BB哦！")
elif int(age) < 4:
	print("你正在蹒跚学步！")
elif int(age) < 13:
	print("你是一位儿童哦！")
elif int(age) < 20:
	print("你是一位青年！")
elif int(age) < 65:
	print("你是一位成年人！")
else:
	print("你是一位老人！")

#5-7喜欢的水果
favorite_fruits = ['香蕉','榴莲','西瓜']
if '香蕉' in favorite_fruits:
	print("你喜欢香蕉")

if '榴莲' in favorite_fruits:
	print("你喜欢榴莲")

if '苹果' in favorite_fruits:
	print("你喜欢苹果")
```

##### 使用if语句处理列表

###### 简单示例

```
#5.4.1
#创建一个列表，列表里包含相关配菜；
requested_toppings = ['mushrooms','green peppers','extra cheese']

#使用for循环，遍历这个列表每个元素；
for requested_topping in requested_toppings:
	#判断这个元素是否green peppers，如果是则输出以下句子；
	if requested_topping == 'green peppers':
		print("Soryy, we are out of green peppers right now.")
	#如果元素不等于green peppers就输出以下句子；
	else:
		print("Adding " + requested_topping + ".")
#循环外增加一个提示语，说明pizza已经完成。
print("\nFinished making your pizza!")
```

##### 确定列表不是空

###### 简单示例

```
#5.4.2确定列表不是空

#创建一个空列表
requested_toppings = []

#判断列表是否为空，如果列表有值，返回将会是True。
if requested_toppings :
	for requested_topping in requested_toppings:
		print("Adding " + requested_topping + ".")
#否则将输出提示语；
else:
	print("Are you sure you want a plain pizza?")
```

##### 使用多个列表

对比两个列表中的元素，如果元素不在另外一个列表里，将提示相关语句。

###### 简单示例

```
#5.4.3使用多个列表
available_toppings = ['mushrooms','olives','green peppers','pepperoni'
                      ,'pineapple','extra cheese']


requested_toppings = ['mushrooms','french fries','extra cheese']

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print("Adding " + requested_topping + ".")
	else:
		print("Sorry ,we don't have " + requested_topping + ".")
print("Finished making your pizza.")
```

##### 练习

```
#5-8以特殊方式跟管理员打招呼

user_groups = ['jerry','tom','admin','kirs','bitch']

for user_group in user_groups:
    if user_group == 'admin':
      print("Hello " + user_group + ", would you like to see a status report?")
    else:
      print("Hello " + user_group.title() + ", thank you for logging in again.")


#5-9判断列表是否为空

user_groups = ['jerry','tom','admin','kirs','bitch']


#增加if判断user_groups列表是否为空，如果不为空将进入for循环
if user_groups:
    for user_group in user_groups:
        if user_group == 'admin':
            print("Hello " + user_group + ", would you like to see a status report?")
        else:
            print("Hello " + user_group.title() + ", thank you for logging in again.")
#如果列表为空，将输入相关提示语；
else:
    print("We need to find some users!")


#5-10检查用户名

current_users = ['jerry','tom','admin','kirs','bitch']

new_users = ['sisi','minmin','yiyi','kirs','jiji']

for new_user in new_users:
    if new_user in current_users:
        print("用户名" + new_user.lower() + "已被占用，请使用别的用户名！" )
    else:
        print("用户名" + new_user.lower() + "已成功注册，感谢！")

#5-11序数

sort_numbers = [2,3,5,6,7,1,4,8,9]
#对列表进行排序
sort_numbers.sort()
for sort_number in sort_numbers:
    if sort_number == 1:
        print("1st\n")
    elif sort_number == 2:
        print("2nd\n")
    elif sort_number == 3:
        print("3rd\n")
    elif sort_number == 4:
        print("4th\n")
    elif sort_number == 5:
        print("5th\n")
    elif sort_number == 6:
        print("6th\n")
    elif sort_number == 7:
        print("7th\n")
    elif sort_number == 8:
        print("8th\n")
    else:
        print("9th\n")
print(max(sort_numbers))
print(min(sort_numbers))
print(sum(sort_numbers))
print(len(sort_numbers))
```

##### if语句格式建议

PEP8提供建议是，在条件== ,>=之类的比较语句，建议两端都增加空格，增加可读性。

feichou == zhangwenya

zhangwenya > haoge

##### 总结

1. 编写true或Falese条件测试。
2. if、if-else、if-elif-else结果语句。
3. 使用for，加上if语句，对列表进行处理。
4. if语句的写法建议。

### 6 .字典

Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。

#### 简单的字典

```
#简单的字典
#字典为花括号，第一个为key，第二个为value；
alien_0 = {'color': 'green', 'options': 5}

print(alien_0['color'])
print(alien_0['options'])

```

#### 使用字典

字典是一系列的键——值对。每个键都与一个值相关联。可将python任何对象用作字典的值。数字、字符串、列表乃至字典都可以。

键——值对是两个相关联的值。指定键的时候将返回对应的值。

键和值用冒号分隔。键——值对 用逗号分隔。

字典不限键——值对数量。

#### 访问字典的值

获取键对应的值，输入字典名字加方括号的键，将会返回对应的值。

```
alien_0 = {'color': 'green', 'options': 5}
#字典名加方括号内的键；
print(alien_0['color'])
```

#### 添加键——值对

字典是一种动态结构，可随时添加键——值对。

```

#创建一个字典
alien_0 = {'coloer': 'green', 'points': 5}
print(alien_0)
#添加新的键--值对；
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
```

#### 创建空字典

```
#创建一个空字典
alien_0 = {}
```

#### 修改字典键的值

```
#字典原本color键的值为green。
alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + ".")
#将字典color键的值更改为黄色
alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")
```

修改字典某个值，而改变外星人的行为

```
#创建一个外星人字典，包含该外星人属性；
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
#输出外星人x_position值；
print("Original x-position: " + str(alien_0['x_position']))

#判断外星人speed值，然后执行对应代码；
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

#最终外星人的x_position 为x_increment值加x_position值；
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))

```

#### 删除键--值对

```
#删除键--值对
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

#删除color这个键
del alien_0['color']
print(alien_0)
```

#### 字典书写建议

```
#favorite_languages，该小结告诉字典书写技巧；

#包含多个键--值对时，建议使用语法书写；
#1、输入左花括号回车，然后下一行缩进四个空格’
#2、指定键--值对，并在后面加上一个逗号,回车自动缩进后续的键--值对；
#3、建议在最后一个键--值对也加上逗号，为后续增加键--值对做好准备；
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

print("Sarah's favorite language is " +
      favorite_languages['sarah'].title() +
      ".")

```

#### 练习

```
#练习
#6-1创建一个熟人信息

feichou = {
    'last_name': '抽',
    'first_name': '废',
    'age': '25',
    'city': 'shenzhen',
    }

print("张文雅简称： " +
      feichou['first_name'] +
      feichou['last_name'] +
      "，今年她" +
      feichou['age'] +
      "岁，她居住在" +
      feichou['city'] +
      ".")

#6-2喜欢的数字

numbers = {
    'simin': '8',
    'sihua': '7',
    'shuyi': '5',
    'weijie': '4',
    }

print("思敏喜欢的数字：" + numbers['simin'])
print("思华喜欢的数字：" + numbers['sihua'])
print("淑仪喜欢的数字：" + numbers['shuyi'])
print("伟杰喜欢的数字：" + numbers['weijie'])


#6-3已学python词汇表

vocabulary = {
    'list': '列表',
    'tupe': '元组',
    'dict': '字典',
    'variable': '变量',
    'if': '判断',
    }

print("list：\n" + vocabulary['list'])
print("tupe：\n" + vocabulary['tupe'])
print("dict：\n" + vocabulary['dict'])
print("variable：\n" + vocabulary['variable'])
print("if：\n" + vocabulary['if'])

```

#### 遍历字典

```
#6.3.1遍历所有键--值对

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

#使用for循环遍历字典所有键--值对；
#key,value两个变量可以自定义；
for key, value in favorite_languages.items():
    print("\nKey: " + key)
    print("Value: " + value)

```

遍历字典顺序python毫不关心，只关心键--值对应关系。



##### 遍历字典所有键

```
#6.3.2遍历所有键
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

#使用for循环遍历字典所有键；
#使用变量name遍历键，这样更直观需要提取相关的信息；
#如果不加favorite_languages.key()效果和favorite_languages：一样，不过增加key()更直观；
for name in favorite_languages.keys():
    print(name.title())

```

遍历字典，在指定名字时输出喜欢的语言

```
#6.3.2-1遍历包含指定的键
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
#创建一个指定名称的列表；

friend = ['jen', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    #判断键如果在列表里，将输出喜欢的语言；
    if name in friend:
        print(" Hi " + name.title() +
              ",I see your favorite language is " +
              favorite_languages[name].title())
        

```

还可以使用key()确定某个人是否接受了调查。

```
#6.3.2-2使用key()确定某个人是否被调查。
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

#判断erin是否在favorite_languages字典里，如果不在将输出提示语,请参加投票。
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

```

##### 按顺序遍历字典中的键

字典总是明确的记录键和值之间的关联关系，但获取字典元素时，获取顺序是不可预测的。这不是问题，只要键和值相对应即可。如果需要特定顺序返回元素，需要使用sorted()进行特定排序。

```
#6.3.3 使用sorted()排序dirt键的顺序.

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

#使用sorted()将键排序，然后在遍历。
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

```

##### 遍历字典中所有的值

如果需要提取字典的值，需要使用values()，它将返回一个值的列表，而不包含任何键。

```
#6.3.4遍历字典所有的值。使用values()

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
print("The following languages have been mentioned:")
#遍历字典所有的值，并赋值给language该变量。
for language in favorite_languages.values():
    print(language.title())


```

检查值中是否重复，可以使用set()集合，剔除重复项。

```
#6.3.4-1使用set()集合，剔除重复值

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
print("The following languages have been mentioned:")
#使用set剔除字典值重复项。
for language in set(favorite_languages.values()):
    print(language.title())

```

##### 练习

```
#6-4使用6-3代码，分别输出键或值。
vocabularys = {
    'list': '列表',
    'tupe': '元组',
    'dict': '字典',
    'variable': '变量',
    'if': '判断',
    'set': '集合',
    'sorted': '排序',
    'title': '首字母大写',
    'items': '遍历key,value',
    'keys': '遍历key',
    'value': '遍历value'
    }

for key, value in vocabularys.items():
    print(key.title() + ":" + value)


#6-5河流

#创建一个字典，包括河流及经过国家

three_rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'changjiang': 'china',
    }

#遍历字典
for river, state in three_rivers.items():
    print("The " + river + " runs through " + state + ".")

#遍历所有键
for river in three_rivers.keys():
    print("The three major rivers in the world are " + river)
    
#遍历所有值
for state in three_rivers.values():
    print("The countries where the three major rivers pass " + state)


#6-6调查，判断列表是否在名单里，如果在输出相关提示语。

#创建一个字典。
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

#创建一个调查名单，判断是否在字典里
friends = ['jen','kris','sarah','jerry','tom']

#先遍历调查名单
for friend in friends:
    #判断调查名单是否在字典里，如果是将执行代码，否则输出提示语。
    if friend in favorite_languages.keys():
        print(friend.title() + " ,感谢你参与投票，你喜欢的语言是 " +
              favorite_languages[friend])
    else:
        print(friend.title() + "你没有参与本次投票，欢迎参与，谢谢！")

```

#### 嵌套

有时需要将一系列字典存储在列表中，或将列表作为存储在字典中，这称为嵌套。

可以在列表中去嵌套字典、在字典中嵌套列表甚至在字典中嵌套字典。

##### 字典列表

如果管理成群结队的外星人呢？一种办法是创建一个外星人列表，其中每个外星人都是一个字典，包含有关的外星人的各种信息。

```
#6.4.1字典列表

#创建3个包含不同信息的外星人字典；
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

#列表嵌入字典；
aliens = [alien_0, alien_1, alien_2]

#遍历列表所有的字典；
for alien in aliens:
    print(alien)

```

一般情况外星人不止三个，而且每个外星人的代码都是自动生成的，可以使用range（）生成30个外星人：

```
#6.4.1-2 range()自动生成30个外星人信息

#创建一个空列表，将存储30个外星人字典信息；
aliens = []

#使用range()，产生30个外星人信息，并且添加到aliens列表里。
for alien_number in range(30):
    new_alien = {'color': 'green', 'poions': 5, 'speed': 'slow'}
    aliens.append(new_alien)

#使用切片，显示列表前五位外星人信息；
for alien in aliens[:5]:
    print(alien)
print("...")

#显示列表长度
print("Total number of aliens: \n" + str(len(aliens)))

```



###### 字典中存储列表

如果使用列表，只能存储添加的比萨配料，而如果使用字典，就不仅可以包含配料列表，还可以包含其他比萨的描述。

```
#6.4.2在字典中存储列表

#存储所点的比萨信息
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }

#概述所点的比萨

print("You ordered a " + pizza['crust'] + "-crust pizza " +
      "with the following toppings:")

#pizza字典里配料toppings包含配料列表，而不是单个值；
for topping in pizza['toppings']:
    print("\t" + topping)

```



字典包含列表的好处，一个键可以对应多个值，这些值都包含在这个列表里。

```

#6.4.2-1 字典嵌套列表
#遍历字典的for 循环中，需要再使用一个for循环来遍历相对应的列表；

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell']
    }
#for循环，先遍历字典元素；
#再使用for循环，编列字典值里列表的元素；
for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())

```



加入if语句，判断如果只有一种喜欢的语言，将提示其他语句。

```

#6.4.2-2 增加if语句，判断喜欢语言是否只有一个

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell']
    }

for name, languages in favorite_languages.items():
    #判断喜欢语言是否只有一个，如果不是将输出以下代码；
    if len(languages) > 1:
        print("\n" + name.title() + "'s favorite languages are:")
        for language in languages:
            print("\t" + language.title())
    else:
        for language in languages:
            print("\n" + name.title() + "'s favorite languages is:" +
                  language)

```

同样问题，else没有使用for遍历列表，而是直接用索引访问列表元素。

```

#6.4.2-2 增加if语句，判断喜欢语言是否只有一个

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell']
    }

for name, languages in favorite_languages.items():
    #判断喜欢语言是否只有一个，如果不是将输出以下代码；
    if len(languages) > 1:
        print("\n" + name.title() + "'s favorite languages are:")
        for language in languages:
            print("\t" + language.title())
    else:
        language = languages[0]
        print("\n" + name.title() + "'s favorite languages is:" +
                  language.title())

```



##### 字典中存储字典

字典中嵌套字典，代码可能会变复杂很多。但是遍历字典键时，将返回对应信息的字典。

```
#6.4.3字典嵌套字典

#字典嵌套字典；
#键为用户名，值为字典。字典里包含用户名相关信息；
user = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },
    }
#遍历字典；
for username, user_info in user.items():
    print("\nUsername: " + username)
    #合并字典值，并赋值给full_name变量；
    full_name = user_info['first'] + " "  + user_info['last']
    location = user_info['location']

    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())

```

##### 练习

```
#练习
#6-7 创建3个表示人的字典

feichou = {
    'position': 'lowly',
    'nature': 'not good',
    'sex': 'girl',
    }

haohao = {
    'position': 'rank',
    'nature': 'good',
    'sex': 'boy',
    }

weijie = {
    'position': 'medium',
    'nature': 'medium',
    'sex': 'boy',
    }

peoples = [feichou, haohao, weijie]

for people in peoples:
    print(people)


#6-8 列表嵌套字典

cat_green = {
    '主人': 'liangweijie',
    '类型': '斗牛犬',
    }

cat_yellow ={
    '主人': '自己',
    '类型': '汪汪',
    }

cat_balk ={
    '主人': '自己',
    '类型': '人类',
    }

pets = [cat_green, cat_yellow, cat_balk]

for pet in pets:
    print(pet)



#6-9 字典嵌套列表

favorite_places = {
    'tom': ['北京', '泰国', '日本'],
    'jerry': ['广州', '深圳', '龙岗'],
    'kirs': ['新加坡', '海南', '巴黎'],
    }


for name, places in favorite_places.items():
    print(name.title() + "喜欢去的地方有：")
    for place in places:
        print("\t" + place)


#6-10 字典嵌套列表

favorite_numbers = {
    'tom': [1, 2, 3],
    'jerry': [4, 5, 6],
    'kirs': [7, 8, 9],
    }


for name, numbers in favorite_numbers.items():
    print(name.title() + "喜欢去的数字有：")
    for number in numbers:
        print("\t" + str(number))


#6-10 字典嵌套字典

cities = {
	'深圳': {
	'国家': '中国',
	'人口': '13亿',
	'事实': '强大',
	},
	'曼谷': {
	'国家': '泰国',
	'人口': '6900万',
	'事实': '强大',
	},
	'河内': {
	'国家': '越南',
	'人口': '9554万',
	'事实': '强大',
        },
    }

for city, citie_info in cities.items():
    print("城市：" + city)
    country = citie_info['国家']
    poputation = citie_info['人口']
    fact = citie_info['事实']

    print("它属于 " + country + "，国家人口 " + poputation + ",国家事实 " + fact)

```

#### 小结

1. 如何定义字典；
2. 如何存储信息在字典里；
3. 如何访问修改字典元素；
4. 遍历字典元素；
5. 遍历字典键-值对；
6. 遍历字典所有键；
7. 遍历字典所有值；
8. 如何列表中嵌套字典；
9. 如何字典中嵌套列表；
10. 如何字典中嵌套字典；



### 7 .input输入

input()函数可以让用户输入需要的信息。

工作原理：函数input（）让程序暂停运行，等待用户输入一些文本。获取用户输入后，python将其存储一个变量，方便调用。

```
#7.1函数input()的工作原理

message = input("告诉一些东西，然后我会重复告诉你：")
print(message)

```

#### 编写清晰的程序

每当使用input（）时，都应制定清晰而易于明白的提示，准确的指出你希望用户提供什么信息。

```
#一般使用input()，需要准确的指出希望用户提供什么信息；

name = input("请输入你的名字：")
print("您好," + name + "!")

#如果提示语超过一行，可以将提示语赋值给一个变量，这样input()会较为清晰；

prompt = "如果你告诉我你是谁，我们可以对你的信息个性化设置。"
prompt += "\n你的姓名是什么？"

name = input(prompt)
print("您好," + name + "!")

```



#### 使用int()来获取数值输入

使用int()时，用户输入信息python将解读为字符串，如果用作输入将不会发生问题，但是如果进行数值判断，就会报错。就必须使用int()函数转换为数值。

```
#7.1.2使用int()获取数值输入

height = input("你的身高多少？")

#将字符串转换为数值；
height = int(height)


#将用户提供信息进行判断；
if height >= 36:
    print("你身高适合玩过山车呀！")
else:
    print("你身高还不适合玩过山车哦~")

```

#### 求模运算符（%）

两个数相处返回余数。可以使用求模运算符判断奇数还是偶数。

```
#7.1.3 求模运算符  %

number = input("请输入一位数字：")
number = int(number)

if number % 2 == 0:
    print("这是偶数！")
else:
    print("这是奇数！")

```



#### python2.7获取输入

python2.7使用raw_input()函数，而不是使用input()。



#### 练习

```
#7-1汽车租赁

rent = input("What car would you like to rent?")
print("Let me see if I can find you a " + rent + "。")

#7-2餐馆定位

danner = input("How many people have dinner?")
danner = int(danner)

if danner >= 8:
    print("Sorry, Not enough Seat.You have " + str(danner) + " people.")
else:
    print("Have a good dinner.")

#7-3 10的倍数

number = input("请输入一位数，将判断是否10的倍数:")
number = int(number)

if number % 10 == 0:
    print(str(number) + "是10的倍数。")
else:
    print(str(number) + "不是10的倍数。")

```



#### while 循环

for循环用于针对集合中的每个元素的一个代码块，而while循环不断的运行，直到指定条件不满足位置；

##### 使用while循环

```
#7.2.1使用while循环


current_number = 1
#只要cuen_number满足<=5，就会一直运行此循环；
while current_number <= 5:
    print(current_number)
    #每次叠加1；
    current_number += 1

```

##### 判断退出

```
#7.2.2让用户选择退出

#提示语
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."

#定义message为空，不然无法进入while循环；
message = ""
#如果不等于quit将一直执行；
while message != 'quit':
    message = input(prompt)
    print(message)

```

以上代码如果输入quit，将会把quit再次输出才退出程序，增加if判断，以下为优化程序：

```
#7.2.2让用户选择退出优化

#提示语
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."

#定义message为空，不然无法进入while循环；
message = ""
#如果不等于quit将一直执行；
while message != 'quit':
    message = input(prompt)
    #增加if判断是否quit，如果是则输入信息；
    if message != 'quit':
        print(message)

```



##### 使用标志

定义一个变量用于判断程序是否处于活动状态，这个变量被称为标志。while语句只需判断变量当前值是否True还是False。

```
#7.2.3使用标志

#提示语
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program.\n"

#定义个变量作为标志
active = True

#判断标志当前值是否True，如果是将执行循环；
while active:
    message = input(prompt)
    
    #使用if判断message是否quit，如果是将标志赋值为False;
    if message == 'quit':
        active = False
    else:
        print(message)
```



##### break退出循环

要立即退出while循环，不再运行循环中余下的代码，也不管条件测试结果如何，可使用break语句。

```
#7.2.4使用break退出循环

#提示语
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\nEnter 'quit' when you are finished.\n"



#判断标志当前值是否True，如果是将执行循环；
while True:
    city = input(prompt)
    
    #使用if判断city是否quit，如果是则使用break语句直接退出循环；
    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")

```

##### continue

要返回到循环开头，并根据条件测试结果决定是否继续执行循环，可使用continue，它不像break语句直接退出循环。

```
#7.2.5 在循环中使用continue

current_number = 0

#打印1-10里的奇数；
while current_number < 10:
    current_number += 1
    
    #使用求模运算，判断是否偶数，将返回循环，不再执行下面代码；
    if current_number % 2 == 0 :
        continue
    
    #如果是奇数将输出信息；
    print(current_number)

```



##### 避免无限循环

ctrl+C可以结束无限循环。

确认程序至少有一个这样的地方能让循环条件为False或让break语句得以执行。

##### 练习

```
#7-4比萨配料

prompt = "请输入你的pizaa配料:\n"
prompt += "Enter 'quit' when you are finished."

pizza = ""
while pizza != 'quit':
    pizza = input(prompt)

    if pizza != 'quit':
        print("你的pizza已经添加配料: " + pizza + ".")


#7-5电影票

prompt = "请输入您的年龄查看电影票价格：\n"
prompt += "\nEnter 'quit' when you go out."

active = True
while active:
    age = input(prompt)
    
    if age != 'quit':
        age = int(age)
        if age < 3:
            print("免费")
        elif age <= 12:
            print("10元.")
        else:
            print("15元.")
    else:
        active = False


#7-6电影票,break结束
prompt = "请输入您的年龄查看电影票价格：\n"
prompt += "\nEnter 'quit' when you go out."

age = ""
while age != 'qiut':
    age = input(prompt)
    
    if age != 'quit':
        age = int(age)
        if age < 3:
            print("免费")
        elif age <= 12:
            print("10元.")
        else:
            print("15元.")
        
    else:
        break

```



#### 处理列表和字典

要记录大量的用户和信息，需要在while循环中使用列表和字典。

for可以遍历列表，但是for循环中不应该修改列表。修改列表将会导致for循环无法遍历元素，所以可以使用while循环。



##### 在列表间移动元素

将一个列表的元素转移到另外一个列表。



```
#首先，创建一个待验证用户列表；
#和一个用于存储已验证用户的空列表；

unconfirmed_users = ['alice', 'brian', 'candace']

confirmed_users = []

#验证每个用户，直到没有未验证用户为止；
#将每个经过验证的列表都移到已验证用户列表中；

#判断未验证用户列表是否为空；
while unconfirmed_users:
    #使用pop()弹出未验证列表最后一位元素；
    current_user = unconfirmed_users.pop()
    
    print("Verifying user: " + current_user.title())
    #将弹出的元素添加至已验证列表中；
    confirmed_users.append(current_user)


#显示所有已验证的用户
print("\nThe following users have been confirmed:")

#遍历已验证的用户列表
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

```



##### 删除包含特定值的所有元素表

函数remove()可以删除列表中的特定值，如果需要删除列表中所有特定值，需要使用while循环。

```
#7.3.2删除列表所有特定值

#创建一个包含重复元素的列表；
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']

#输出原列表所有元素；
print(pets)

#判断cat是否在列表里，如果是将执行循环；
while 'cat' in pets:
    pets.remove('cat')

#输出删除后的pets列表，所有重复元素已被删除；
print(pets)

```



##### 使用用户输入来填充字典

使用while循环，获取用户相关信息，来填充字典。

```
#7.3.3使用用户输入来填充字典

#创建一个空字典，将存储用户、及喜欢那座山；
responses = {}

#创建一个标志；
polling_active = True

while polling_active:
    #获取用户名字；
    name = input("\nWhat is your name?")
    #获取用户喜欢的山；
    response = input("Whitch mountain would you like to climb someday?")
    #将信息写入列表里；
    responses[name] = response
    
    #询问用户是否还继续调查，如果否将退出调查；
    repeat = input("Would you like to let another person respond?(yes/no)")
    if repeat == 'no':
        #标志赋值为False，将退出循环；
        polling_active = False

print("\n----Poll Results ----\n")
#遍历字典，输出用户和用户喜欢的山；
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")

```



##### 练习

```
#7-8 熟食店
#创建一个三文治列表；
sanwich_orders = ['火腿', '鸡蛋', '青菜']
#创建一个三文治空列表；
finished_sandwiches = []
#输出三文治清单；
print(sanwich_orders)

while sanwich_orders:
    #弹出三文治清单；
    sanwich_order = sanwich_orders.pop()
    print("三文治里面有:" + sanwich_order)
    #将弹出清单添加至完成的三文治清单；
    finished_sandwiches.append(sanwich_order)

print("三文治已完成。")

#遍历已完成的三文治清单；
for finished_sandwiche in finished_sandwiches:
    print(finished_sandwiche)

#7-9 五香烟熏牛肉卖完，需要在列表删除
#创建一个三文治列表；
sanwich_orders = ['dog', 'pastrami', 'age', 'pastrami', 'pastrami']

#输出三文治清单；
print(sanwich_orders)

if 'pastrami' in sanwich_orders:
    print("No have pastrami,delete pastrami ing..")
    while 'pastrami' in sanwich_orders:
        sanwich_orders.remove('pastrami')

print("三文治已完成。")

#遍历已完成的三文治清单；
for finished_sandwiche in sanwich_orders:
    print(finished_sandwiche)


#7-10 梦想度假胜地

resorts = {}

polling_active = True

while polling_active:
    name = input("您叫什么名字？\n:")
    resort = input("您想去哪里度假啊？\n:")

    resorts[name] = resort

    repeat = input("是否继续调查？[yes/no]")

    if repeat == 'no':
        polling_active = False

print("以下为统计信息：\n")

for name, resort in resorts.items():
    print(name.title() + " 想去 " + resort.title() + "度假游玩。")

```



#### 小结

1. input（）获取用户信息；
2. while（）循环；
3. 控制while循环流程，设置标志、break、continue。
4. while循环将列表元素移动到另外一个列表；
5. while删除列表所有特定值；
6. while（）循环字典；

### 8 .函数

函数是带名字的代码块，用于完成具体的工作。要执行函数定义的特定任务，可调用该函数。如果需要多次执行相同任务，只需执行该任务函数。

#### 定义函数

```
#8.1定义函数

#使用def关键字定义一个greet_user函数。括号里可以包含其他信息，这里将不需要；
def greet_user():
    #文档字符串注释，描述函数做什么的，help（）可以查看相关文档；
    """显示简单的问候语"""
    #函数体内代码；
    print("hello!")
#调用函数gret_user()；
greet_user()

```

##### 向函数传递信息

定义函数后，可以在函数括号里添加username，函数就可以接受你给username指定任何值。

```
#8.1.1向函数传递信息

#使用def关键字定义一个greet_user函数。括号里可以包含其他信息，这里将不需要；
#在括号添加username；
def greet_user(username):
    #文档字符串注释，描述函数做什么的，help（）可以查看相关文档；
    """显示简单的问候语"""
    #函数体内代码；
    print("hello!" + username.title())
#调用函z数gret_user()；
#在括号将需要传递信息填入；
greet_user('kirs')
```



##### 实参和形参

实参是调用函数时调用给函数对应的形参。

以下区分实参和实参关系：

```
#8.1.2实参和形参的区别

#括号内usename即为形参；
def greet_user(username):
...
#'kirs'即为实参；
#实参是调用函数时调用给函数对应的形参，即为上面函数的username；
#类似实参kirs赋值给形参username；
greet_user('kirs')

```

##### 练习

```
#8-1消息

def display_message():
    print("本章学习了如何定义函数。")

display_message()

#8-2喜欢的图书

def favorite_book(book):
    print("my favorite book is " + book.title())

favorite_book('python3')

```



#### 传递实参

函数定义可能包含多个形参，因此函数调用中也可能包含多个实参。

向函数传递实参方式很多：

可使用**位置实参**：这要求实参的顺序与形参顺序相同；

可使用**关键字实参**：其中每个实参都由变量名和值组成；

#### 位置实参

实参顺序一一对应形参的，这种被称为位置实参。

位置实参顺序很重要，如果实参的顺序与形参顺序不一致，结果可能将会出乎意料。所以使用位置形参，必须确认实参与形参顺序一致。

```
#8.2.1位置实参

#定义形参animal_type和pet_name；
def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
#实参dog,feichou位置必须按形参顺序对应，否则实参与形参对应关系就有误；
describe_pet('dog', 'feichou')
```



##### 调用多次函数

如果需要调用函数任意次，再次调用函数即可，若需要对应形参，必须添加对应的实参即可。

```
describe_pet('dog', 'feichou')
#第二次调用函数，与第一次调用函数一样，实参顺序对应形参；
describe_pet('cat', 'xiaoliang')
```

调用函数多次是一种效率极高的工作方式，我们只需在函数中编写一次，然后将函数重复调用，即可重复运行函数里的代码。



#### 关键字实参

关键字实参是传递给函数的名称——值对。关键字实参无需考虑函数调用中的实参顺序，并且能清楚的指出函数调用中各个值的用途。

```
#8.2.2关键字实参

#定义形参animal_type和pet_name；
def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
#关键字实参明确地指出各个实参对应的形参；
#使用关键字实参，务必准确地指定函数定义的形参名；
describe_pet(animal_type='dog', pet_name='feichou')

```



#### 默认值

编写函数时，可给每个形参指定默认值。在调用函数中给形参提供了实参时，python将使用指定实参的值，否则将会使用形参的默认值。

```
#8.2.3默认值

#animal_type使用默认值dog；
#函数调用时没有给animal_type实参，默认将会使用dog这个实参；
def describe_pet(pet_name, animal_type='dog'):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
#只指定pet_name实参，animal_type将使用默认值；
describe_pet(pet_name='feichou')

```

由于animal_type**指定了默认值**，无需通过实参来指定，因此函数调用中只包含一个实参；然而python依然将这个pet_name**实参视为位置实参**；所以需要将pet_name放在形参开头；如果不使用默认值，并且按关键字实参覆盖了默认值，将无需考虑位置实参问题；



#### 等效的函数调用

可混合使用位置实参、关键字实参和默认值，通常有多重等效的函数调用方式，以下各种实参传递方式，实现效果都一致。调用方式无关紧要，只要函数调用能生成预期结果就行。

```
#8.2.4等效的函数调用

#animal_type使用默认形参，所以pet_name需要提供实参；
def describe_pet(pet_name, animal_type='dog'):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

#位置实参
describe_pet('willie')

#关键字实参
describe_pet(pet_name='willie')

#位置形参，并且将animal_type默认值覆盖；
describe_pet('willie', 'hamster')


#关键字实参，并且将animal_type默认值覆盖；
describe_pet(pet_name='willie', animal_type='hamster')

#关键字实参，不在乎形参位置顺序；
describe_pet(animal_type='hamster', pet_name='willie')


```



#### 避免实参错误

如果遇到实参不配错误，python将会用trceback指出错误出处。

```
Traceback (most recent call last):
  File "D:/Github/python_work/ex/ex8/8.2.4.py", line 23, in <module>
    describe_pet(animal_type='hamster')
TypeError: describe_pet() missing 1 required positional argument: 'pet_name'

```

告诉你错误在23行，describe_pet函数里。缺少一个实参；



##### 练习

```
#8-3 T_shirt

def make_shirt(size, prompt):
    print("即将制作一件大小为 " + size.upper() + ",标语为 " + prompt.title() + " 的T-shirt.")


#位置实参
make_shirt('xl', 'i love you')

#关键字实参
make_shirt(size='xl', prompt='i love you')


#8-4 大号T_shirt

def make_shirt(size, prompt='i love python'):
    print("即将制作一件大小为 " + size.upper() + ",标语为 " + prompt.title() + " 的T-shirt.")


#制作一件印有默认字样的大号T，位置实参；
make_shirt('l')

#制作一件印有默认字样的中号T，关键字实参；
make_shirt(size='m')

#制作一件印有其他字样的T,关键字形参，不考虑顺序；
make_shirt(prompt='i love you', size='m')

#8-5 城市

def describe_city(city, state='china'):
    print("城市： " + city.title() + " 属于这个国家： " + state.title())


#位置实参；
describe_city('shenzhen')

#关键字实参；
describe_city(city='guangzhou')

#关键字形参，不考虑顺序；
describe_city(state='japan', city='tokyo')

```



#### 返回值

函数并非总是直接显示输出，相反，它可以处理一些数据，并返回一个或一组值，返回的值被称为返回值。可以使用return语句将值方慧到调用函数的代码行。返回值能够让程序的大部分繁重工作转移到函数中去完成，从而简化程序。

##### 返回简单值

```
#8.3.1返回简单值

def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + last_name
    #将full_name的值返回
    return full_name.title()

#将函数返回值复赋值给musician变量；
musician = get_formatted_name('jimi', 'hendrix')
print(musician)

```

以上函数分别存储名和姓，每当需要显示姓名时可以调用此函数。



##### 让实参变成可选

有时候需要让实参变成可选的，可使用默认值来让实参变成可选。

```
#8.3.2让实参变成可选的

def get_formatted_name(first_name, middle_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    #将full_name的值返回
    return full_name.title()

#将函数返回值复赋值给musician变量；
musician = get_formatted_name('jimi', 'lee', 'hendrix')
print(musician)

```

以上代码增加了中间名，但是有时候不是所有人都会有中间名，所以需要让中间名该实参变成可选。

```
#8.3.2让实参变成可选的

def get_formatted_name(first_name, middle_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    #将full_name的值返回
    return full_name.title()

#将函数返回值复赋值给musician变量；
musician = get_formatted_name('jimi', 'lee', 'hendrix')
print(musician)

```

以上代码中，添加中间名选项，如果没有中间名的用户，会导致程序运行有问题。所以需要将中间名实参变为可选，需要更改一下代码：

```
#8.3.2-1让实参变成可选的

#将middle_name中间名指定一个默认值，让中间名实参可选；
def get_formatted_name(first_name, last_name, middle_name=''):
    """返回整洁的姓名"""
    #python中非空字符串解读为true,判断中间名是否为空，如果不是将把中间名字段加上；
    if middle_name:
    	full_name = first_name + ' ' + middle_name + ' ' + last_name
    #如果中间名为空，全名将不会包含中间名；
    else:
    	full_name = first_name + ' ' + last_name
    #将full_name的值返回
    return full_name.title()

#将函数返回值复赋值给musician变量；
musician = get_formatted_name('jimi', 'hendrix',)
print(musician)

```



#### 返回字典

函数可返回任何类型的值，包括列表和字典等较复杂的数据结构。

```
#8.3.3返回字典

def build_person(first_name, last_name):
    """返回一个字典，其中包含有关一个人的信息"""
    
    #键为fist，而key为形参first_name；
    person = {'fist': first_name, 'last': last_name}
    return person
#使用位置实参对应形参，把信息存储在字典里;
musician = build_person('jimi', 'hendrix')
print(musician)

```

字典也接受可选值：

```
#8.3.3-1字典实参变为可选

#添加一个age形参，并且指定为默认值为空；
#这样该形参如果没有传递实参，就直接使用默认值空字符；
def build_person(first_name, last_name, age=''):
    """返回一个字典，其中包含有关一个人的信息"""

    person = {'fist': first_name, 'last':last_name}

    #判断age字段是否为空，如果不是将值写入person字典对应的age key中；
    if age:
        person['age'] = age

    #键为fist，而key为形参first_name；
    return person
#使用位置实参对应形参，把信息存储在字典里;
#这里增加age的实参；
musician = build_person('jimi', 'hendrix', age = 28)
print(musician)

```



#### 函数和while循环

```
#8.3.4函数和while循环

def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + last_name
    return full_name


while True:
   print("\n请告诉你的名字：")
   f_name = input("姓：")
   l_name = input("名:")

   formatted_name = get_formatted_name(f_name, l_name)
   print("\n您好！ " + formatted_name.title())

```

以上代码不没有涉及退出条件，导致无限循环，以下增加退出条件：

```
#8.3.4-1函数和while循环，增加break退出条件

def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + last_name
    return full_name


while True:
   print("\n请告诉你的名字：")
   print("随时输入'q'即将退出程序")
   f_name = input("姓：")
   #增加判断是否需要执行退出循环；
   if f_name == 'q':
       break
   l_name = input("名:")
   if l_name == 'q':
       break

   formatted_name = get_formatted_name(f_name, l_name)
   print("\n您好！ " + formatted_name.title())

```

#### 练习

```
#8-6城市名

def city_country(city, country):
    citys = city + "," + country
    return citys

musician = city_country('shenzhen', 'china')
print(musician)
musician = city_country('guangzhou', 'china')
print(musician)
musician = city_country('phoenix', 'america')
print(musician)

#8-7专辑

def make_album(star, song, number=''):
    album = {star: song}
    if number:
        album['数量'] = number
    
    return album


musician = make_album('周杰伦', '不想你哭')
print(musician)

musician = make_album('张国荣', '我')
print(musician)

musician = make_album('刘德华', '17岁', number = 20)
print(musician)


#8-8专辑,增加while循环，读取用户数据，并且提供退出循环条件；

def make_album(star, song, number=''):
    album = {star: song}
    if number:
        album[number] = number
    
    return album


while True:
    print("请输入您喜欢的专辑：\n")
    print("随时可以输入'q'退出")

    star_i = input("歌手：")
    if star_i == 'q':
        break
    song_i = input("歌曲名：")
    if song_i == 'q':
        break

    musician = make_album(star_i, song_i)
    print(musician)

```



#### 传递列表

向函数传递列表很有用，这种列表包含的可能是名字、数字或更复杂的对象（如字典）。

```
#8.4传递列表

#定义一个函数greet_users；
def greet_users(names):
    """向列表中的每位用户都发出简单的问候"""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

#定义一个名字列表；
usernames = ['kirs', 'tom', 'jerry']
#将列表作为实参，使用位置实参传递给形参；
greet_users(usernames)
```



##### 函数中修改列表

将列表传递给函数后，函数就可对其进行修改。在函数中对这个列表所做的任何修改都是永久性的，这能够高效的处理大量数据。

```
#8.4.1在函数中修改列表

def print_models(unprinted_designs, completed_models):
    """
    模拟打印每个设计，直到没有未打印的设计为止
    打印每个设计后，都将其已到列表completed_models中
    """

    while unprinted_designs:
        current_design = unprinted_designs.pop()

        #模拟根据设计制作3D打印模型的过程
        print("Printing model: " + current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """显示打印好的所有模型"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

#创建一个未打印列表；
unprinted_designs = ['iphone case', 'robo pendant', 'dodecachedron']
#创建一个完成列表；
completed_models = []

#调用打印函数，使用位置实参传递给形参；
print_models(unprinted_designs, completed_models)

#调用显示完成函数；
show_completed_models(completed_models)
```

以上函数优点：

1. 程序更容易扩展和维护，不需要对源代码修改，只需要将打印内容修改一次再调用即可。
2. 每个函数都负责一项具体工作，有助于复杂的任务划分成一系列步骤；



##### 禁止函数修改列表

向函数传递列表的副本，保留原有的列表。这样函数修改将只会影响副本，而丝毫不影响原件。

将列表副本传递给函数，可以使用切片：

`function_name(list_name[:])`

`print_models(unprinted_designs[:], completed_models)`

一般处理大型列表时，建议不使用副本。让函数使用现成的列表可避免花时间和内存创建副本，从而提升效率。



#### 练习

```
#8-9魔术师

def show_magicians(names):
    """向列表中魔术师打招呼"""
    print("以下魔术师有：\n")
    for name in names:
        print("欢迎魔术师 " + name.title() + "!")

magicians = ['kirs', 'tom', 'jerry']
show_magicians(magicians)
    
#8-10了不起的魔术师

def make_great(ungreat, great):
    """
    模拟每个魔术师，直到没有魔术师为止
    每个魔术师增加The Great，并已到列表great里；
    """
    while ungreat:
        current_magicians = ungreat.pop()
        completed_magicians = 'The Great' + current_magicians
        great.append(completed_magicians)


def show_magicians(names):
    """向列表中魔术师打招呼"""
    print("以下魔术师有：\n")
    for name in names:
        print("欢迎魔术师 " + name.title() + "!")

#创建一个未增加The Great的魔术师列表;
ungreat = ['kirs', 'tom', 'jerry']
#创建一个空列表，将存储增加The Great魔术师的列表；
great = []
make_great(ungreat, great)
show_magicians(great)


#8-11了不起的魔术师

#使用切片，传递ungreat副本给函数make_great；
def make_great(ungreat, great):
    """
    模拟每个魔术师，直到没有魔术师为止
    每个魔术师增加The Great，并已到列表great里；
    """
    while ungreat:
        current_magicians = ungreat.pop()
        completed_magicians = 'The Great' + current_magicians
        great.append(completed_magicians)


def show_magicians(names):
    """向列表中魔术师打招呼"""
    print("以下魔术师有：\n")
    for name in names:
        print("欢迎魔术师 " + name.title() + "!")

#创建一个未增加The Great的魔术师列表;
ungreat = ['kirs', 'tom', 'jerry']
#创建一个空列表，将存储增加The Great魔术师的列表；
great = []
make_great(ungreat[:], great)

#显示增加The Great 的魔术师
show_magicians(great)

#显示为增加The Great的列表，确保函数修改的不是原件；
show_magicians(ungreat)

```



#### 传递任意数量的实参

python允许函数从调用语句中收集任意数量的实参。

```
#8.5传递任意数量的实参

#形参*toppings中的星号让python创建一个名为toppings的空元组
#收到所有实参都封装到这个元组中；

def make_pizza(*toppings):
    """打印顾客点的所有配料"""
    print(toppings)

#一个实参调用函数；
make_pizza('pepperoni')

#三个实参条用函数；
make_pizza('mushrooms', 'green peppers', 'extra cheese')
```

增加for循环，对配料做遍历：

```
#8.5-1增加for循环对配料做遍历

#形参*toppings中的星号让python创建一个名为toppings的空元组
#收到所有实参都封装到这个元组中；

def make_pizza(*toppings):
    """打印顾客点的所有配料"""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("-" + topping)

#一个实参调用函数；
make_pizza('pepperoni')

#三个实参条用函数；
make_pizza('mushrooms', 'green peppers', 'extra cheese')

```



##### 位置实参和任意数实参

python先匹配位置实参和关键字实参，再将余下的实参都收集到最后一个形参。

```
#8.5.1 结合使用位置实参和任意数量实参


def make_pizza(size, *toppings):
    """概述要制作的比萨"""
    print("\nMkaing a " + str(size) + "-inch pizza with the following toppings:")
    
    #遍历比萨材料；
    for topping in toppings:
        print("-" + topping)


make_pizza(16, 'pepperoni')

#增加size实参，后续无论多少个实参，都会存储在toppings形参里；
make_pizza(20, 'mushrooms', 'green peppers', 'extra cheese')

```



##### 任意数量的关键字实参

python也可以接受任意数量的键--值对。（字典）

```
#8.5.2 使用任意数量的关键字实参


def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们指导的有关用户的一切"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    
    #将user_info键值对写入profile字典里；
    for key, value in user_info.items():
        profile[key] = value
    
    #返回字典值；
    return profile
#将传递姓，名，两个键值对location='princeton'和field='physics'
user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')

print(user_profile)

```



#### 练习

```
#8-12三文治

def sandwich(*toppings):
    """概述制作三文治材料"""
    print("\n以下是制作三文治的材料:")
    for topping in toppings:
        print("- " + topping)

sandwich('火腿', '鸡蛋', '青菜')

sandwich('西红柿')



#8-13 用户简介

def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们指导的有关用户的一切"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    
    #将user_info键值对写入profile字典里；
    for key, value in user_info.items():
        profile[key] = value
    
    #返回字典值；
    return profile


user_profile = build_profile('liang', 'weijie', location='shenzhen', love='jerry', wife='feichou')

print(user_profile)



#8-14 汽车

def make_car(firm, type, **property):
    """创建一个字典，其中包含我们指导的有关用户的一切"""
    car = {}
    car['firm_name'] = firm
    car['type_name'] = type
    
    #将property键值对写入car字典里；
    for key, value in property.items():
        car[key] = value
    
    #返回字典值；
    return car


car = make_car('subaru', 'outback', color='blue', tow_package=True)

print(car)


```



#### 函数存储在模块中

函数的优点之一是，使用它们可将代码与主程序分离。通过给函数指定描述性名称，可让程序容易理解得多。还可以将函数存储在被称为模块的独立文件夹中，再将模块导入到主程序中。import语句允许在当前运行的程序文件中使用模块的代码。

模块的优点：

1、将函数存储在模块中，可隐藏程序代码的细节，将重点放在程序的高层逻辑上。

2、不同程序中重用函数。

3、模块便于分享，并且可以共同编写函数库。



##### 导入整个模块

创建模块及导入方法：

1、让函数导入，就需要先创建模块，模块是扩展名为.py的文件。

```
#8.6.1创建模块
#创建一个名为pizza.py的模块，包含要导入的程序代码；

def make_pizza(size, *toppings):
    """概述要制作的比萨"""
    print("\nMaking a " + str(size) +
    "-inch pizza with the following toppings:")
    for topping in toppings:
        print("-" + topping)
```

2、导入模块。在pizza.py模块所在的目录中创建另一个名为making_pizzas.py文件，导入pizza模块。

```
#8.6.1导入pizza.py模块
#导入刚创建的pizza模块
import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```



import模块后，可以调用模块中所有函数。如果import moudule_name模块，以下为调用模块中函数的方法：

`module_name.function_name()`



##### 导入特定的函数

导入模块中特定函数：

`from moudule_name import function_name`

导入模块中任意函数：

`from moudule_name import function_0, function_1`

示例：

```
#导入模块指定的模块
from pizza import make_pizza
#无需增加模块名.函数名调用，直接使用函数名称即可。
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
```



##### 使用as给函数指定别名

导入的函数名称可能与程序中现有名称冲突，或者函数名称过长，可指定简短的别名——使用as。

```
#8.6.3使用as给函数指定别名

#模块导入make_pizza函数，并指定mp别名。
from pizza import make_pizza as mp

#使用别名mp就可以调用；
mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green pepers', 'extra cheese')
```



给模块指定别名通用语法：

`import module_name as mn`



##### 导入模块中所有函数

使用（*）号运算符可让python导入模块所有函数。

建议：尽量不要使用。模块中有函数名称与项目名称重复，python遇到多个名称相同，只会覆盖，而不会分别导入所有函数。

导入模块所有函数语法：

`from module_name import *`



#### 函数编写指南

1、给函数指定描述性名称。小写字母或下划线；

2、包含阐述函数功能的注释。采用文档字符串格式；

3、给形参指定默认值，等号两边不要加空格；

4、关键字形参指定值，等号两边不要加空格；

5、PEP8建议代码长度不要超过79字符。

6、程序或模块包含多个函数，可使用两个空行将相邻函数分开。方便查看前一个函数结尾，和函数开头地方。

7、import语句放开头。



#### 练习

```
#8-15打印模型
#1、首先创建一个模块，另存为printing_functions.py

def print_models(unprinted_designs, completed_models):
    """
    模拟打印每个设计，直到没有未打印的设计为止
    打印每个设计后，都将其已到列表completed_models中
    """

    while unprinted_designs:
        current_design = unprinted_designs.pop()

        #模拟根据设计制作3D打印模型的过程
        print("Printing model: " + current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """显示打印好的所有模型"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

#2、创建一个文件print_models.py，导入模块，并使用模块中的函数

#导入刚创建的模块
import printing_functions

#创建一个未打印列表；
unprinted_designs = ['iphone case', 'robo pendant', 'dodecachedron']
#创建一个完成列表；
completed_models = []

#使用模块名.函数名调用；
printing_functions.print_models(unprinted_designs, completed_models)

printing_functions.show_completed_models(completed_models)



#8-16创建一个模块，say_hello.py

def hello(name, sex):
    print(sex + ' ' + ' ' + name.title() + " Hello!")

#创建hello_all.py，导入say_hello.py

#8-16导入say_hello模块
#方:1：import 模块，调用模块.函数名
import say_hello

say_hello.hello('feichou', girl)

#8-16-1导入say_hello模块
#方法2：导入指定的模块 
#from module_name import function_name
#调用直接函数，不需要加模块名。

from say_hello import hello

hello('feichou', 'Mis')


#8-16-3导入say_hello模块
#方法3：将模块指定别名
#import module_name as fn

import say_hello as hi

hi.hello('feichou', 'Mis')


#8-16-4导入say_hello模块
#方法4：导入模块里所有的函数
#from module_name import *

from say_hello import *

hello('feichou', 'Mis')


```



#### 小结

1、编写函数。

2、传递实参。位置实参/关键字实参。

3、返回函数的值。

4、函数、列表、字典、if和while结合使用。

5、将函数存储在模块里，再从另外程序调用。



### 9.类

举个例子：你要充话费，就需要先下载支付宝，实名认证、绑定银行卡，再进行充值扣款这一系列操作。而对于你女朋友来说，她只需要想到对象，叫对象帮她充话费，她并不关心你是如何帮她充值的。

面向对象编程(Object Oriented Programming，缩写OOP)，是一种程序设计思想，OOP把对象作为程序的基本单元，也就是说，在面向对象编程的世界里，万事万物皆对象。一种事物对应一个类，事物的属性定义为变量，事物的行为写成方法，把封装好的对象对外提供访问，提高了软件的重用性、灵活性和扩展性。


| 事物                   | 类                   |
| ---------------------- | -------------------- |
| 属性：该事物的描述信息 | 成员变量：事物的属性 |
| 行为：该事物能够做什么 | 成员方法：事物的行为 |



#### 创建和使用类

使用类可以模拟任何东西，类里可以包含信息（姓名、年龄）和行为（翻滚、蹲下）。



##### 创建Dog类

```
#9.1.1创建Dog类，赋予每条狗sit()和roll_over()能力；

class Dog():
    """一次模拟小狗的简单尝试"""
    def __init__(self, name, age):
        """初始化属性name和age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗被命令蹲下"""
        print(self.name.title() + " is now sitting."


    def roll_over(self):
        """模拟小狗被命令打滚"""
        print(self.name.title() + " rolled over.")

```

步骤：

1、class Dog()。定义一个Dog类，根据python，首字母大写的名称指的是类。括号为空说明要从空白创建这个类。

2、定义类后，需要使用文档字符串来阐述该类的功能。"""

3、类中的函数都称为方法。

  `__init_（）`，开头末尾都有两个下划线，避免python默认方法与普通方法发生名称冲突。

4、`__init__()`定义包含三个形参,self,name,age。

​	self是必不可少，并且其他形参的最前面。python调用`__init__()`方法来创建Dog实例时，将自动传入实参self。每个与类相关联的方法调用都自动传递实参self，它是一个指向实例本身的引用，让实例能够访问类中的属性和方法。

5、定义两个变量都有前缀self，self为前缀的变量都可供所有方法使用。

​	self.name = name获取存储在形参name的值，并将其存储到变量name中，然后该变量被关联到当前创建的实例。通过实例访问的变量成为属性。



##### 在python2.7创建类

```
#python2.7中创建类括号包括object
class ClassName(object):
    --snip--
```



##### 根据类创建实例

可将类视为有关如何创建实例的说明，例如Dog（）类就是一系列说明。

```
#9.1.2根据类创建实例

class Dog():
    """一次模拟小狗的简单测试"""

    def  __init__(self, name, age):
        """初始化属性name和age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + "is now sitting.")\


    def roll_over(self):
        """模拟小狗被命令打滚"""
        print(self.name.title() + " rolled over!")


#1、创建实例，名为willie，年龄6岁的小狗。
#2、实参调用Dog类中的方法__init__()。
#3、方法__init__()创建一个表示特定的小狗实例，并将实参设置属性的值name和age。
#4、方法__init__()并未显示return语句，但python自动返回这个小狗实例，并存储在my_dog变量
#5、一般首字母大写为类，小写名称为实例。
my_dog = Dog('willie', 6)

#访问类中的属性。my_dog.name
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

```

##### 调用方法

```
#9.1.2根据类创建实例

class Dog():
    """一次模拟小狗的简单测试"""

    def  __init__(self, name, age):
        """初始化属性name和age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + " is now sitting.")\


    def roll_over(self):
        """模拟小狗被命令打滚"""
        print(self.name.title() + " rolled over!")


#1、创建实例，名为willie，年龄6岁的小狗。
#2、实参调用Dog类中的方法__init__()。
#3、方法__init__()创建一个表示特定的小狗实例，并将实参设置属性的值name和age。
#4、方法__init__()并未显示return语句，但python自动返回这个小狗实例，并存储在my_dog变量
#5、一般首字母大写为类，小写名称为实例。
my_dog = Dog('willie', 6)

#句点表示法调用Dog类定义的任何方法；
my_dog.sit()
my_dog.roll_over()

```



##### 创建多个实例

```
#9.1.2-2创建多个实例

class Dog():
    """一次模拟小狗的简单测试"""

    def  __init__(self, name, age):
        """初始化属性name和age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗被命令时蹲下"""
        print(self.name.title() + " is now sitting.")\


    def roll_over(self):
        """模拟小狗被命令打滚"""
        print(self.name.title() + " rolled over!")


#1、创建实例，名为willie，年龄6岁的小狗。
#2、实参调用Dog类中的方法__init__()。
#3、方法__init__()创建一个表示特定的小狗实例，并将实参设置属性的值name和age。
#4、方法__init__()并未显示return语句，但python自动返回这个小狗实例，并存储在my_dog变量
#5、一般首字母大写为类，小写名称为实例。
my_dog = Dog('willie', 6)

#访问类中的属性。my_dog.name
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

my_dog.sit()


#创建一个your_dog实例
your_dog = Dog('feichou', 25)
print("Your dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")
your_dog.roll_over()

```



##### 练习

```
#9-1餐馆

class Restaurant():
    def __init__(self, restaurant, cuisine_type):
        self.restaurant = restaurant
        self.cuisine_type = cuisine_type


    def describe_restaurant(self):
        print(self.restaurant.title() + " restauran is so good!")


    def open_restaurant(self):
        print(self.restaurant.title() + " restaran delicious " +
              self.cuisine_type.title() + ".")


foods = Restaurant('kuaileyuan', 'chicken')
foods.describe_restaurant()
foods.open_restaurant()

#9-2增加餐馆调用
two_foods = Restaurant('zhengongfu', 'meat pie')
two_foods.describe_restaurant()

three_foods = Restaurant('miandingxiang', 'face')
three_foods.describe_restaurant()





#9-3用户

class User():
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


    def describe_user(self):
        full_name = self.first_name + " " + self.last_name
        print("Hi, " + full_name)

    def greet_user(self):
        print("You're " + str(self.age) + " years old this year.")


feichou = User('zhang', 'wenchou', 25)
feichou.describe_user()
feichou.greet_user()

tom = User('liang', 'weijie', 27)
tom.describe_user()
tom.greet_user()
```



#### 使用类和实例

可以使用类模拟现实世界许多情景。相同的类可以有不同的属性，可以修改实例的属性，也可以编写方法以特定的方式进行修改。

```
#9.2.1 Car类

class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year


    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

```



##### 给属性指定默认值

类总每个属性都必须有初始值，哪怕这个值是0或空字符串。

在`__init__()`方法里指定属性的初始值也可以，类似形参默认值，指定后就无需提供实参，默认使用初始值。

```
#9.2.2 给属性指定默认值

#增加odometer_reading属性
#增加read_odometer()方法

class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + self.model
        return long_name

    def read_odometer(self):
        """打印一条指出汽车的里程信息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

```



##### 修改属性的值

三种不同方式属性的值：

1、直接修改

2、通过方法进行修改

3、通过方法进行递增



直接修改：

```
#9.2.3 修改属性的值

#1、直接修改属性的值
#增加odometer_reading属性
#增加read_odometer()方法

class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + self.model
        return long_name

    def read_odometer(self):
        """打印一条指出汽车的里程信息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

#直接修改属性值
my_new_car.odometer_reading = 23
my_new_car.read_odometer()
```



通过方法修改属性值：

```
#9.2.3-1 修改属性的值

#2、通过方法修改属性的值
#增加odometer_reading属性
#增加read_odometer()方法

class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + self.model
        return long_name

    def read_odometer(self):
        """打印一条指出汽车的里程信息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """将里程表读书设置为指定的值"""
        self.odometer_reading = mileage


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

#通过方法传递属性的值
my_new_car.update_odometer(23)
my_new_car.read_odometer()

```

增加判断语句

```
#9.2.3-3 修改属性的值,并且增加判断语句

#2、通过方法修改属性的值，并且增加判断语句
#增加odometer_reading属性
#增加read_odometer()方法

class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        #设置初始值为23
        self.odometer_reading = 23

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + self.model
        return long_name

    def read_odometer(self):
        """打印一条指出汽车的里程信息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    
    #增加判断语句，避免传递的数值小于原本的；
    def update_odometer(self, mileage):
        """
        将里程表读书设置为指定的值
        禁止将里程表读书往回调
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

#传递值小于默认值，将提示
my_new_car.update_odometer(10)


```



##### 通过方法对属性的值进行递增

```
#9.2.3-3 修改属性的值,并且增加判断语句

#2、通过方法修改属性的值，并且增加判断语句
#增加odometer_reading属性
#增加read_odometer()方法

class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + self.model
        return long_name

    def read_odometer(self):
        """打印一条指出汽车的里程信息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    
    #增加判断语句，避免传递的数值小于原本的；
    def update_odometer(self, mileage):
        """
        将里程表读书设置为指定的值
        禁止将里程表读书往回调
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")


    def increment_odometer(self, miles):
        """将里程表读书增加指定的量"""
        self.odometer_reading += miles

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

#通过方法传递属性的值
my_new_car.update_odometer(23500)
my_new_car.read_odometer()

#在原有值上递增
my_new_car.increment_odometer(100)
my_new_car.read_odometer()

```



##### 练习

```
#9-4练习 餐馆

class Restaurant():
    def __init__(self, restaurant, cuisine_type):
        self.restaurant = restaurant
        self.cuisine_type = cuisine_type
        self.number_served = 0


    def describe_restaurant(self):
        """告知餐厅很好吃"""
        print(self.restaurant.title() + " restauran is so good!")


    def open_restaurant(self):
        """告知餐厅有什么吃的"""
        print(self.restaurant.title() + " restaran delicious " +
              self.cuisine_type.title() + ".")
    

    def set_number_served(self):
        """计算今天有多少个人来餐厅"""
        print("There today " + str(self.number_served) + " people in this restaurant.")
    

    def increment_number_served(self, sum):
        """递增人数，并且算出目前总共多少人"""
        self.number_served += sum
        print("There sum " + str(self.number_served) + " pople in this restaurant.")

foods = Restaurant('kuaileyuan', 'chicken')
foods.describe_restaurant()
foods.open_restaurant()
foods.set_number_served()
foods.increment_number_served(70)


#9-5
#用户

class User():
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0


    def describe_user(self):
        """显示全名"""
        full_name = self.first_name + " " + self.last_name
        print("Hi, " + full_name)

    def greet_user(self):
        """显示年龄"""
        print("You're " + str(self.age) + " years old this year.")


    def increment_login_attempts(self):
        """增加登陆次数"""
        self.login_attempts += 1
        print("Total " + str(self.login_attempts) + " of logins")


    def reset_login_attempts(self):
        """重置登陆次数"""
        self.login_attempts = 0
        print("Reset Login number.")


feichou = User('zhang', 'wenchou', 25)
feichou.describe_user()
feichou.greet_user()
feichou.increment_login_attempts()
feichou.increment_login_attempts()
feichou.increment_login_attempts()
feichou.increment_login_attempts()
feichou.reset_login_attempts()
print("Current login times： " + str(feichou.login_attempts))

```



#### 继承

编写类时，并非总是要从空白开始。如果要编写的类是另一个现成类的特殊版本，可使用继承。

一个类继承另一个类时，它将自动获得另一个类的所有属性和方法；

原有的类成为父类，而新类称为子类。子类继承了其父类的所有属性和方法，同时还可以定义自己的属性和方法。



##### 子类的方法`__init__()`

```
#9.3.1创建子类

class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """按年份、厂商、型号输出汽车信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()


    def read_odometer(self):
        """显示里程信息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """
        判断里程信息是否往回调整
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage

        else:
            print("You can't roll back an odometer!") 

    def increment_odometer(self, miles):
        """递增里程信息"""
        self.odometer_reading += miles

#创建子类，子类括号必须包含父类；
class ElectricCar(Car):
    """电动车的独特之处"""

    def __init__(self, make, model, year):
        """初始化父类属性"""
        #super()是一个特殊函数，帮助python将父类和子类关联起来；
        #super()让python调用父类__init__()方法，让实例包含父类所有属性；
        super().__init__(make, model, year)

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
```



##### python2.7中的继承

```
#9.3.2python2.7中的继承

class Car(object):
    --snip--

#子类括号指定父类名称;
class ElectricCar(Car):
    def __init__(self, make, model, year):
        #super()需要两个实参：子类名和对象self，帮助python将父类和子类关联起来。
        super(ElectricCar, self).__init__(make, model, year)
        --snip--

```



##### 给子类定义属性和方法

让一个类继承另一个类后，可添加区分子类和父类所需的新属性和方法。

```
class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """按年份、厂商、型号输出汽车信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()


    def read_odometer(self):
        """显示里程信息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """
        判断里程信息是否往回调整
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage

        else:
            print("You can't roll back an odometer!") 

    def increment_odometer(self, miles):
        """递增里程信息"""
        self.odometer_reading += miles

#创建子类，子类括号必须包含父类；
class ElectricCar(Car):
    """电动车的独特之处"""

    def __init__(self, make, model, year):
        """初始化父类属性"""
        #super()是一个特殊函数，帮助python将父类和子类关联起来；
        #super()让python调用父类__init__()方法，让实例包含父类所有属性；
        super().__init__(make, model, year)
        #增加子类属性
        self.battery_size = 70
    
    #增加电动车独有的电池信息
    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + " =kWh battery.")

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

```



##### 重写父类方法

```
#9.3.4 重写父类的方法
#Car类增加油箱容量方法fule_gas_tank，并且ElectricCar类也增加fule_gas_tank。
#ElectricCar类与Car父类都存在fule_gas_tank，子类将不考虑父类的方法，而是用子类的方法。

class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.fule_capactiy = 55

    def get_descriptive_name(self):
        """按年份、厂商、型号输出汽车信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()


    def read_odometer(self):
        """显示里程信息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """
        判断里程信息是否往回调整
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage

        else:
            print("You can't roll back an odometer!") 

    def increment_odometer(self, miles):
        """递增里程信息"""
        self.odometer_reading += miles

    def fill_gas_tank(self, fule):
        """增加油箱显示"""
        self.fule_capactiy = fule
        print("Fule Capactiy is : " + str(self.fule_capactiy) + "L.")

#创建子类，子类括号必须包含父类；
class ElectricCar(Car):
    """电动车的独特之处"""

    def __init__(self, make, model, year):
        """初始化父类属性"""
        #super()是一个特殊函数，帮助python将父类和子类关联起来；
        #super()让python调用父类__init__()方法，让实例包含父类所有属性；
        super().__init__(make, model, year)
        #增加子类属性
        self.battery_size = 70
    
    #增加电动车独有的电池信息
    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + " =kWh battery.")

    def fill_gas_tank(self):
        """将提示电动车没有油箱"""
        print("This car doesn't need a gas tank!")

#使用父类创建实例
my_car = Car('toyota', 'levin', 2016)
print(my_car.get_descriptive_name())
my_car.fill_gas_tank(45)

#使用子类创建实例
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.fill_gas_tank()

```

使用继承，可以让子类保留父类继承而来的精华，也可以剔除不需要的方法。



##### 将实例用作属性

```
#9.3.5将实例用作属性
#创建Battery类，将电瓶的属性都归于此类，并用该类用作属性值；
class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.fule_capactiy = 55

    def get_descriptive_name(self):
        """按年份、厂商、型号输出汽车信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()


    def read_odometer(self):
        """显示里程信息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """
        判断里程信息是否往回调整
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage

        else:
            print("You can't roll back an odometer!") 

    def increment_odometer(self, miles):
        """递增里程信息"""
        self.odometer_reading += miles

    def fill_gas_tank(self, fule):
        """增加油箱显示"""
        self.fule_capactiy = fule
        print("Fule Capactiy is : " + str(self.fule_capactiy) + "L.")

#将Battery方法作为独立的类，这样便于添加更多关于电瓶的细节；

class Battery():
    """一次模拟电动汽车点评的简单尝试"""

    def __init__(self, battery_size=70):
        """初始化电瓶属性"""
        self.battery_size = battery_size
    
    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")


class ElectricCar(Car):
    """电动汽车的独特之处"""

    def __init__(self, make, model, year):
        """
        初始化父类的属性，再初始化电动汽车特有的属性
        """
        super().__init__(make, model, year)
         #将类作为属性值；
        self.battery = Battery()


my_tesla = ElectricCar('tesla', 'model s', 2016)

print(my_tesla.get_descriptive_name())
#调用battery类中的describe_battery方法；
my_tesla.battery.describe_battery()

```



在Battery方法里添加续航里程判断：

```
#9.3.5将实例用作属性
#在Battery类中添加判断电瓶续航

class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.fule_capactiy = 55

    def get_descriptive_name(self):
        """按年份、厂商、型号输出汽车信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()


    def read_odometer(self):
        """显示里程信息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """
        判断里程信息是否往回调整
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage

        else:
            print("You can't roll back an odometer!") 

    def increment_odometer(self, miles):
        """递增里程信息"""
        self.odometer_reading += miles

    def fill_gas_tank(self, fule):
        """增加油箱显示"""
        self.fule_capactiy = fule
        print("Fule Capactiy is : " + str(self.fule_capactiy) + "L.")

#将Battery方法作为独立的类，这样便于添加更多关于电瓶的细节；

class Battery():
    """一次模拟电动汽车点评的简单尝试"""

    def __init__(self, battery_size=70):
        """初始化电瓶属性"""
        self.battery_size = battery_size
    
    def get_range(self):
        """打印一条信息，指出电瓶的续航里程"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270         
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)
    
    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")


class ElectricCar(Car):
    """电动汽车的独特之处"""

    def __init__(self, make, model, year):
        """
        初始化父类的属性，再初始化电动汽车特有的属性
        """
        super().__init__(make, model, year)
         #将类作为属性值；
        self.battery = Battery()


my_tesla = ElectricCar('tesla', 'model s', 2016)

print(my_tesla.get_descriptive_name())
#调用battery类中的get_range方法；
my_tesla.battery.battery_size = 85
my_tesla.battery.get_range()

```



#### 练习

```
#9-6冰淇淋小店

class Restaurant():
    """模拟一个餐厅，并且该餐厅提供美食"""
    def __init__(self, restaurant, cuisine_type):
        self.restaurant = restaurant
        self.cuisine_type = cuisine_type


    def describe_restaurant(self):
        """输出该餐厅就是好"""
        print(self.restaurant.title() + " restauran is so good!")


    def open_restaurant(self):
        """输出该餐厅有什么美食"""
        print(self.restaurant.title() + " restaran delicious " +
              self.cuisine_type.title() + ".")


class IceCreamStand(Restaurant):
    """创建雪糕店类"""
    def __init__(self, restaurant, cuisine_type):
        """初始化父类属性"""
        super().__init__(restaurant, cuisine_type)
        #添加口味
        self.flavors = ['chocolates', 'vanilla', 'green tea']

#创建雪糕店实例
ice = IceCreamStand('kuaileyuan', 'chicken')
ice.open_restaurant()
for i in ice.flavors:
    print("The taste of ice cream is " + i)




#9-7管理员

class User():
    """模拟用户登录次数"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0


    def describe_user(self):
        """显示全名"""
        full_name = self.first_name + " " + self.last_name
        print("Hi, " + full_name.title())

    def greet_user(self):
        """显示年龄"""
        print("You're " + str(self.age) + " years old this year.")


    def increment_login_attempts(self):
        """增加登陆次数"""
        self.login_attempts += 1
        print("Total " + str(self.login_attempts) + " of logins")


    def reset_login_attempts(self):
        """重置登陆次数"""
        self.login_attempts = 0
        print("Reset Login number.")


class Admin(User):
    """模拟admin用户可以执行什么"""
    def __init__(self, first_name, last_name, age):
        """初始化父类属性"""
        super().__init__(first_name, last_name, age)
        #增加privileges属性，存储admin可执行任务的列表；
        self.privileges = ['can add post', 'can delete post', 'can ban user']
       
    def show_privileges(self):
        """显示admin管理权限"""
        for i in self.privileges:
            self.describe_user()
            print("You " + i)


admin_user = Admin('zhang', 'wenchou', 25)
admin_user.show_privileges()



#9-8权限
#将实例用作属性

class User():
    """模拟用户登录次数"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0


    def describe_user(self):
        """显示全名"""
        full_name = self.first_name + " " + self.last_name
        print("Hi, " + full_name.title())

    def greet_user(self):
        """显示年龄"""
        print("You're " + str(self.age) + " years old this year.")


    def increment_login_attempts(self):
        """增加登陆次数"""
        self.login_attempts += 1
        print("Total " + str(self.login_attempts) + " of logins")


    def reset_login_attempts(self):
        """重置登陆次数"""
        self.login_attempts = 0
        print("Reset Login number.")


class Admin(User):
    """模拟admin用户可以执行什么"""
    def __init__(self, first_name, last_name, age):
        """初始化父类属性"""
        super().__init__(first_name, last_name, age)
        #增加privileges属性，存储admin可执行任务的列表；
        self.privileges = Privileges()

class Privileges():
    """模拟admin可执行列表"""
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']   

    def show_privileges(self):
        """显示admin管理权限"""
        for i in self.privileges:
            #暂时无法像9-7那样调用其他类方法及属性；
            print("You " + i)


admin_user = Admin('zhang', 'wenchou', 25)
admin_user.privileges.show_privileges()



#9-9电瓶升级
#在Battery增加upgrade_battery()方法，判断电瓶容量;

class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.fule_capactiy = 55

    def get_descriptive_name(self):
        """按年份、厂商、型号输出汽车信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()


    def read_odometer(self):
        """显示里程信息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """
        判断里程信息是否往回调整
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage

        else:
            print("You can't roll back an odometer!") 

    def increment_odometer(self, miles):
        """递增里程信息"""
        self.odometer_reading += miles

    def fill_gas_tank(self, fule):
        """增加油箱显示"""
        self.fule_capactiy = fule
        print("Fule Capactiy is : " + str(self.fule_capactiy) + "L.")

#将Battery方法作为独立的类，这样便于添加更多关于电瓶的细节；

class Battery():
    """一次模拟电动汽车点评的简单尝试"""

    def __init__(self, battery_size=70):
        """初始化电瓶属性"""
        self.battery_size = battery_size
    
    def get_range(self):
        """打印一条信息，指出电瓶的续航里程"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270         
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)
    
    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")
    
    def upgrade_battery(self):
        """检查电瓶容量及更新他的容量"""
        if self.battery_size != 85:
            self.battery_size = 85

class ElectricCar(Car):
    """电动汽车的独特之处"""

    def __init__(self, make, model, year):
        """
        初始化父类的属性，再初始化电动汽车特有的属性
        """
        super().__init__(make, model, year)
         #将类作为属性值；
        self.battery = Battery()


my_tesla = ElectricCar('tesla', 'model s', 2016)

print(my_tesla.get_descriptive_name())
#调用battery类中的get_range方法；
my_tesla.battery.get_range()

#调用电瓶升级;
my_tesla.battery.upgrade_battery()

my_tesla.battery.get_range()


```



#### 导入类

python允许将类存储在模块里，然后在主程序中导入所需的模块。



##### 导入单个类

```
#9.4.1导入单个类
#1、将Car类存储为一个模块car.py然后进行导入；
#2、from car import Car，导入Car类

class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.fule_capactiy = 55

    def get_descriptive_name(self):
        """按年份、厂商、型号输出汽车信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()


    def read_odometer(self):
        """显示里程信息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """
        判断里程信息是否往回调整
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage

        else:
            print("You can't roll back an odometer!") 

    def increment_odometer(self, miles):
        """递增里程信息"""
        self.odometer_reading += miles

    def fill_gas_tank(self, fule):
        """增加油箱显示"""
        self.fule_capactiy = fule
        print("Fule Capactiy is : " + str(self.fule_capactiy) + "L.")

```

2、导入模块

```
#9.4.1导入模块car.py

from car import Car

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

```

导入类是一种有效的编程方式，让主程序文件变得整洁而易于阅读，而专注主程序的高级逻辑。



##### 一个模块存储多个类

```
#9.4.2在一个模块中存储多个类,car_2.py
#在一个模块存储多个类后，然后指定单独的ElectricCar类


"""一组用于表示燃油气和电动汽车的类"""

class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.fule_capactiy = 55

    def get_descriptive_name(self):
        """按年份、厂商、型号输出汽车信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()


    def read_odometer(self):
        """显示里程信息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """
        判断里程信息是否往回调整
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage

        else:
            print("You can't roll back an odometer!") 

    def increment_odometer(self, miles):
        """递增里程信息"""
        self.odometer_reading += miles

    def fill_gas_tank(self, fule):
        """增加油箱显示"""
        self.fule_capactiy = fule
        print("Fule Capactiy is : " + str(self.fule_capactiy) + "L.")

#将Battery方法作为独立的类，这样便于添加更多关于电瓶的细节；

class Battery():
    """一次模拟电动汽车点评的简单尝试"""

    def __init__(self, battery_size=70):
        """初始化电瓶属性"""
        self.battery_size = battery_size
    
    def get_range(self):
        """打印一条信息，指出电瓶的续航里程"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270         
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)
    
    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")


class ElectricCar(Car):
    """电动汽车的独特之处"""

    def __init__(self, make, model, year):
        """
        初始化父类的属性，再初始化电动汽车特有的属性
        """
        super().__init__(make, model, year)
         #将类作为属性值；
        self.battery = Battery()

```

2、导入指定类

```
#9.4.2在一个模块中存储多个类
#在一个模块存储多个类后，然后指定单独的ElectricCar类

from car_2 import ElectricCar

my_tesla = ElectricCar('tesla', 'model s', 2016)
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

```



##### 一个模块导入多个类

`from car import Car, ElectricCar`



##### 导入整个模块

```
#9.4.4导入整个模块

#导入整个模块，使用句点表示法访问需要的类；
import car_2

my_beetle = car_2.Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = car_2.ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())

```



##### 导入模块中的所有类

`from module_name import *`

不推荐使用import *方法。
1、没有明确指出使用模块中哪些类。
2、担心与其他类重名，导致难以诊断错误。

推荐使用import module_name导入整个模块
1、使用module_name.class_name访问类。明确知道程序哪个位置使用模块。
2、避免名字冲突。



##### 在一个模块中导入另一个模块

为避免模块太大，有时候需要将类分散到多个模块中。

```
#9.4.6在一个模块中导入另一个模块
#首先将两个类存储在一个模块里


"""一组可用于表示电动汽车的类"""
#导入Car类，因为ElectricCar需要访问其父类Car，不然将会导致错误；
from car import Car
class Battery():
    """一次模拟电动汽车点评的简单尝试"""

    def __init__(self, battery_size=70):
        """初始化电瓶属性"""
        self.battery_size = battery_size
    
    def get_range(self):
        """打印一条信息，指出电瓶的续航里程"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270         
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)
    
    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")


class ElectricCar(Car):
    """电动汽车的独特之处"""

    def __init__(self, make, model, year):
        """
        初始化父类的属性，再初始化电动汽车特有的属性
        """
        super().__init__(make, model, year)
         #将类作为属性值；
        self.battery = Battery()


```

2、创建一个my_cars_2.py，导入模块需要的类

```
#9.4.6在一个模块中导入另一个模块
#2、导入模块中相关类，并创建实例

from car import Car
from electric_car import ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())

```





##### 自定义工作流程

建议：

1、先尽可能在一个文件完成所有工作，再将类转移到独立模块中。

2、一开始就尝试类存储在模块中，让代码更为组织有序。



#### 练习

```
#9-10将Restaurant存储在一个模块restaurant中；
"""一组餐馆评价"""

class Restaurant():
    def __init__(self, restaurant, cuisine_type):
        self.restaurant = restaurant
        self.cuisine_type = cuisine_type
        self.number_served = 0


    def describe_restaurant(self):
        """告知餐厅很好吃"""
        print(self.restaurant.title() + " restauran is so good!")


    def open_restaurant(self):
        """告知餐厅有什么吃的"""
        print(self.restaurant.title() + " restaran delicious " +
              self.cuisine_type.title() + ".")
    

    def set_number_served(self):
        """计算今天有多少个人来餐厅"""
        print("There today " + str(self.number_served) + " people in this restaurant.")
    

    def increment_number_served(self, sum):
        """递增人数，并且算出目前总共多少人"""
        self.number_served += sum
        print("There sum " + str(self.number_served) + " pople in this restaurant.")
        
 2、创建my_restaurant,导入Restaurant，并创建实例
 
 #9-10将Restaurant存储在一个模块中；
#导入模块restaurant中的Restaurant类，并创建实例;

from restaurant import Restaurant

foods = Restaurant('kuaileyuan', 'chicken')
foods.describe_restaurant()

______

#9-11一个模块包含多个类
#将9-8所有类存储在一个模块里，user.py
"""用户权限"""

class User():
    """模拟用户登录次数"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0


    def describe_user(self):
        """显示全名"""
        full_name = self.first_name + " " + self.last_name
        print("Hi, " + full_name.title())

    def greet_user(self):
        """显示年龄"""
        print("You're " + str(self.age) + " years old this year.")


    def increment_login_attempts(self):
        """增加登陆次数"""
        self.login_attempts += 1
        print("Total " + str(self.login_attempts) + " of logins")


    def reset_login_attempts(self):
        """重置登陆次数"""
        self.login_attempts = 0
        print("Reset Login number.")


class Admin(User):
    """模拟admin用户可以执行什么"""
    def __init__(self, first_name, last_name, age):
        """初始化父类属性"""
        super().__init__(first_name, last_name, age)
        #增加privileges属性，存储admin可执行任务的列表；
        self.privileges = Privileges()

class Privileges():
    """模拟admin可执行列表"""
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']   

    def show_privileges(self):
        """显示admin管理权限"""
        for i in self.privileges:
            
            print("You " + i)

2、导入模块及创建实例
#9-11将9-8所有类存储在user.py模块里，然后导入并创建实例

from user import Admin

admin_user = Admin('zhang', 'wenchou', 25)
admin_user.privileges.show_privileges()


——————


#9-12多个模块
#User存储一个模块里,user_only.py
#Privileges和Admin存储admin_user.py

"""显示用户信息"""

class User():
    """模拟用户登录次数"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0


    def describe_user(self):
        """显示全名"""
        full_name = self.first_name + " " + self.last_name
        print("Hi, " + full_name.title())

    def greet_user(self):
        """显示年龄"""
        print("You're " + str(self.age) + " years old this year.")


    def increment_login_attempts(self):
        """增加登陆次数"""
        self.login_attempts += 1
        print("Total " + str(self.login_attempts) + " of logins")


    def reset_login_attempts(self):
        """重置登陆次数"""
        self.login_attempts = 0
        print("Reset Login number.")


#9-12多个模块
#User存储一个模块里,user_only.py
#Privileges和Admin存储admin_user.py
#因为Admin需要访问User父类，需要导入

from user_only import User

"""admin权限集"""

class Admin(User):
    """模拟admin用户可以执行什么"""
    def __init__(self, first_name, last_name, age):
        """初始化父类属性"""
        super().__init__(first_name, last_name, age)
        #增加privileges属性，存储admin可执行任务的列表；
        self.privileges = Privileges()

class Privileges():
    """模拟admin可执行列表"""
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']   

    def show_privileges(self):
        """显示admin管理权限"""
        for i in self.privileges:
            
            print("You " + i)


#9-12多个模块
#User存储一个模块里,user_only.py
#Privileges和Admin存储admin_user.py
#创建admin实例

from admin_user import Admin

admin_user = Admin('zhang', 'wenchou', 25)
admin_user.privileges.show_privileges()


```



#### 标准库

python标准库是一组模块，安装的python都包含它。

collections类中的OrderedDict类：可以保持字典添加顺序。

```
#9.5标注库
#collections类中的OrdereDict方法，可以保持字典添加顺序；

#导入OrdereDict方法
from collections import OrderedDict

#OrdereDict创建一个空的有序字典，并存储在favorite_languages中；
favorite_languages = OrderedDict()

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
    language.title() + ".")

```

##### 练习

```
#9-14创建骰子
#导入随机模块
from random import randint

"""一个骰子游戏"""

class Die():
    #初始化order次数，sides面数属性;
    def __init__(self, order, sides=6):
        self.order = order
        self.sides = sides
    
    def roll_die(self):
        """投掷次数及输出投掷数字"""
        while self.order:
            x = randint(1, self.sides)
            print("roll number is " + str(x))
            self.order -= 1

#创建一个6面骰子，投掷10次
play_roll = Die(10)
play_roll.roll_die()
print("-" * 10)

#创建一个10面骰子，投掷10次
play_roll = Die(10, 10)
play_roll.roll_die()
print("-" * 10)

#创建一个20面骰子，投掷10次
play_roll = Die(10, 20)
play_roll.roll_die()
print("-" * 10)

```

python module of the week:http://pymotw.com可以了解python标准库的资源网站。



#### 类编码风格

1、类命名应采用驼峰命名法。

 - 即将类名中的每个单词首字母都大写，而不使用下划线。
 - 实例名和模块名都采用小写格式，并在单词之间加上下划线。

2、每个模块、类或方法后面都应紧跟一个文档字符串。
 - 文档字符串简要地描述类的功能。

3、可使用空行组织代码，带不能滥用。
 - 类中科使用一个空行隔开。
 - 模块中科使用两个空行隔开。

 4、导入标准库中模块和自定义模块顺序。
 - 先导入标准库，再加一个空格，后续再导入自定义模块。



#### 小结

1、如何编写类。
2、如何使用属性在类中存储信息。
3、如何编写`__init__()。`
4、如何创建实例。
5、继承可简化工作。
6、将类用作另一个类属性。
7、如何修改实例属性，直接修改或通过方法修改。
8、如何将类存储在模块里。
9、使用标准库。
10、编写类的语法。



### 文件和异常

#### 文件中读取数据

```
#1、open函数打开pidigits.txt，存储在file_object中。
#2、使用read函数，读取文件所有内容并赋值给contents；
#3、输出内容；
#4、with不需要访问文件后调用close（）关闭。
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    #read()到达文件末尾会返回一个空字符串，所以需要删除；
    print(contents.rstrip())

```



##### 文件路径

open（）函数打开文件，是从当前运行文件的文件夹里寻找文件。

相对路径：位置相对于当前运行的程序所在的目录中寻找文件。

`with open('text_files/filename.txt') as file_object:`



绝对路径：文件不在当前运行的程勋所在目录里，提供详细的文件路径。

```
file_path = '/home/text_file.txt'
with open(file_path) as file_object:
```



在win系统里，文件路径是反斜杠（\），而不是斜杠（/）。由于win系统下路径为反斜杠，所以需要在开头加r。

```
file_path = r'C:\text_files\pi_digits.txt'
with open(file_path) as file_object:
```



##### 逐行读取

```
#文件赋值给变量filename；
filename = 'pi_digits.txt'

#使用open打开文件，并且将内容对象存储到变量file_object中；
with open(filename) as file_object:
    #for循环导出每一行数字；
    for line in file_object:
        #每行末尾都有一个隐藏的换行符，由于print会产生一个换行符，所以总共两个；
        #使用rstrip()删除空格；
        print(line.rstrip())

```



##### 各行内容的列表

```
#10.1.4包含文件中各行的列表
#文件赋值给变量filename；
filename = 'pi_digits.txt'

#使用open打开文件，并且将内容对象存储到变量file_object中；
with open(filename) as file_object:
    #readlines()从文件中读取每一行，并存储在一个列表中；
    lines = file_object.readlines()
    #for循环导出每一行数字；
    for line in lines:
        #每行末尾都有一个隐藏的换行符，由于print会产生一个换行符，所以总共两个；
        #使用rstrip()删除空格；
        print(line.rstrip())

```



##### 使用文件内容

```
#10.1.5使用文件内容
#文件赋值给变量filename；
filename = 'pi_digits.txt'

#使用open打开文件，并且将内容对象存储到变量file_object中；
with open(filename) as file_object:
    #readlines()从文件中读取每一行，并存储在一个列表中；
    lines = file_object.readlines()

    pi_string = ''
    #for循环导出每一行数字；
    for line in lines:
        #删除左右空格；
        pi_string += line.strip()
    
    print(pi_string)
    #计算pi_string长度,小数点算一位。
    print(len(pi_string))
    

```

如果读取是数字，需要该内容来使用，必须使用int（）转换或float（）转换。



输出百万位圆周率长度

```
#10.1.6包含一百万位大型的文件
#文件赋值给变量filename；
filename = 'pi_million_digits.txt'

#使用open打开文件，并且将内容对象存储到变量file_object中；
with open(filename) as file_object:
    #readlines()从文件中读取每一行，并存储在一个列表中；
    lines = file_object.readlines()

    pi_string = ''
    #for循环导出每一行数字；
    for line in lines:
        pi_string += line.strip()
    
    #使用切片，输出前52位数；
    print(pi_string[:52] + "...")
    #计算pi_string长度
    print(len(pi_string))

```



判断生日是否存在圆周率中

```
#10.1.7圆周率包含生日
#文件赋值给变量filename；
filename = 'pi_million_digits.txt'

#使用open打开文件，并且将内容对象存储到变量file_object中；
with open(filename) as file_object:
    #readlines()从文件中读取每一行，并存储在一个列表中；
    lines = file_object.readlines()

    pi_string = ''
    #for循环导出每一行数字；
    for line in lines:
        pi_string += line.strip()
    
    birthday = input("Enter your birthday, in the form mmddyy:")
    if birthday in pi_string:
        print("Your birthday apperars in the first million digits of pi!")
    else:
        print("Your birthday does not appear in the fist million digits of pi.")

```

##### 练习

```
#10-1

filename = 'learning_python.txt'

with open(filename) as file_object:
    learns = file_object.read()
    print(learns.rstrip())


————————
#10-1-1
#遍历对象
filename = 'learning_python.txt'

with open(filename) as file_object:
    for line in file_object:
        new_line = line.rstrip()
        print(new_line('Python', 'C'))

————————
#10-1-2
#各行存储列表中
filename = 'learning_python.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
    for line in lines:
        print(line.rstrip())
    print(lines)

————————
#10-2 replace()替换文字
filename = 'learning_python.txt'

with open(filename) as file_object:
    for line in file_object:
        new_line = line.rstrip()
        print(new_line.replace('Python', 'C'))

```

