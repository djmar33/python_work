#9-11将9-8所有类存储在user.py模块里，然后导入并创建实例

from user import Admin

admin_user = Admin('zhang', 'wenchou', 25)
admin_user.privileges.show_privileges()
