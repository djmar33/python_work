#10-4访客名单

filename = 'hello.txt'

with open(filename, 'w') as file_object:
    while True:
        print("Enter 'q' to exit.")
        name = input("请输入你的名字： ")
        if name == 'q':
            break
        else:
            print("Welcome! " + name.title())
            file_object.write(name + "\n")
