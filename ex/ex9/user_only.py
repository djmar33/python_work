#9-12多个模块
#User存储一个模块里,user_only.py
#Privileges和Admin存储admin_user.py

"""显示用户信息"""

class User():
    """模拟用户登录次数"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0


    def describe_user(self):
        """显示全名"""
        full_name = self.first_name + " " + self.last_name
        print("Hi, " + full_name.title())

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
