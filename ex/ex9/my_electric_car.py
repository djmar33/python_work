#9.4.2在一个模块中存储多个类
#在一个模块存储多个类后，然后指定单独的ElectricCar类

from car_2 import ElectricCar

my_tesla = ElectricCar('tesla', 'model s', 2016)
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
