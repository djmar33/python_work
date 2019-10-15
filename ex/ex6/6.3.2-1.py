#6.3.2-1遍历包含指定的键
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
#创建一个指定名称的列表；

friend = ['jen', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    #判断键如果在列表里，将输出喜欢的语言；
    if name in friend:
        print(" Hi " + name.title() +
              ",I see your favorite language is " +
              favorite_languages[name].title())
        
