#8.2.1位置实参

#定义形参animal_type和pet_name；
def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
#实参dog,feichou位置必须按形参顺序对应，否则实参与形参对应关系就有误；
describe_pet('dog', 'feichou')
