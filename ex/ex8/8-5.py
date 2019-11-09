#8-5 城市

def describe_city(city, state='china'):
    print("城市： " + city.title() + " 属于这个国家： " + state.title())


#位置实参；
describe_city('shenzhen')

#关键字实参；
describe_city(city='guangzhou')

#关键字形参，不考虑顺序；
describe_city(state='japan', city='tokyo')
