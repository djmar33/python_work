#7.2.4使用break退出循环

#提示语
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\nEnter 'quit' when you are finished.\n"



#判断标志当前值是否True，如果是将执行循环；
while True:
    city = input(prompt)
    
    #使用if判断city是否quit，如果是则使用break语句直接退出循环；
    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")
