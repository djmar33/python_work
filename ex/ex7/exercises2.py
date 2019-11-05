#7-4比萨配料

prompt = "请输入你的pizaa配料:\n"
prompt += "Enter 'quit' when you are finished."

pizza = ""
while pizza != 'quit':
    pizza = input(prompt)

    if pizza != 'quit':
        print("你的pizza已经添加配料: " + pizza + ".")
