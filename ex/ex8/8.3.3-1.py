#8.3.3-1字典实参变为可选

#添加一个age形参，并且指定为默认值为空；
#这样该形参如果没有传递实参，就直接使用默认值空字符；
def build_person(first_name, last_name, age=''):
    """返回一个字典，其中包含有关一个人的信息"""

    person = {'fist': first_name, 'last':last_name}

    #判断age字段是否为空，如果不是将值写入person字典对应的age key中；
    if age:
        person['age'] = age

    #键为fist，而key为形参first_name；
    return person
#使用位置实参对应形参，把信息存储在字典里;
musician = build_person('jimi', 'hendrix', age = 28)
print(musician)
