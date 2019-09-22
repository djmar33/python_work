#3-8放眼看世界

world = ['japan','laos','hongkong','thailand','malaysia']
print("这是我想去的5个国家：\n",world)

#使用sorted()按字母排序
print("使用sorted()函数按字母排序：\n",sorted(world))
print("使用sorted()函数只会临时排序，不影响原始列表元素：\n",world)

#使用sorted()反向排序
print("使用sorted()反向排序：\n",sorted(world,reverse=True))
print("同样也不会影响原来列表顺序：\n",world)

#使用reverse()反向排序
world.reverse()
print("使用reverse()反向排序：\n",world)

#再次使用reverse()反向排序，将恢复默认列表顺序
world.reverse()
print("再次使用reverse()，恢复默认顺序：\n",world)

#使用sort()排序
world.sort()
print("使用sort()函数排序：\n",world)

#使用sort()反向排序
world.sort(reverse=True)
print("使用sort()反向函数排序：\n",world)

#3-9晚餐使用len()长度函数
danner_names = ['废抽','浩哥','爸爸']
print("总共" + str(len(danner_names)) + "人吃晚餐")

#3-10练习本章函数排序
english = ['z','s','e','x','b','o']
print("默认排序：\n",english)

#sortend()
print("sorted()：\n",sorted(english))

#sorted()反向
print("sorted()：\n",sorted(english,reverse=True))

#reverse()
english.reverse()
print("revers()：\n",english)

#reverse()恢复
english.reverse()
print("再次revers(),恢复顺序：\n",english)

#sort()
english.sort()
print("sort()：\n",english)

#sort()反向
english.sort(reverse=True)
print("sort()反向：\n",english)


