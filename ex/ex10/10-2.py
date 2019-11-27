#10-2 replace()替换文字
filename = 'learning_python.txt'

with open(filename) as file_object:
    for line in file_object:
        new_line = line.rstrip()
        print(new_line.replace('Python', 'C'))
