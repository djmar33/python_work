#8.2.3默认值

#animal_type使用默认值dog；
#函数调用时没有给animal_type实参，默认将会使用dog这个实参；
def describe_pet(pet_name, animal_type='dog'):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
#只指定pet_name实参，animal_type将使用默认值；
#由于animal_type指定了默认值，无需通过实参来指定，因此函数调用中只包含一个实参；
#然而python依然将这个pet_name实参视为位置实参；
#所以需要将pet_name放在形参开头；
#如果不使用默认值，并且按关键字实参覆盖了默认值，将无需考虑位置实参问题；
describe_pet(pet_name='feichou')
