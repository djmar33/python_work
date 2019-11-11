#8-9魔术师

def show_magicians(names):
    """向列表中魔术师打招呼"""
    print("以下魔术师有：\n")
    for name in names:
        print("欢迎魔术师 " + name.title() + "!")

magicians = ['kirs', 'tom', 'jerry']
show_magicians(magicians)
    
