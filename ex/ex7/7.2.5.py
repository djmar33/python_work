#7.2.5 在循环中使用continue

current_number = 0

#打印1-10里的奇数；
while current_number < 10:
    current_number += 1
    
    #使用求模运算，判断是否偶数，将返回循环，不再执行下面代码；
    if current_number % 2 == 0 :
        continue
    
    #如果是奇数将输出信息；
    print(current_number)
