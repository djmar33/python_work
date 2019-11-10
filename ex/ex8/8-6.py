#8-6城市名

def city_country(city, country):
    citys = city + "," + country
    return citys

musician = city_country('shenzhen', 'china')
print(musician)
musician = city_country('guangzhou', 'china')
print(musician)
musician = city_country('phoenix', 'america')
print(musician)
