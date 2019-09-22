#sore()排序

cars = ['bmw','audi','toyota','subaru']
cars.sort()
print(cars)

#sort()反向排序，传递参数reverse=True


cars = ['bmw','audi','toyota','subaru']
cars.sort(reverse=True)
print(cars)

#sorted()临时排序
cars = ['bmw','audi','toyota','subaru']
print("这是没排序前的列表：\n",cars)
print("这是排序后的列表：\n",sorted(cars))

#sorted()临时反向排序，传递参数reverse=True
cars = ['bmw','audi','toyota','subaru']
print("这是没排序前的列表：\n",cars)
print("这是排序后的列表：\n",sorted(cars,reverse=True))


#reverse()反向排序
cars = ['bmw','audi','toyota','subaru']
print("这是没排序前的列表：\n",cars)
cars.reverse()
print("这是使用reverse()排序后的列表\n",cars)

#len()列表长度
cars = ['bmw','audi','toyota','subaru']
print("列表长度为：",len(cars))
