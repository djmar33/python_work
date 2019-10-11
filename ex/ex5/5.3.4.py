#5.3.4 多个elif语句
age = 70

if age < 4:
	price = 0
elif age < 18:
	price = 5
elif age < 64:
	price = 10
else:
	price = 0
print("Your admission cost is $" + str(price) + "元.")