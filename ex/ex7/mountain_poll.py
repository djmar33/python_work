#7.3.3使用用户输入来填充字典

#创建一个空字典，将存储用户、及喜欢那座山；
responses = {}

#创建一个标志；
polling_active = True

while polling_active:
    #获取用户名字；
    name = input("\nWhat is your name?")
    #获取用户喜欢的山；
    response = input("Whitch mountain would you like to climb someday?")
    #将信息写入列表里；
    responses[name] = response
    
    #询问用户是否还继续调查，如果否将退出调查；
    repeat = input("Would you like to let another person respond?(yes/no)")
    if repeat == 'no':
        #标志赋值为False，将退出循环；
        polling_active = False

print("\n----Poll Results ----\n")
#遍历字典，输出用户和用户喜欢的山；
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")
