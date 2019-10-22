#6.4.1-3 使用for 和if语句修改外星人属性

#创建一个空列表，将存储30个外星人字典信息；
aliens = []

#使用range()，产生30个外星人信息，并且添加到aliens列表里。
for alien_number in range(0,30):
    new_alien = {'color': 'green', 'poions': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['poions'] = 10
        alien['speed'] = 'medium'

print(aliens)
