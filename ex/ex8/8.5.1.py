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
