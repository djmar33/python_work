#9.3.5将实例用作属性
#创建Battery类，将电瓶的属性都归于此类，并用该类用作属性值；
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


class Battery():
    """一次模拟电动汽车点评的简单尝试"""

    def __init__(self, battery_size=70):
        """初始化电瓶属性"""
        self.battery_size = battery_size
    
    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")


class ElectricCar(Car):
    """电动汽车的独特之处"""

    def __init__(self, make, model, year):
        """
        初始化父类的属性，再初始化电动汽车特有的属性
        """
        super().__init__(make, model, year)
         #将类作为属性值；
        self.battery = Battery()


my_tesla = ElectricCar('tesla', 'model s', 2016)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
