from time import sleep
from random import randint

company_names = ["星辰科技有限公司", "海洋物流有限公司", "绿色能源发展有限公司", "瑞丰投资管理有限公司",
                "智慧城市网络科技有限公司", "神州旅游有限公司", "蓝天环保工程有限公司", "阳光农业科技有限公司",
                "和谐地产有限公司", "时代广告传媒有限公司", "飞龙航空服务有限公司", "美丽家园装饰工程有限公司",
                "金色年华养老服务有限公司", "欣欣向荣贸易有限公司", "神速快递有限公司", "甜蜜时光餐饮管理有限公司",
                "智慧医疗科技有限公司", "碧水蓝天环保工程有限公司", "优学派教育科技有限公司", "神州租车有限公司",
                "阳光保险有限公司", "美丽中国旅游发展有限公司", "和谐家居有限公司", "金色年华酒店管理有限公司",
                "欣欣向荣影视有限公司", "神速物流有限公司", "甜蜜时光烘焙有限公司", "智慧城市安防科技有限公司",
                "碧水蓝天园林工程有限公司", "优学派智能科技有限公司", "神州数码有限公司", "阳光能源有限公司",
                "美丽中国环保有限公司", "和谐地产投资有限公司", "金色年华教育科技有限公司", "欣欣向荣广告传媒有限公司",
                "神速航空服务有限公司", "甜蜜时光餐饮管理有限公司", "智慧城市网络科技有限公司", "碧水蓝天农业科技有限公司",
                "优学派影视有限公司", "神州租车有限公司", "阳光保险有限公司", "美丽家园装饰工程有限公司",
                "和谐家居有限公司", "金色年华养老服务有限公司", "欣欣向荣贸易有限公司", "神速快递有限公司",
                "甜蜜时光餐饮管理有限公司", "智慧医疗科技有限公司", "碧水蓝天环保工程有限公司", "优学派教育科技有限公司",
                "神州旅游有限公司", "阳光农业科技有限公司", "美丽中国旅游发展有限公司", "和谐地产有限公司",
                "金色年华酒店管理有限公司", "欣欣向荣影视有限公司", "神速物流有限公司", "甜蜜时光烘焙有限公司",
                "智慧城市安防科技有限公司", "碧水蓝天园林工程有限公司", "优学派智能科技有限公司", "神州数码有限公司",
                "阳光能源有限公司", "美丽中国环保有限公司", "和谐地产投资有限公司"
]

comapany_dollar = [89, 
                   46, 
                   44, 
                   53, 
                   55, 
                   46, 
                   72, 
                   89, 
                   70, 
                   67, 
                   44, 
                   30, 
                   58, 
                   80, 
                   43, 
                   92, 
                   34, 
                   59, 
                   81, 
                   48, 
                   52, 
                   34, 
                   52, 
                   39, 
                   92, 
                   71, 
                   70, 
                   52, 
                   38, 
                   99, 
                   32, 
                   38, 
                   76, 
                   89, 
                   88, 
                   78, 
                   94, 
                   38, 
                   86, 
                   56, 
                   34, 
                   78, 
                   61, 
                   34, 
                   47, 
                   61, 
                   92, 
                   65, 
                   78, 
                   95, 
                   65, 
                   73, 
                   31, 
                   33, 
                   60, 
                   41, 
                   32, 
                   46, 
                   59, 
                   36, 
                   51, 
                   77, 
                   82, 
                   84, 
                   54, 
                   50, 
                   71, 
                   75, 
                   57, 
                   48, 
                   93, 
                   56, 
                   37, 
                   85, 
                   40, 
                   36, 
                   92, 
                   36, 
                   49, 
                   64, 
                   77, 
                   62, 
                   53, 
                   79, 
                   71, 
                   59, 
                   98, 
                   37, 
                   48, 
                   97, 
                   43, 
                   91, 
                   42, 
                   42, 
                   41, 
                   98, 
                   32, 
                   49, 
                   61, 
                   75]

CompanyNumber = []


comapany_Dict = dict(zip(company_names, comapany_dollar))
for i in range(len(company_names)):
    CompanyNumber.append(i)

for i in comapany_Dict:
    CompanyNumber.append(i)

Comapany_NUMBER_NAME_DICT = dict(zip(CompanyNumber, company_names))
