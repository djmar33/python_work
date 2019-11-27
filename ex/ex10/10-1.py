
filename = 'learning_python.txt'

with open(filename) as file_object:
    learns = file_object.read()
    print(learns.rstrip())
