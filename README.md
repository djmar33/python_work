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

### 3.1列表

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

#### 4操作列表

##### for语句

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

##### range()函数

range（）能够轻松地生成一系列的数字。

```
#4.3.1 range()函数使用

#打印一系列数字，range函数里1,5，表示生成1-4范围的数字，并不会打印数字5；
for value in range(1,5):
    print(value)
```

###### 创建数字列表

使用list（）将range（）的结果直接转为列表。

```
#4.3.2 创建数字列表
number = list(range(1,5))
print(number)
```

###### 指定步长

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

##### 切片

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

###### 遍历切片

```
#4.4.2遍历切片
#使用遍历，输出列表前三名球员；
players = ['charles','martina','michael','florence','eli']
print("Here are the fist three players on my team:")
for player in players[0:4]:
    print(player.title())

```

###### 复制列表

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

##### 元组

python将不能修改的值称为不可变的，而不不可变的列表称为元组。

###### 定义元组

元组看起来犹如列表，但使用的是圆括号而不是方括号。定义元组后，可以使用索引来访问其元素，像访问列表一样。

###### 遍历元组的所有值

元组也可以像列表一样使用for循环遍历每个元素。

```
foods = ('烧鸡','咸鱼肉饼','酱油鸭','白切鸡','鳄鱼汤')

#使用for遍历元组

for food in foods:
    print(food)
```



###### 修改元组元素的值

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

#### 5 if语句

if语句让你能够检查程序当前状态，并据此采取相应措施。

###### 简单示例

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

##### if-else语句

判断条件测试通过执行一个操作，若没有通过，将执行另外一个操作。

###### 简单示例

```
#5.3.2 if-else语句
age = 17
if age >= 18:
	print("你年龄满足投票。")
	print("你登记投票了吗？")
else:
	print("你年龄未满足投票资格啊，小弟弟！")

```

##### if-elif-else语句

依次检查每个条件，否则将执行else操作。

###### 简单示例

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

##### 多个elif语句

###### 简单示例

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

##### 省略else

python并不要求if-elif语句里一定要包含else，有时候去掉else，判断语句将会更清晰。

###### 简单示例

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

##### 测试多个条件

一般if-elif语句，都只能满足一个条件，然后执行对应的代码。但是如果需要判断每一个元素的时候，就需要使用多个if语句结构来判断。

##### 练习

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

#### 6 字典

Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。

##### 简单的字典

```
#简单的字典
#字典为花括号，第一个为key，第二个为value；
alien_0 = {'color': 'green', 'options': 5}

print(alien_0['color'])
print(alien_0['options'])

```

##### 使用字典

字典是一系列的键——值对。每个键都与一个值相关联。可将python任何对象用作字典的值。数字、字符串、列表乃至字典都可以。

键——值对是两个相关联的值。指定键的时候将返回对应的值。

键和值用冒号分隔。键——值对 用逗号分隔。

字典不限键——值对数量。

##### 访问字典的值

获取键对应的值，输入字典名字加方括号的键，将会返回对应的值。

```
alien_0 = {'color': 'green', 'options': 5}
#字典名加方括号内的键；
print(alien_0['color'])
```

##### 添加键——值对

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

##### 创建空字典

```
#创建一个空字典
alien_0 = {}
```

##### 修改字典键的值

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

##### 删除键--值对

```
#删除键--值对
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

#删除color这个键
del alien_0['color']
print(alien_0)
```

##### 字典书写建议

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

##### 练习

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

##### 遍历字典

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

##### 嵌套

有时需要将一系列字典存储在列表中，或将列表作为存储在字典中，这称为嵌套。

可以在列表中去嵌套字典、在字典中嵌套列表甚至在字典中嵌套字典。

###### 字典列表

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



###### 字典中存储字典

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

##### 小结

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



#### 7 input输入

input()函数可以让用户输入需要的信息。

工作原理：函数input（）让程序暂停运行，等待用户输入一些文本。获取用户输入后，python将其存储一个变量，方便调用。

```
#7.1函数input()的工作原理

message = input("告诉一些东西，然后我会重复告诉你：")
print(message)

```

##### 编写清晰的程序

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



##### 使用int()来获取数值输入

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

##### 求模运算符（%）

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



##### python2.7获取输入

python2.7使用raw_input()函数，而不是使用input()。



##### 练习

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

