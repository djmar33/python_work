#9.5标注库
#collections类中的OrdereDict方法，可以保持字典添加顺序；

#导入OrdereDict方法
from collections import OrderedDict

#OrdereDict创建一个空的有序字典，并存储在favorite_languages中；
favorite_languages = OrderedDict()

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
    language.title() + ".")
