#favorite_languages，该小结告诉字典书写技巧；

#包含多个键--值对时，建议使用语法书写；
#1、输入左花括号回车，然后下一行缩进四个空格’
#2、指定键--值对，并在后面加上一个逗号,回车自动缩进后续的键--值对；
#3、建议在最后一个键--值对也加上逗号，为后续增加键--值对做好准备；
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

print("Sarah's favorite language is " +
      favorite_languages['sarah'].title() +
      ".")
