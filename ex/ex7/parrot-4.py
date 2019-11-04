#7.2.3使用标志

#提示语
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program.\n"

#定义个变量作为标志
active = True

#判断标志当前值是否True，如果是将执行循环；
while active:
    message = input(prompt)
    
    #使用if判断message是否quit，如果是将标志赋值为False;
    if message == 'quit':
        active = False
    else:
        print(message)
