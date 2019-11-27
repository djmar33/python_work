#文件赋值给变量filename；
filename = 'pi_digits.txt'

#使用open打开文件，并且将内容对象存储到变量file_object中；
with open(filename) as file_object:
    #for循环导出每一行数字；
    for line in file_object:
        #每行末尾都有一个隐藏的换行符，由于print会产生一个换行符，所以总共两个；
        #使用rstrip()删除空格；
        print(line.rstrip())
