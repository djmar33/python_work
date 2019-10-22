#6-4使用6-3代码，分别输出键或值。
vocabularys = {
    'list': '列表',
    'tupe': '元组',
    'dict': '字典',
    'variable': '变量',
    'if': '判断',
    'set': '集合',
    'sorted': '排序',
    'title': '首字母大写',
    'items': '遍历key,value',
    'keys': '遍历key',
    'value': '遍历value'
    }

for key, value in vocabularys.items():
    print(key.title() + ":" + value)


#6-5河流

#创建一个字典，包括河流及经过国家

three_rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'changjiang': 'china',
    }

#遍历字典
for river, state in three_rivers.items():
    print("The " + river + " runs through " + state + ".")

#遍历所有键
for river in three_rivers.keys():
    print("The three major rivers in the world are " + river)
    
#遍历所有值
for state in three_rivers.values():
    print("The countries where the three major rivers pass " + state)


#6-6调查，判断列表是否在名单里，如果在输出相关提示语。

#创建一个字典。
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

#创建一个调查名单，判断是否在字典里
friends = ['jen','kris','sarah','jerry','tom']

#先遍历调查名单
for friend in friends:
    #判断调查名单是否在字典里，如果是将执行代码，否则输出提示语。
    if friend in favorite_languages.keys():
        print(friend.title() + " ,感谢你参与投票，你喜欢的语言是 " +
              favorite_languages[friend])
    else:
        print(friend.title() + "你没有参与本次投票，欢迎参与，谢谢！")
