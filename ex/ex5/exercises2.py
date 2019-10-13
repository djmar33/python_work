#5-8以特殊方式跟管理员打招呼

user_groups = ['jerry','tom','admin','kirs','bitch']

for user_group in user_groups:
    if user_group == 'admin':
      print("Hello " + user_group + ", would you like to see a status report?")
    else:
      print("Hello " + user_group.title() + ", thank you for logging in again.")


#5-9判断列表是否为空

user_groups = ['jerry','tom','admin','kirs','bitch']


#增加if判断user_groups列表是否为空，如果不为空将进入for循环
if user_groups:
    for user_group in user_groups:
        if user_group == 'admin':
            print("Hello " + user_group + ", would you like to see a status report?")
        else:
            print("Hello " + user_group.title() + ", thank you for logging in again.")
#如果列表为空，将输入相关提示语；
else:
    print("We need to find some users!")


#5-10检查用户名

current_users = ['jerry','tom','admin','kirs','bitch']

new_users = ['sisi','minmin','yiyi','kirs','jiji']

for new_user in new_users:
    if new_user in current_users:
        print("用户名" + new_user.lower() + "已被占用，请使用别的用户名！" )
    else:
        print("用户名" + new_user.lower() + "已成功注册，感谢！")

#5-11序数

sort_numbers = [2,3,5,6,7,1,4,8,9]
#对列表进行排序
sort_numbers.sort()
for sort_number in sort_numbers:
    if sort_number == 1:
        print("1st\n")
    elif sort_number == 2:
        print("2nd\n")
    elif sort_number == 3:
        print("3rd\n")
    elif sort_number == 4:
        print("4th\n")
    elif sort_number == 5:
        print("5th\n")
    elif sort_number == 6:
        print("6th\n")
    elif sort_number == 7:
        print("7th\n")
    elif sort_number == 8:
        print("8th\n")
    else:
        print("9th\n")
print(max(sort_numbers))
print(min(sort_numbers))
print(sum(sort_numbers))
print(len(sort_numbers))
