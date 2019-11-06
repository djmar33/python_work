#7-8 熟食店
#创建一个三文治列表；
sanwich_orders = ['火腿', '鸡蛋', '青菜']
#创建一个三文治空列表；
finished_sandwiches = []
#输出三文治清单；
print(sanwich_orders)

while sanwich_orders:
    #弹出三文治清单；
    sanwich_order = sanwich_orders.pop()
    print("三文治里面有:" + sanwich_order)
    #将弹出清单添加至完成的三文治清单；
    finished_sandwiches.append(sanwich_order)

print("三文治已完成。")

#遍历已完成的三文治清单；
for finished_sandwiche in finished_sandwiches:
    print(finished_sandwiche)
