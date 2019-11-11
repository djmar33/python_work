#8-10了不起的魔术师

def make_great(ungreat, great):
    """
    模拟每个魔术师，直到没有魔术师为止
    每个魔术师增加The Great，并已到列表great里；
    """
    while ungreat:
        current_magicians = ungreat.pop()
        completed_magicians = 'The Great' + current_magicians
        great.append(completed_magicians)


def show_magicians(names):
    """向列表中魔术师打招呼"""
    print("以下魔术师有：\n")
    for name in names:
        print("欢迎魔术师 " + name.title() + "!")

#创建一个未增加The Great的魔术师列表;
ungreat = ['kirs', 'tom', 'jerry']
#创建一个空列表，将存储增加The Great魔术师的列表；
great = []
make_great(ungreat, great)
show_magicians(great)
