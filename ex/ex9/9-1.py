#9-1餐馆

class Restaurant():
    def __init__(self, restaurant, cuisine_type):
        self.restaurant = restaurant
        self.cuisine_type = cuisine_type


    def describe_restaurant(self):
        print(self.restaurant.title() + " restauran is so good!")


    def open_restaurant(self):
        print(self.restaurant.title() + " restaran delicious " +
              self.cuisine_type.title() + ".")


foods = Restaurant('kuaileyuan', 'chicken')
foods.describe_restaurant()
foods.open_restaurant()


two_foods = Restaurant('zhengongfu', 'meat pie')
two_foods.describe_restaurant()

three_foods = Restaurant('miandingxiang', 'face')
three_foods.describe_restaurant()
