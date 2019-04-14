# -*- coding:utf-8 -*-

import numpy as np

# array方法生成数组，形式为[]，元素由空格分隔，类型为ndarray
# 可以由列表、元组或者组合创建ndarray数组
n = np.array([0,1,2,3,4,9,8,7,6,5,4])
n2 = np.array((4,5,6,7))
n3 = np.array([[1,2],[9,8],(0.1, 0.2)])
b = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

# 强制修改shape
# 注：从(3,4)改为(4,3)并不是对数组进行转置，而只是改变每个轴的大小，数组元素在内存中的位置并没有改变
# 当某个轴为-1时，将根据数组元素的个数自动计算此轴的长度
b.shape = 4,3

# ndim是ndarray的维度
number = n.ndim

# ndarry对象的尺度,显示n行m列，返回元组类型
m = n.shape

# ndarry对象元素的个数
s = n.size

# ndarry对象的元素类型
t = n.dtype

# 创建ndarray类型数组，元素从0到n-1，使用指定起始值、终止值和步长来创建数组
arr = np.arange(10)

# 创建3行6列的全1数组
arr2 = np.ones((3,6))

# 创建3行6列的全0数组,通过dtype参数在创建时指定元素类型
arr3 = np.zeros((3,6), dtype = np.int32)
# 如果更改元素类型，可以使用astype安全的转换
# arr2 = arr3.astype(np.int64)

# 创建3行6列的全5数组
arr4 = np.full((3,6), fill_value=5)

# 创建一个正方的n*n单位矩阵，对角线为1，其余为0
arr5 = np.eye(5)

# reshape(shape) 不改变数组元素，返回一个shape形状的数组，原数组不变，负数应该按照其他的正数进行匹配
a = np.ones((2,3,4))
arr6 = a.reshape((-100,4))
# 数组a和arr6共享内存，修改任意一个将影响另外一个

# np.ones_like(a) 根据数组a的形状生成一个全1数组
# np.zeros_like(a) 根据数组a的形状生成一个全0数组
# np.full_like(a,val) 根据数组a的形状生成一个数组，每个元素值都是val
# np.linspace() 通过指定起始值、终止值和元素个数来创建数组，缺省包括终止值,可以通过endpoint关键字指定是否包括终值
b1 = np.linspace(1, 10, 10)
c = np.linspace(1, 10, 10, endpoint=False)

# 和linspace类似，logspace可以创建等比数列
# 下面函数创建起始值为10^1，终止值为10^2，有20个数的等比数列
d = np.logspace(1, 2, 10, endpoint=True)
# 下面创建起始值为2^0，终止值为2^10(包括)，有10个数的等比数列
f = np.logspace(0, 10, 11, endpoint=True, base=2)

# np.concatenate() 将两个或多个数组合并成一个新的数组

# 例子：
# [[ 0  1  2  3  4  5]
#  [10 11 12 13 14 15]
#  [20 21 22 23 24 25]
#  [30 31 32 33 34 35]
#  [40 41 42 43 44 45]
#  [50 51 52 53 54 55]]
a = np.arange(0, 60, 10).reshape((-1, 1)) + np.arange(6)

# 标准Python的列表(list)中，元素本质是对象。
# 如：L = [1, 2, 3]，需要3个指针和三个整数对象，对于数值运算比较浪费内存和CPU。
# 因此，Numpy提供了ndarray(N-dimensional array object)对象：存储单一数据类型的多维数组。


# 数据的存取
# 切片数据是原数组的一个视图，与原数组共享内容空间，可以直接修改元素值
# a[:5]     a[1:9:2]    a[::-1]：翻转

# 使用布尔数组i作为下标存取数组a中的元素：返回数组a中所有在数组b中对应下标为True的元素
a = np.random.rand(10)
# 大于0.5的元素索引
index = a>0.5
# 大于0.5的元素
b = a[a > 0.5]
# 将原数组中大于0.5的元素截取成0.5, b不受影响
a[a > 0.5] = 0.5










