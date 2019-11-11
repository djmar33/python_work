#8-12三文治

def sandwich(*toppings):
    """概述制作三文治材料"""
    print("\n以下是制作三文治的材料:")
    for topping in toppings:
        print("- " + topping)

sandwich('火腿', '鸡蛋', '青菜')

sandwich('西红柿')
