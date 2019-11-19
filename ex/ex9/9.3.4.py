#9.3.4 重写父类的方法
#Car类增加油箱容量方法fule_gas_tank，并且ElectricCar类也增加fule_gas_tank。
#ElectricCar类与Car父类都存在fule_gas_tank，子类将不考虑父类的方法，而是用子类的方法。

class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.fule_capactiy = 55

    def get_descriptive_name(self):
        """按年份、厂商、型号输出汽车信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()


    def read_odometer(self):
        """显示里程信息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """
        判断里程信息是否往回调整
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage

        else:
            print("You can't roll back an odometer!") 

    def increment_odometer(self, miles):
        """递增里程信息"""
        self.odometer_reading += miles

    def fill_gas_tank(self, fule):
        """增加油箱显示"""
        self.fule_capactiy = fule
        print("Fule Capactiy is : " + str(self.fule_capactiy) + "L.")

#创建子类，子类括号必须包含父类；
class ElectricCar(Car):
    """电动车的独特之处"""

    def __init__(self, make, model, year):
        """初始化父类属性"""
        #super()是一个特殊函数，帮助python将父类和子类关联起来；
        #super()让python调用父类__init__()方法，让实例包含父类所有属性；
        super().__init__(make, model, year)
        #增加子类属性
        self.battery_size = 70
    
    #增加电动车独有的电池信息
    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + " =kWh battery.")

    def fill_gas_tank(self):
        """将提示电动车没有油箱"""
        print("This car doesn't need a gas tank!")

#使用父类创建实例
my_car = Car('toyota', 'levin', 2016)
print(my_car.get_descriptive_name())
my_car.fill_gas_tank(45)

#使用子类创建实例
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()
my_tesla.fill_gas_tank()
