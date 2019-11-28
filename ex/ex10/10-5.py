#10-5关于编程

filename = 'program.txt'

with open(filename, 'w') as file_object:
    while True:
        print("Enter 'q' to exit.")
        program = input("为何喜欢编程： ")
        if program == 'q':
            break
        else:
            file_object.write(program + "\n")
