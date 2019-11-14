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
