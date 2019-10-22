#6.4.3字典嵌套字典

#字典嵌套字典；
#键为用户名，值为字典。字典里包含用户名相关信息；
user = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },
    }
#遍历字典；
for username, user_info in user.items():
    print("\nUsername: " + username)
    #合并字典值，并赋值给full_name变量；
    full_name = user_info['first'] + " "  + user_info['last']
    location = user_info['location']

    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())


