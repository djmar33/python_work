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