#10-3访客

filename = 'guest_book.txt'

with open(filename, 'w') as file_object:
    while True:
        print("Enter 'q' to exit.")
        name = input("请输入你的名字： ")
        if name == 'q':
            break
        else:
            file_object.write(name + "\n")
