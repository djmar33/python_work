#练习
#5-3外星人颜色
alien_color = 'green'
if alien_color == 'green':
	print("获得5个点。")

alien_color = 'yellow'
if alien_color == 'green':
	print("获得5个点。")

alien_color = 'red'
if alien_color == 'green':
	print("获得5个点。")

#5-4外星人颜色2
alien_color = 'green'
if alien_color == 'green':
	print("获得5个点。")
else:
	print("获得10个点。")

#5-5外星人颜色3
alien_color = input("""
	input Color green,red,yellow\n>""")
if alien_color.lower() == 'green':
	print("获得5个点。")
elif alien_color.lower() == 'yellow':
	print("获得10个点。")
else:
	print("获得15个点。")

#5-6人生的不同阶段
age = input("请输入你的年龄：\n")
if int(age) < 2:
	print("你是个小BB哦！")
elif int(age) < 4:
	print("你正在蹒跚学步！")
elif int(age) < 13:
	print("你是一位儿童哦！")
elif int(age) < 20:
	print("你是一位青年！")
elif int(age) < 65:
	print("你是一位成年人！")
else:
	print("你是一位老人！")

#5-7喜欢的水果
favorite_fruits = ['香蕉','榴莲','西瓜']
if '香蕉' in favorite_fruits:
	print("你喜欢香蕉")

if '榴莲' in favorite_fruits:
	print("你喜欢榴莲")

if '苹果' in favorite_fruits:
	print("你喜欢苹果")