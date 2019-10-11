#5.4.1
#创建一个列表，列表里包含相关配菜；
requested_toppings = ['mushrooms','green peppers','extra cheese']

#使用for循环，遍历这个列表每个元素；
for requested_topping in requested_toppings:
	#判断这个元素是否green peppers，如果是则输出以下句子；
	if requested_topping == 'green peppers':
		print("Soryy, we are out of green peppers right now.")
	#如果元素不等于green peppers就输出以下句子；
	else:
		print("Adding " + requested_topping + ".")
#循环外增加一个提示语，说明pizza已经完成。
print("\nFinished making your pizza!")