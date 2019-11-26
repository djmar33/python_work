#9-12多个模块
#User存储一个模块里,user_only.py
#Privileges和Admin存储admin_user.py
#因为Admin需要访问User父类，需要导入

from user_only import User

"""admin权限集"""

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
