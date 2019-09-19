#修改列表元素
family = ['baba','haohao','chouchou']
print(family)

family[0] = 'tom'
print(family)

#append(),添加元素

family.append('mama')
print(family)


#列表中插入元素,insert（）

family.insert(1,'yeye')
print(family)

#列表中删除元素,使用del语句

del family[1]

#使用pop()删除元素
#pop()删除列表末尾的元素，并让你能够接着使用该元素。
#列表就像一个栈，而删除列表末尾的元素相当于弹出栈顶元素。
popend_family = family.pop()
print(family)
print(popend_family)


#弹出列表中任何位置处的元素
first_popend = family[0]
print(first_popend)


#根据值删除元素,remove()
family.remove('chouchou')
print(family)


#remove()删除值接着使用，一般用来提示删除信息
del_family = 'tom'
family.remove(del_family)
print(family)
print("这个元素" + del_family.title() + "已被删除！")
