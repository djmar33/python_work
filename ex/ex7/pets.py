#7.3.2删除列表所有特定值

#创建一个包含重复元素的列表；
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']

#输出原列表所有元素；
print(pets)

#判断cat是否在列表里，如果是将执行循环；
while 'cat' in pets:
    pets.remove('cat')

#输出删除后的pets列表，所有重复元素已被删除；
print(pets)
