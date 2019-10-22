
#6.4.2-1 字典嵌套列表
#遍历字典的for 循环中，需要再使用一个for循环来遍历相对应的列表；

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell']
    }
#for循环，先遍历字典元素；
#再使用for循环，编列字典值里列表的元素；
for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())
