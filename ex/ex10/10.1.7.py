#10.1.7圆周率包含生日
#文件赋值给变量filename；
filename = 'pi_million_digits.txt'

#使用open打开文件，并且将内容对象存储到变量file_object中；
with open(filename) as file_object:
    #readlines()从文件中读取每一行，并存储在一个列表中；
    lines = file_object.readlines()

    pi_string = ''
    #for循环导出每一行数字；
    for line in lines:
        pi_string += line.strip()
    
    birthday = input("Enter your birthday, in the form mmddyy:")
    if birthday in pi_string:
        print("Your birthday apperars in the first million digits of pi!")
    else:
        print("Your birthday does not appear in the fist million digits of pi.")
