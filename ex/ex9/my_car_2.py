#9.4.4导入整个模块

#导入整个模块，使用句点表示法访问需要的类；
import car_2

my_beetle = car_2.Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = car_2.ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())
