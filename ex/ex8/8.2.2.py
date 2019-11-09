#8.2.2关键字实参

#定义形参animal_type和pet_name；
def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
#关键字实参明确地指出各个实参对应的形参；
#使用关键字实参，务必准确地指定函数定义的形参名；
describe_pet(animal_type='dog', pet_name='feichou')
