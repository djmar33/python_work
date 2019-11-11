#8.4传递列表

#定义一个函数greet_users；
def greet_users(names):
    """向列表中的每位用户都发出简单的问候"""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

#定义一个名字列表；
usernames = ['kirs', 'tom', 'jerry']
#将列表作为实参，使用位置实参传递给形参；
greet_users(usernames)
