#9-8权限
#将实例用作属性

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


class Admin(User):
    """模拟admin用户可以执行什么"""
    def __init__(self, first_name, last_name, age):
        """初始化父类属性"""
        super().__init__(first_name, last_name, age)
        #增加privileges属性，存储admin可执行任务的列表；
        self.privileges = Privileges()

class Privileges():
    """模拟admin可执行列表"""
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']   

    def show_privileges(self):
        """显示admin管理权限"""
        for i in self.privileges:
            
            print("You " + i)


admin_user = Admin('zhang', 'wenchou', 25)
admin_user.privileges.show_privileges()
