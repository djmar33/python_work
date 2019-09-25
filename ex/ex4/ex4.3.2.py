#4.3.2 创建数字列表
number = list(range(1,5))
print(number)

#指定步长,生成10以下的偶数列表
number = list(range(2,11,2))
print(number)

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


#更简洁计算1~10平方数
squares = []
for value in range(1,11):
    squares.append(value ** 2)
print(squares)
