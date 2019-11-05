#7-6电影票,break结束
prompt = "请输入您的年龄查看电影票价格：\n"
prompt += "\nEnter 'quit' when you go out."

age = ""
while age != 'qiut':
    age = input(prompt)
    
    if age != 'quit':
        age = int(age)
        if age < 3:
            print("免费")
        elif age <= 12:
            print("10元.")
        else:
            print("15元.")
        
    else:
        break
