#首先，创建一个待验证用户列表；
#和一个用于存储已验证用户的空列表；

unconfirmed_users = ['alice', 'brian', 'candace']

confirmed_users = []

#验证每个用户，直到没有未验证用户为止；
#将每个经过验证的列表都移到已验证用户列表中；

#判断未验证用户列表是否为空；
while unconfirmed_users:
    #使用pop()弹出未验证列表最后一位元素；
    current_user = unconfirmed_users.pop()
    
    print("Verifying user: " + current_user.title())
    #将弹出的元素添加至已验证列表中；
    confirmed_users.append(current_user)


#显示所有已验证的用户
print("\nThe following users have been confirmed:")

#遍历已验证的用户列表
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
