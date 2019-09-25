#4-3数到20
for value in range(1,21):
    print(value)

#4-4一百万，数太大了，无法运行改成100；
number = list(range(1,101))
print(number)
#4-5计算1~100最大的数，最小的数，1~100求和
number = list(range(1,101))
print(max(number))
print(min(number))
print(sum(number))

#4-6奇数
odd_number = []
for value in range(1,21,2):
    odd_number.append(value)
print(odd_number)

#4-7 3的倍数
number = []
for value in range(3,31,3):
    number.append(value)
print(number)

#4-8 立方
squares = []
for value in range(1,11):
    squares.append(value ** 3)
print(squares)

#4-9 立方解析
squares = [ value ** 3 for value in range(1,11)]
print(squares)
