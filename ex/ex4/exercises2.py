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
