#10.2.3附加到文件

#文件赋值给变量filename
filename = 'programming.txt'

#open()有读取模式r，写入模式w，附加模式a，读取和写入r+.默认为r。
#如果文件不存在，open将自动创建。
with open(filename, 'a') as file_object:
    #使用wirte将字符串写入对象。
    #使用模式a，在文件后面附加内容。
    #让每个字符串单独占一行，需要增加换行符\n；
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")
