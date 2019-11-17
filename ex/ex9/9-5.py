#9-5
#用户

class User():
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0


    def describe_user(self):
        """显示全名"""
        full_name = self.first_name + " " + self.last_name
        print("Hi, " + full_name)

    def greet_user(self):
        """显示年龄"""
        print("You're " + str(self.age) + " years old this year.")


    def increment_login_attempts(self):
        """增加登陆次数"""
        self.login_attempts += 1
        print("Total " + str(self.login_attempts) + " of logins")


    def reset_login_attempts(self):
        """重置登陆次数"""
        self.login_attempts = 0
        print("Reset Login number.")


feichou = User('zhang', 'wenchou', 25)
feichou.describe_user()
feichou.greet_user()
feichou.increment_login_attempts()
feichou.increment_login_attempts()
feichou.increment_login_attempts()
feichou.increment_login_attempts()
feichou.reset_login_attempts()
print("Current login times： " + str(feichou.login_attempts))
