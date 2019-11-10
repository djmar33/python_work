#8.3.2-1让实参变成可选的

#将middle_name中间名指定一个默认值；
def get_formatted_name(first_name, last_name, middle_name=''):
    """返回整洁的姓名"""
    #python中非空字符串解读为true,判断中间名是否为空，如果不是将把中间名字段加上；
    if middle_name:
    	full_name = first_name + ' ' + middle_name + ' ' + last_name
    #如果中间名为空，全名将不会包含中间名；
    else:
    	full_name = first_name + ' ' + last_name
    #将full_name的值返回
    return full_name.title()

#将函数返回值复赋值给musician变量；
musician = get_formatted_name('jimi', 'hendrix',)
print(musician)
