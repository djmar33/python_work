#9-6冰淇淋小店

class Restaurant():
    """模拟一个餐厅，并且该餐厅提供美食"""
    def __init__(self, restaurant, cuisine_type):
        self.restaurant = restaurant
        self.cuisine_type = cuisine_type


    def describe_restaurant(self):
        """输出该餐厅就是好"""
        print(self.restaurant.title() + " restauran is so good!")


    def open_restaurant(self):
        """输出该餐厅有什么美食"""
        print(self.restaurant.title() + " restaran delicious " +
              self.cuisine_type.title() + ".")


class IceCreamStand(Restaurant):
    """创建雪糕店类"""
    def __init__(self, restaurant, cuisine_type):
        """初始化父类属性"""
        super().__init__(restaurant, cuisine_type)
        #添加口味
        self.flavors = ['chocolates', 'vanilla', 'green tea']

#创建雪糕店实例
ice = IceCreamStand('kuaileyuan', 'chicken')
ice.open_restaurant()
for i in ice.flavors:
    print("The taste of ice cream is " + i)
