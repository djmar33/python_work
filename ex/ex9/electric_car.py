#9.4.6在一个模块中导入另一个模块
#首先将两个类存储在一个模块里


"""一组可用于表示电动汽车的类"""
#导入Car类，因为ElectricCar需要访问其父类Car，不然将会导致错误；
from car import Car
class Battery():
    """一次模拟电动汽车点评的简单尝试"""

    def __init__(self, battery_size=70):
        """初始化电瓶属性"""
        self.battery_size = battery_size
    
    def get_range(self):
        """打印一条信息，指出电瓶的续航里程"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270         
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)
    
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

