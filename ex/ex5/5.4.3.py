#5.4.3使用多个列表
available_toppings = ['mushrooms','olives','green peppers','pepperoni'
                      ,'pineapple','extra cheese']


requested_toppings = ['mushrooms','french fries','extra cheese']

for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print("Adding " + requested_topping + ".")
	else:
		print("Sorry ,we don't have " + requested_topping + ".")
print("Finished making your pizza.")