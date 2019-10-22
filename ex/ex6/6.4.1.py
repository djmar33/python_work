#6.4.1字典列表

#创建3个包含不同信息的外星人字典；
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

#列表嵌入字典；
aliens = [alien_0, alien_1, alien_2]

#遍历列表所有的字典；
for alien in aliens:
    print(alien)
