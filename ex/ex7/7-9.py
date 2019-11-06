#7-9 五香烟熏牛肉卖完，需要在列表删除
#创建一个三文治列表；
sanwich_orders = ['dog', 'pastrami', 'age', 'pastrami', 'pastrami']

#输出三文治清单；
print(sanwich_orders)

if 'pastrami' in sanwich_orders:
    print("No have pastrami,delete pastrami ing..")
    while 'pastrami' in sanwich_orders:
        sanwich_orders.remove('pastrami')

print("三文治已完成。")

#遍历已完成的三文治清单；
for finished_sandwiche in sanwich_orders:
    print(finished_sandwiche)
