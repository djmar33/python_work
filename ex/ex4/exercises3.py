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
