#8.2.4等效的函数调用

#animal_type使用默认形参，所以pet_name需要提供实参；
def describe_pet(pet_name, animal_type='dog'):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

#位置实参
describe_pet('willie')

#关键字实参
describe_pet(pet_name='willie')

#位置形参，并且将animal_type默认值覆盖；
describe_pet('willie', 'hamster')


#关键字实参，并且将animal_type默认值覆盖；
describe_pet(pet_name='willie', animal_type='hamster')

#关键字实参，不在乎形参位置顺序；
describe_pet(animal_type='hamster', pet_name='willie')
