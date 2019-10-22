#6.4.2在字典中存储列表

#存储所点的比萨信息
pizza = {
    'crust': 'thick',
    'toppings': {'mushrooms', 'extra cheese'},
    }

#概述所点的比萨

print("You ordered a " + pizza['crust'] + "-crust pizza " +
      "with the following toppings:")

#pizza字典里配料toppings包含配料列表，而不是单个值；
for topping in pizza['toppings']:
    print("\t" + topping)
