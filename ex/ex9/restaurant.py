#9-10将Restaurant存储在一个模块中；
"""一组餐馆评价"""

class Restaurant():
    def __init__(self, restaurant, cuisine_type):
        self.restaurant = restaurant
        self.cuisine_type = cuisine_type
        self.number_served = 0


    def describe_restaurant(self):
        """告知餐厅很好吃"""
        print(self.restaurant.title() + " restauran is so good!")


    def open_restaurant(self):
        """告知餐厅有什么吃的"""
        print(self.restaurant.title() + " restaran delicious " +
              self.cuisine_type.title() + ".")
    

    def set_number_served(self):
        """计算今天有多少个人来餐厅"""
        print("There today " + str(self.number_served) + " people in this restaurant.")
    

    def increment_number_served(self, sum):
        """递增人数，并且算出目前总共多少人"""
        self.number_served += sum
        print("There sum " + str(self.number_served) + " pople in this restaurant.")
