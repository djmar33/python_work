#5.3.5 省略else语句
age = 64

if age < 4:
	price = 0
elif age < 18:
	price = 5
elif age < 64:
	price = 10
elif age >= 64:
	price = 0
print("Your admission cost is $" + str(price) + "元.")