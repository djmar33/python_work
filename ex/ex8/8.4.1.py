#8.4.1在函数中修改列表

def print_models(unprinted_designs, completed_models):
    """
    模拟打印每个设计，直到没有未打印的设计为止
    打印每个设计后，都将其已到列表completed_models中
    """

    while unprinted_designs:
        current_design = unprinted_designs.pop()

        #模拟根据设计制作3D打印模型的过程
        print("Printing model: " + current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """显示打印好的所有模型"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

#创建一个未打印列表；
unprinted_designs = ['iphone case', 'robo pendant', 'dodecachedron']
#创建一个完成列表；
completed_models = []

#调用打印函数，使用位置实参传递给形参；
print_models(unprinted_designs, completed_models)

#调用显示完成函数；
show_completed_models(completed_models)