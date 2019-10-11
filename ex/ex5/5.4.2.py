#5.4.2确定列表不是空

#创建一个空列表
requested_toppings = []

#判断列表是否为空，如果列表有值，返回将会是True。
if requested_toppings :
	for requested_topping in requested_toppings:
		print("Adding " + requested_topping + ".")
#否则将输出提示语；
else:
	print("Are you sure you want a plain pizza?")