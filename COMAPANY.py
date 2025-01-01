import random
from Page import comapany_Dict

# 确保字典中至少有4个键
# 将字典的键转换为列表，然后随机选择4个键
random_keys = random.sample(list(comapany_Dict.keys()), 5)
