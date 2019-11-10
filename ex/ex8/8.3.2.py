#8.3.2让实参变成可选的

def get_formatted_name(first_name, middle_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    #将full_name的值返回
    return full_name.title()

#将函数返回值复赋值给musician变量；
musician = get_formatted_name('jimi', 'lee', 'hendrix')
print(musician)
