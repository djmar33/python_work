#8.1.1向函数传递信息

#使用def关键字定义一个greet_user函数。括号里可以包含其他信息，这里将不需要；
#在括号添加username；
def greet_user(username):
    #文档字符串注释，描述函数做什么的，help（）可以查看相关文档；
    """显示简单的问候语"""
    #函数体内代码；
    print("hello!" + username.title())
#调用函数gret_user()；
#在括号将需要传递信息填入；
greet_user('kirs')
