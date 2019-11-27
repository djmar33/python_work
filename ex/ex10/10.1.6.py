#10.1.6包含一百万位大型的文件
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
    
    #使用切片，输出前52位数；
    print(pi_string[:52] + "...")
    #计算pi_string长度
    print(len(pi_string))
