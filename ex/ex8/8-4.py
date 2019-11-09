#8-4 大号T_shirt

def make_shirt(size, prompt='i love python'):
    print("即将制作一件大小为 " + size.upper() + ",标语为 " + prompt.title() + " 的T-shirt.")


#制作一件印有默认字样的大号T，位置实参；
make_shirt('l')

#制作一件印有默认字样的中号T，关键字实参；
make_shirt(size='m')

#制作一件印有其他字样的T,关键字形参，不考虑顺序；
make_shirt(prompt='i love you', size='m')
