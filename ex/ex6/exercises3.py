#练习
#6-7 创建3个表示人的字典

feichou = {
    'position': 'lowly',
    'nature': 'not good',
    'sex': 'girl',
    }

haohao = {
    'position': 'rank',
    'nature': 'good',
    'sex': 'boy',
    }

weijie = {
    'position': 'medium',
    'nature': 'medium',
    'sex': 'boy',
    }

peoples = [feichou, haohao, weijie]

for people in peoples:
    print(people)


#6-8 列表嵌套字典

cat_green = {
    '主人': 'liangweijie',
    '类型': '斗牛犬',
    }

cat_yellow ={
    '主人': '自己',
    '类型': '汪汪',
    }

cat_balk ={
    '主人': '自己',
    '类型': '人类',
    }

pets = [cat_green, cat_yellow, cat_balk]

for pet in pets:
    print(pet)



#6-9 字典嵌套列表

favorite_places = {
    'tom': ['北京', '泰国', '日本'],
    'jerry': ['广州', '深圳', '龙岗'],
    'kirs': ['新加坡', '海南', '巴黎'],
    }


for name, places in favorite_places.items():
    print(name.title() + "喜欢去的地方有：")
    for place in places:
        print("\t" + place)


#6-10 字典嵌套列表

favorite_numbers = {
    'tom': [1, 2, 3],
    'jerry': [4, 5, 6],
    'kirs': [7, 8, 9],
    }


for name, numbers in favorite_numbers.items():
    print(name.title() + "喜欢去的数字有：")
    for number in numbers:
        print("\t" + str(number))


#6-10 字典嵌套字典

cities = {
	'深圳': {
	'国家': '中国',
	'人口': '13亿',
	'事实': '强大',
	},
	'曼谷': {
	'国家': '泰国',
	'人口': '6900万',
	'事实': '强大',
	},
	'河内': {
	'国家': '越南',
	'人口': '9554万',
	'事实': '强大',
        },
    }

for city, citie_info in cities.items():
    print("城市：" + city)
    country = citie_info['国家']
    poputation = citie_info['人口']
    fact = citie_info['事实']

    print("它属于 " + country + "，国家人口 " + poputation + ",国家事实 " + fact)
