#6.3.2遍历所有键
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

#使用for循环遍历字典所有键；
#使用变量name遍历键，这样更直观需要提取相关的信息；
for name in favorite_languages.keys():
    print(name.title())
