#6.3.4遍历字典所有的值。使用values()

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
print("The following languages have been mentioned:")
#遍历字典所有的值，并赋值给language该变量。
for language in favorite_languages.values():
    print(language.title())
