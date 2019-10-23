#一般使用input()，需要准确的指出希望用户提供什么信息；

name = input("请输入你的名字：")
print("您好," + name + "!")

#如果提示语超过一行，可以将提示语赋值给一个变量，这样input()会较为清晰；

prompt = "如果你告诉我你是谁，我们可以对你的信息个性化设置。"
prompt += "\n你的姓名是什么？"

name = input(prompt)
print("您好," + name + "!")
