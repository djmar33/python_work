#1、open函数打开pidigits.txt，存储在file_object中。
#2、使用read函数，读取文件所有内容并赋值给contents；
#3、输出内容；
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    #read()到达文件末尾会返回一个空字符串，所以需要删除；
    print(contents.rstrip())
