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
