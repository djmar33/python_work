#创建一个外星人字典，包含该外星人属性；
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
#输出外星人x_position值；
print("Original x-position: " + str(alien_0['x_position']))

#判断外星人speed值，然后执行对应代码；
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

#最终外星人的x_position 为x_increment值加x_position值；
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))
