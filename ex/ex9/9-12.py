#9-12多个模块
#User存储一个模块里,user_only.py
#Privileges和Admin存储admin_user.py
#创建admin实例

from admin_user import Admin

admin_user = Admin('zhang', 'wenchou', 25)
admin_user.privileges.show_privileges()
