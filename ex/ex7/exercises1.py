#7-1汽车租赁

rent = input("What car would you like to rent?")
print("Let me see if I can find you a " + rent + "。")

#7-2餐馆定位

danner = input("How many people have dinner?")
danner = int(danner)

if danner >= 8:
    print("Sorry, Not enough Seat.You have " + str(danner) + " people.")
else:
    print("Have a good dinner.")

#7-3 10的倍数

number = input("请输入一位数，将判断是否10的倍数:")
number = int(number)

if number % 10 == 0:
    print(str(number) + "是10的倍数。")
else:
    print(str(number) + "不是10的倍数。")
