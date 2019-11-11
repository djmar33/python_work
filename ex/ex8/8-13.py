#8-13 用户简介

def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们指导的有关用户的一切"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    
    #将user_info键值对写入profile字典里；
    for key, value in user_info.items():
        profile[key] = value
    
    #返回字典值；
    return profile


user_profile = build_profile('liang', 'weijie', location='shenzhen', love='jerry', wife='feichou')

print(user_profile)
