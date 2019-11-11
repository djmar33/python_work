#8-14 汽车

def make_car(firm, type, **property):
    """创建一个字典，其中包含我们指导的有关用户的一切"""
    car = {}
    car['firm_name'] = firm
    car['type_name'] = type
    
    #将property键值对写入car字典里；
    for key, value in property.items():
        car[key] = value
    
    #返回字典值；
    return car


car = make_car('subaru', 'outback', color='blue', tow_package=True)

print(car)
