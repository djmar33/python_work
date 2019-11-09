#8-3 T_shirt

def make_shirt(size, prompt):
    print("即将制作一件大小为 " + size.upper() + ",标语为 " + prompt.title() + " 的T-shirt.")


#位置实参
make_shirt('xl', 'i love you')

#关键字实参
make_shirt(size='xl', prompt='i love you')
