#遍历对象
filename = 'learning_python.txt'

with open(filename) as file_object:
    for line in file_object:
        new_line = line.rstrip()
        print(new_line('Python', 'C'))
