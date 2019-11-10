#8.3.4-1函数和while循环，增加break退出条件

def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + last_name
    return full_name


while True:
   print("\n请告诉你的名字：")
   print("随时输入'q'即将退出程序")
   f_name = input("姓：")
   if f_name == 'q':
       break
   l_name = input("名:")
   if l_name == 'q':
       break

   formatted_name = get_formatted_name(f_name, l_name)
   print("\n您好！ " + formatted_name.title())
