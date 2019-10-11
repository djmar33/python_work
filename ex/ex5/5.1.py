#5.1 if语句实例，判断列表中bmw如果是小写，就执行首字母大写输出；

cars = ['audi','bmw','subaru','toyota']

for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())