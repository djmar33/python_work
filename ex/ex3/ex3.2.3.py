#练习3-4
#邀约嘉宾名单

danner_names = ['爸爸','妈妈','爷爷','奶奶','婆婆','公公']

print(danner_names[0] + "," + "明天一起吃饭咯！")
print(danner_names[1] + "," + "明天一起吃饭咯！")
print(danner_names[2] + "," + "明天一起吃饭咯！")
print(danner_names[3] + "," + "明天一起吃饭咯！")
print(danner_names[4] + "," + "明天一起吃饭咯！")
print(danner_names[5] + "," + "明天一起吃饭咯！\n\n\n\n")

#修改嘉宾名单

busy_names = danner_names[0]
print(busy_names + "明天没空来不了啊，你们吃吧！\n")
danner_names[0] = "三姑奶"
print(danner_names[0] + "," + "明天一起吃饭咯！")
print(danner_names[1] + "," + "明天一起吃饭咯！")
print(danner_names[2] + "," + "明天一起吃饭咯！")
print(danner_names[3] + "," + "明天一起吃饭咯！")
print(danner_names[4] + "," + "明天一起吃饭咯！")
print(danner_names[5] + "," + "明天一起吃饭咯！\n\n\n\n")


#添加嘉宾
print("我买了张大圆桌，大家都过来吃饭吧！\n")
danner_names.insert(0,"姨仔")
danner_names.insert(3,"妹妹")
danner_names.append("洪梓峰")
print(danner_names[0] + "," + "明天一起吃饭咯！")
print(danner_names[1] + "," + "明天一起吃饭咯！")
print(danner_names[2] + "," + "明天一起吃饭咯！")
print(danner_names[3] + "," + "明天一起吃饭咯！")
print(danner_names[4] + "," + "明天一起吃饭咯！")
print(danner_names[5] + "," + "明天一起吃饭咯！")
print(danner_names[6] + "," + "明天一起吃饭咯！")
print(danner_names[7] + "," + "明天一起吃饭咯！")
print(danner_names[8] + "," + "明天一起吃饭咯！\n\n\n\n")


#缩减名单
print("不好意思，剧情需求，餐桌无法到达，只能两个人参与盛宴！\n")
lower_names = danner_names.pop()
print(lower_names + "不好意思啊，不能一起吃饭啦。")
lower_names = danner_names.pop()
print(lower_names + "不好意思啊，不能一起吃饭啦。")
lower_names = danner_names.pop()
print(lower_names + "不好意思啊，不能一起吃饭啦。")
lower_names = danner_names.pop()
print(lower_names + "不好意思啊，不能一起吃饭啦。")
lower_names = danner_names.pop()
print(lower_names + "不好意思啊，不能一起吃饭啦。")
lower_names = danner_names.pop()
print(lower_names + "不好意思啊，不能一起吃饭啦。")
lower_names = danner_names.pop()
print(lower_names + "不好意思啊，不能一起吃饭啦。")
print(danner_names[0] + "," + "你还是受邀约任务，一起吃饭！")
print(danner_names[1] + "," + "你还是受邀约任务，一起吃饭！")
del danner_names[0]
del danner_names[0]
print(danner_names)
