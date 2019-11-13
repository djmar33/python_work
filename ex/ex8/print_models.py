#8-15打印模型

import printing_functions

#创建一个未打印列表；
unprinted_designs = ['iphone case', 'robo pendant', 'dodecachedron']
#创建一个完成列表；
completed_models = []

#调用打印函数，使用位置实参传递给形参；
printing_functions.print_models(unprinted_designs, completed_models)

#调用显示完成函数；
printing_functions.show_completed_models(completed_models)
