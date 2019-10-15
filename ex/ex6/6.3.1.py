#6.3.1遍历所有键--值对

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

#使用for循环遍历字典所有键--值对；
#key,value两个变量可以自定义；
for key, value in favorite_languages.items():
    print("\nKey: " + key)
    print("Value: " + value)
