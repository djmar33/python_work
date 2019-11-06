#7-10 梦想度假胜地

resorts = {}

polling_active = True

while polling_active:
    name = input("您叫什么名字？\n:")
    resort = input("您想去哪里度假啊？\n:")

    resorts[name] = resort

    repeat = input("是否继续调查？[yes/no]")

    if repeat == 'no':
        polling_active = False

print("以下为统计信息：\n")

for name, resort in resorts.items():
    print(name.title() + " 想去 " + resort.title() + "度假游玩。")
