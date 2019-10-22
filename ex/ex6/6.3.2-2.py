#6.3.2-2使用key()确定某个人是否被调查。
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

#判断erin是否在favorite_languages字典里，如果不在将输出提示语,请参加投票。
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")
