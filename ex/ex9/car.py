#9.4.1将Car类存储为一个模块car.py然后进行导入；

"""一个用于表示汽车的类"""

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
