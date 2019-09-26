#4.4.1切片使用

players = ['charles','martina','michael','florence','eli']
#players[0:3]，表示从索引0开始，分别输出0,1,2三个元素。
#若要使用最后一个元素，索引需要加1；与range()一样。但是切片索引还是从0开始；
print(players[0:3])

#索引从头开始,可以不需要指定第一个索引
print(players[:3])

#索引直到最后，可以不需要指定最后一个索引
print(players[2:])

#导出列表倒数第三个元素，无论列表怎么变化，都只会导出倒数第三个数；
print(players[-3:])
