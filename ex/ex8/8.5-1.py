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
