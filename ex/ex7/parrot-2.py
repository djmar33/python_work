#7.2.2让用户选择退出

#提示语
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."

#定义message为空，不然无法进入while循环；
message = ""
#如果不等于quit将一直执行；
while message != 'quit':
    message = input(prompt)
    print(message)
