#6.3.3 使用sorted()排序dirt键的顺序.

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

#使用sorted()将键排序，然后在遍历。
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")
