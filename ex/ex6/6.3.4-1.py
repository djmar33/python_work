#6.3.4-1使用set()集合，剔除重复值

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
print("The following languages have been mentioned:")
#使用set剔除字典值重复项。
for language in set(favorite_languages.values()):
    print(language.title())
