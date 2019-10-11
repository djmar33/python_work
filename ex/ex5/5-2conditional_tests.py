#5-2更多条件测试
#检查两个字符串相等和不等
#False
print("feichou" == "feichou2")
#True
print("feichou" == "feichou")

#lower测试
a = "FEICHOU"
print(a.lower() == "feichou")

#and，只要一个为False就是False

print("结果：",True and False )
print("结果：",True and True ,"\n")

#or,只要一个为True就是True
print("结果：",True or False )
print("结果：",False or False,"\n")

#in语句判断
mama = "废抽"
print("废在妈妈名字里:\n",'废' in mama)

#not in 语句判断
mama = "废抽"
print("废在妈妈名字里:\n",'废' not in mama)