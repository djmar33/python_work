#9-14创建骰子
#导入随机模块
from random import randint

"""一个骰子游戏"""

class Die():
    #初始化order次数，sides面数属性;
    def __init__(self, order, sides=6):
        self.order = order
        self.sides = sides
    
    def roll_die(self):
        """投掷次数及输出投掷数字"""
        while self.order:
            x = randint(1, self.sides)
            print("roll number is " + str(x))
            self.order -= 1

#创建一个6面骰子，投掷10次
play_roll = Die(10)
play_roll.roll_die()
print("-" * 10)

#创建一个10面骰子，投掷10次
play_roll = Die(10, 10)
play_roll.roll_die()
print("-" * 10)

#创建一个20面骰子，投掷10次
play_roll = Die(10, 20)
play_roll.roll_die()
print("-" * 10)
