#10.1.4包含文件中各行的列表
#文件赋值给变量filename；
filename = 'pi_digits.txt'

#使用open打开文件，并且将内容对象存储到变量file_object中；
with open(filename) as file_object:
    #readlines()从文件中读取每一行，并存储在一个列表中；
    lines = file_object.readlines()
    #for循环导出每一行数字；
    for line in lines:
        #每行末尾都有一个隐藏的换行符，由于print会产生一个换行符，所以总共两个；
        #使用rstrip()删除空格；
        print(line.rstrip())
