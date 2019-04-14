# -*- coding:utf-8 -*-

import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import math
from scipy.stats import norm, poisson
from scipy.interpolate import BarycentricInterpolator
import scipy
from scipy.optimize import leastsq

# matplotlib.rcParams['font.sans-serif'] = [u'SimHei']  #FangSong/黑体 FangSong/KaiTi
# matplotlib.rcParams['axes.unicode_minus'] = False

# 绘制正态分布概率密度函数
def draw_normal_distribution():
    mu = 0
    sigma = 1
    x = np.linspace(mu - 3 * sigma, mu + 3 * sigma, 50)
    y = np.exp(-(x - mu) ** 2 / (2 * sigma ** 2)) / (math.sqrt(2 * math.pi) * sigma)
    # linewidth表示线的宽度，markersize表示点的宽度
    # plt.plot(x, y, 'ro-', linewidth=2, markersize=8)
    plt.plot(x, y, 'r-', x, y, 'go', linewidth=2, markersize=8)
    # 生成网格线
    plt.grid(True)
    plt.show()

# 绘制损失函数：Logistic损失(-1,1)/SVM Hinge损失/ 0/1损失
def draw_loss():
    x = np.linspace(start=-2, stop=3, num=1001, dtype=np.float)
    y_logit = np.log(1 + np.exp(-x)) / math.log(2)
    y_boost = np.exp(-x)
    y_01 = x < 0
    y_hinge = 1.0 - x
    y_hinge[y_hinge < 0] = 0
    plt.plot(x, y_logit, 'r--', label='Logistic Loss', linewidth=2)
    plt.plot(x, y_01, 'g-', label='0/1 Loss', linewidth=2)
    plt.plot(x, y_hinge, 'b-', label='Hinge Loss', linewidth=2)
    plt.plot(x, y_boost, 'm-', label='Adaboost Loss', linewidth=2)
    plt.grid()
    # 显示label在右上侧
    plt.legend(loc='upper right')
    # 存储图片
    # plt.savefig('1.png')
    plt.show()

# 绘制 x * x
def draw_pow():
    x = np.linspace(-1.3, 1.3, 101)
    y = f(x)
    # y = np.power(x, 2)
    plt.plot(x, y, 'g-', label='x^x', linewidth=2)
    plt.grid()
    plt.legend(loc='upper left')
    plt.show()

# x ** x        x > 0
# (-x) ** (-x)  x < 0
def f(x):
    y = np.ones_like(x)
    i = x > 0
    y[i] = np.power(x[i], x[i])
    i = x < 0
    y[i] = np.power(-x[i], -x[i])
    return y

# 胸型线绘制
def draw_chest_line():
    x = np.arange(1, 0, -0.001)
    y = (-3 * x * np.log(x) + np.exp(-(40 * (x - 1 / np.e)) ** 4) / 25) / 2
    plt.figure(figsize=(5, 7))
    plt.plot(y, x, 'r-', linewidth=2)
    plt.grid(True)
    plt.show()

# 心形线绘制
def draw_heart():
    t = np.linspace(0, 7, 100)
    x = 16 * np.sin(t) ** 3
    y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)
    plt.plot(x, y, 'r-', linewidth=2)
    plt.grid(True)
    plt.show()

# 渐开线绘制
def draw_evolvent():
    t = np.linspace(0, 50, num=1000)
    x = t*np.sin(t) + np.cos(t)
    y = np.sin(t) - t*np.cos(t)
    plt.plot(x, y, 'r-', linewidth=2)
    plt.grid()
    plt.show()

# 可以在曲线内显示条形状
def draw_bar():
    # 显示汉字
    matplotlib.rcParams['font.sans-serif'] = [u'SimHei']  #黑体 FangSong/KaiTi
    matplotlib.rcParams['axes.unicode_minus'] = False
    x = np.arange(0, 10, 0.1)
    y = np.sin(x)
    # bar为曲线内添加条状
    plt.bar(x, y, width=0.04, linewidth=0.2)
    plt.plot(x, y, 'r--', linewidth=2)
    plt.title(u'Sin曲线')
    # rotation表示标签顺时针旋转60度
    plt.xticks(rotation=-60)
    # xlabel和ylabel是给x和y轴打标签
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid()
    plt.show()

# 绘制均匀分布
def draw_uniform_distribution():
    # 返回一个或一组0到1之间的随机数或随机数组
    x = np.random.rand(10000)
    t = np.arange(len(x))
    # alpha：透明度 30为条状的数量
    plt.hist(x, 30, color='m', alpha=0.5)
    # plt.plot(t, x, 'r-', label=u'均匀分布')
    plt.legend(loc='upper left')
    plt.grid()
    plt.show()

# 验证中心极限定理
def draw_center():
    t = 10000
    a = np.zeros(1000)
    for i in range(t):
        # numpy.random.uniform(low, high, size)
        # 功能：从一个均匀分布[low, high)中随机采样，注意定义域是左闭右开，即包含low，不包含high.
        a += np.random.uniform(-5, 5, 1000)
    a /= t
    # normed这个参数指定密度, 也就是每个条状图的占比例比, 默认为1
    plt.hist(a, bins=30, color='g', alpha=0.5, normed=True)
    plt.grid()
    plt.show()

# Poisson分布绘制
def draw_poission():
    x = np.random.poisson(lam=5, size=10000)
    pillar = 15
    a = plt.hist(x, bins=pillar, normed=True, range=[0, pillar], color='g', alpha=0.5)
    plt.grid()
    plt.show()
    print (a)
    print (a[0].sum())

# 直方图的绘制
def draw_histogram():
    mu = 2
    sigma = 3
    data = mu + sigma * np.random.randn(1000)
    h = plt.hist(data, 30, normed=1, color='#a0a0ff')
    x = h[1]
    y = norm.pdf(x, loc=mu, scale=sigma)
    plt.plot(x, y, 'r--', x, y, 'ro', linewidth=2, markersize=4)
    plt.grid()
    plt.show()

# 绘制三维图像
def draw_3dimension():
    x, y = np.ogrid[-3:3:100j, -3:3:100j]
    # u = np.linspace(-3, 3, 101)
    # x, y = np.meshgrid(u, u)
    z = x*y*np.exp(-(x**2 + y**2)/2) / math.sqrt(2*math.pi)
    # z = x*y*np.exp(-(x**2 + y**2)/2) / math.sqrt(2*math.pi)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    # ax.plot_surface(x, y, z, rstride=5, cstride=5, cmap=cm.coolwarm, linewidth=0.1)  #
    ax.plot_surface(x, y, z, rstride=5, cstride=5, cmap=cm.Accent, linewidth=0.5)
    plt.show()
    # cmaps = [('Perceptually Uniform Sequential',
    #           ['viridis', 'inferno', 'plasma', 'magma']),
    #          ('Sequential', ['Blues', 'BuGn', 'BuPu',
    #                          'GnBu', 'Greens', 'Greys', 'Oranges', 'OrRd',
    #                          'PuBu', 'PuBuGn', 'PuRd', 'Purples', 'RdPu',
    #                          'Reds', 'YlGn', 'YlGnBu', 'YlOrBr', 'YlOrRd']),
    #          ('Sequential (2)', ['afmhot', 'autumn', 'bone', 'cool',
    #                              'copper', 'gist_heat', 'gray', 'hot',
    #                              'pink', 'spring', 'summer', 'winter']),
    #          ('Diverging', ['BrBG', 'bwr', 'coolwarm', 'PiYG', 'PRGn', 'PuOr',
    #                         'RdBu', 'RdGy', 'RdYlBu', 'RdYlGn', 'Spectral',
    #                         'seismic']),
    #          ('Qualitative', ['Accent', 'Dark2', 'Paired', 'Pastel1',
    #                           'Pastel2', 'Set1', 'Set2', 'Set3']),
    #          ('Miscellaneous', ['gist_earth', 'terrain', 'ocean', 'gist_stern',
    #                             'brg', 'CMRmap', 'cubehelix',
    #                             'gnuplot', 'gnuplot2', 'gist_ncar',
    #                             'nipy_spectral', 'jet', 'rainbow',
    #                             'gist_rainbow', 'hsv', 'flag', 'prism'])]

# 线性回归例1
def linear_regression():
    x = np.linspace(-2, 2, 50)
    A, B, C = 2, 3, -1
    y = (A * x ** 2 + B * x + C) + np.random.rand(len(x))*0.75
    t = leastsq(residual, [0, 0, 0], args=(x, y))
    theta = t[0]
    print ('真实值：', A, B, C)
    print ('预测值：', theta)
    y_hat = theta[0] * x ** 2 + theta[1] * x + theta[2]
    plt.plot(x, y, 'r-', linewidth=2, label=u'Actual')
    plt.plot(x, y_hat, 'g-', linewidth=2, label=u'Predict')
    plt.legend(loc='upper left')
    plt.grid()
    plt.show()


if __name__ == "__main__":
    # draw_normal_distribution()
    # draw_loss()
    # draw_pow()
    # draw_chest_line()
    # draw_heart()
    # draw_evolvent()
    # draw_bar()
    # draw_uniform_distribution()
    # draw_center()
    # draw_poission()
    linear_regression()


