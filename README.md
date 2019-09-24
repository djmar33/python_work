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

