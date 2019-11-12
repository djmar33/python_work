#8.6.1创建模块
#创建一个名为pizza.py的模块，包含要导入的程序代码；

def make_pizza(size, *toppings):
    """概述要制作的比萨"""
    print("\nMaking a " + str(size) +
    "-inch pizza with the following toppings:")
    for topping in toppings:
        print("-" + topping)
