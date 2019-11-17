#9-3用户

class User():
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


    def describe_user(self):
        full_name = self.first_name + " " + self.last_name
        print("Hi, " + full_name)

    def greet_user(self):
        print("You're " + str(self.age) + " years old this year.")


feichou = User('zhang', 'wenchou', 25)
feichou.describe_user()
feichou.greet_user()

tom = User('liang', 'weijie', 27)
tom.describe_user()
tom.greet_user()
