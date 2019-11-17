#9.2.3 修改属性的值

#1、直接修改属性的值
#增加odometer_reading属性
#增加read_odometer()方法

class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + self.model
        return long_name

    def read_odometer(self):
        """打印一条指出汽车的里程信息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

#直接修改属性值
my_new_car.odometer_reading = 23
my_new_car.read_odometer()
