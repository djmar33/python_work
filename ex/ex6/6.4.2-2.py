
#6.4.2-2 增加if语句，判断喜欢语言是否只有一个

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell']
    }

for name, languages in favorite_languages.items():
    #判断喜欢语言是否只有一个，如果不是将输出以下代码；
    if len(languages) > 1:
        print("\n" + name.title() + "'s favorite languages are:")
        for language in languages:
            print("\t" + language.title())
    else:
        language = languages[0]
        print("\n" + name.title() + "'s favorite languages is:" +
                  language.title())
