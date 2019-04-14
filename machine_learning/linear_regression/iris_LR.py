#!/usr/bin/python
# -*- coding:utf-8 -*-

import pandas as pd

if __name__ == "__main__":
    path = 'iris.data.csv'  # 数据文件路径
    df = pd.read_csv(path)
    # x为取数据所有行的开始到-2列（包左不包右）的数据
    x = df.values[:, :-1]
    # y为取数据的所有行的最后1列数据
    y = df.values[:, -1]
    # print ( 'x = \n', x)
    # print ('y = \n', y)

