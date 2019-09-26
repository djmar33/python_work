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
