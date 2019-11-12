#8.6.3使用as给函数指定别名

#模块导入make_pizza函数，并指定mp别名。
from pizza import make_pizza as mp

#使用别名mp就可以调用；
mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green pepers', 'extra cheese')
