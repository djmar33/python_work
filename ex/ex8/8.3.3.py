#8.3.3返回字典

def build_person(first_name, last_name):
    """返回一个字典，其中包含有关一个人的信息"""
    
    #键为fist，而key为形参first_name；
    person = {'fist': first_name, 'last': last_name}
    return person
#使用位置实参对应形参，把信息存储在字典里;
musician = build_person('jimi', 'hendrix')
print(musician)
