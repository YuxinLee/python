#coding=utf-8

import pandas as pd

# header=None 表示文件里没有头部部分
# seq默认使用逗号隔开
data1 = pd.read_csv("iris.data1.txt", header=None)
data2 = pd.read_csv("iris.data2.txt", header=None)

# data为pandas.core.frame.DataFrame
# 通过data[""]可以设置(添加或者修改)data属性和属性值
data1["种类"] = "花"

#显示所有列
# pd.set_option('display.max_columns', None)
#显示所有行
# pd.set_option('display.max_rows', None)
#设置value的显示长度为100，默认为50
# pd.set_option('max_colwidth',100)
pd.set_option('display.max_rows', None)

# concat 函数为组合数据集, 设置reset_index属性使得组合后的data索引不重复，而是按照索引顺序排列
data = pd.concat([data1, data2]).reset_index(drop=True)


print(data)
print(type(data))