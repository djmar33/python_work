#7.1.2使用int()获取数值输入

height = input("你的身高多少？")

#将字符串转换为数值；
height = int(height)


#将用户提供信息进行判断；
if height >= 36:
    print("你身高适合玩过山车呀！")
else:
    print("你身高还不适合玩过山车哦~")
