#10.2.1写入空文件

#文件赋值给变量filename
filename = 'programming.txt'

#open()有读取模式r，写入模式w，附加模式a，读取和写入r+.默认为r。
#如果文件不存在，open将自动创建。
with open(filename, 'w') as file_object:
    #使用wirte将字符串写入对象。
    #使用模式w切记，如果问你件已存在，python将在返回文件对象前清空。
    #让每个字符串单独占一行，需要增加换行符\n；
    file_object.write("I love programming.\n")

    
    file_object.write("I love creating new games.\n")
