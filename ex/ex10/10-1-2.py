#各行存储列表中
filename = 'learning_python.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
    for line in lines:
        print(line.rstrip())
    print(lines)
