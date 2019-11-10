#8.3.4函数和while循环

def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + last_name
    return full_name


while True:
   print("\n请告诉你的名字：")
   f_name = input("姓：")
   l_name = input("名:")

   formatted_name = get_formatted_name(f_name, l_name)
   print("\n您好！ " + formatted_name.title())
