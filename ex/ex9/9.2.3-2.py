#9.2.3-3 修改属性的值,并且增加判断语句

#2、通过方法修改属性的值，并且增加判断语句
#增加odometer_reading属性
#增加read_odometer()方法

class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 23

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + self.model
        return long_name

    def read_odometer(self):
        """打印一条指出汽车的里程信息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")
    
    #增加判断语句，避免传递的数值小于原本的；
    def update_odometer(self, mileage):
        """
        将里程表读书设置为指定的值
        禁止将里程表读书往回调
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

#通过方法传递属性的值
my_new_car.update_odometer(10)

